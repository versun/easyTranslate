import logging
import concurrent.futures
import random
# import bisect
import translators as ts
from easytranslator.settings import SUPPORTED_LANGUAGES, STABLE_TS, LANG_MAP
from requests.exceptions import HTTPError
import itertools
from typing import Optional, List, Dict


class EasyTranslatorError(Exception):
    pass

class WeightedRoundRobin:
    def __init__(self, translators):
        self.translators = translators
        self.weights = [translator["priority"] for translator in translators]
        self.total_weight = sum(self.weights)
        self.current_index = -1
        self.current_weight = 0

    def get_next_translator(self):
        while True:
            self.current_index = (self.current_index + 1) % len(self.translators)
            if self.current_index == 0:
                self.current_weight = self.total_weight

            if self.weights[self.current_index] > 0:
                self.current_weight -= self.weights[self.current_index]
                return self.translators[self.current_index]

class EasyTranslator:
    TIMEOUT = 10
    SLEEP_SECONDS = 0
    UPDATE_SESSION_AFTER_FREQ = 1000
    UPDATE_SESSION_AFTER_SECONDS = 1500

    def __init__(self, translators=[]):
        stable_ts = translators if translators else STABLE_TS
        self.translators: List[dict] = sorted(stable_ts, key=lambda x: x["priority"])
        self.wrr = WeightedRoundRobin(self.translators)

    def get_translator(self, translator_id: str) -> Optional[Dict]:
        return next((t for t in self.translators if t["id"] == translator_id), None)

    def get_supported_language(self) -> List:
        return SUPPORTED_LANGUAGES

    def set_priority(self, translator_id: str, priority: int) -> List[Dict]:
        translator = self.get_translator(translator_id)
        if not translator:
            raise EasyTranslatorError(f"Translator {translator_id} not supported")
        translator["priority"] = priority
        self.translators = sorted(self.translators, key=lambda x: x["priority"])
        self.wrr = WeightedRoundRobin(self.translators)
        return self.translators

    def adjust_translator(self, translator, offset):
        logging.info("Adjusting translator %s by offset %s", translator['id'],offset)
        translator["priority"] = max(translator["priority"] + offset, 0)
        self.translators = sorted(self.translators, key=lambda x: x["priority"])
        self.wrr = WeightedRoundRobin(self.translators)

    def translate_with_translator(
        self,
        translator: dict,
        text: str,
        dest_lang: str,
        src_lang: str = "auto",
        proxies: List = [],
    ) -> Dict:

        translator_id = translator["id"]
        translator_lang_map = LANG_MAP[translator_id]

        if dest_lang not in translator_lang_map:
            return {
                "translated_text": None,
                "status": "error",
                "error_info": f"{dest_lang} is not in {translator_id}'s Lang Map, Please check the SUPPORTED_LANGUAGES",
            }
        try:
            logging.info("Translation using %s: %s", translator_id,text)
            result = ts.translate_text(
                text,
                translator=translator_id,
                from_language=src_lang,
                to_language=translator_lang_map[dest_lang],
                timeout=self.TIMEOUT,
                proxies=proxies,
                sleep_seconds=self.SLEEP_SECONDS,
                update_session_after_freq=self.UPDATE_SESSION_AFTER_FREQ,
                update_session_after_seconds=self.UPDATE_SESSION_AFTER_SECONDS,
            )

            if result:
                self.adjust_translator(translator, -1)
                return {"translated_text": result, "status": "success"}
        except ConnectionError as e:
            self.adjust_translator(translator, 2)
            logging.warning("Failed to translate using %s: ConnectionError, %s", translator_id,e)
        except TimeoutError as e:
            self.adjust_translator(translator, 3)
            logging.warning("Failed to translate using %s: TimeoutError, %s", translator_id,e)
        except Exception as e:
            self.adjust_translator(translator, 3)
            logging.warning("Failed to translate using %s: Exception, %s", translator_id,e)

        return {
            "translated_text": None,
            "status": "error",
            "error_info": f"Failed to translate using {translator_id}",
        }

    def translate(
        self, text: str, dest_lang: str, src_lang: str = "auto", proxies: List = []
    ) -> Dict:
        if not text or not dest_lang:
            return {
                "translated_text": None,
                "status": "error",
                "error_info": "Text or dest_lang is empty",
            }

        for _ in range(len(self.translators)):
            translator = self.wrr.get_next_translator()
            if dest_lang not in LANG_MAP[translator["id"]]:
                continue
    
            result = self.translate_with_translator(
                translator, text, dest_lang, src_lang, proxies
            )
            if result.get("status") == "success":
                return result

        logging.error("All services failed to translate!")
        return {
            "translated_text": None,
            "status": "error",
            "error_info": "All services failed to translate!",
        }

    def translate_batch(
        self, text_list: list, dest_lang: str, src_lang: str = "auto"
    ) -> Dict:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = {
                text: translation
                for text, translation in zip(
                    text_list,
                    executor.map(
                        self.translate,
                        text_list,
                        itertools.repeat(dest_lang),
                        itertools.repeat(src_lang),
                    ),
                )
            }
        return results
