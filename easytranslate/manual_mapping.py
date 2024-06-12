# Only use to update the Lang Map
# run: python3 manual_lang_map.py
"""
2024-05-29 Lang Map Results:
{'myMemory': {'Czech': 'cs-CZ', 'Danish': 'da-DK', 'German': 'de-DE', 'English': 'en-ZA', 'Spanish': 'es-US', 'French': 'fr-FR', 'Hungarian': 'hu-HU', 'Indonesian': 'id-ID', 'Italian': 'it-IT', 'Japanese': 'ja-JP', 'Korean': 'ko-KR', 'Dutch': 'nl-NL', 'Polish': 'pl-PL', 'Portuguese': 'pt-PT', 'Russian': 'ru-RU', 'Swedish': 'sv-SE', 'Turkish': 'tr-TR', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW'}, 'alibaba': {'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Swedish': 'sv', 'Turkish': 'tr', 'Chinese Simplified': 'zh', 'Chinese Traditional': 'zh-tw'}, 'baidu': {'Czech': 'cs', 'German': 'de', 'English': 'en', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Turkish': 'tr', 'Chinese Simplified': 'zh'}, 'modernMt': {'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'English': 'en', 'Spanish': 'es-ES', 'French': 'fr', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Russian': 'ru', 'Swedish': 'sv', 'Turkish': 'tr', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW'}, 'iciba': {'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Swedish': 'sv', 'Turkish': 'tr', 'Chinese Simplified': 'zh'}, 'google': {'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'English': 'en-US', 'Spanish': 'es', 'French': 'fr', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Swedish': 'sv', 'Turkish': 'tr', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW'}, 'bing': {'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr-CA', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Russian': 'ru', 'Swedish': 'sv', 'Turkish': 'tr', 'Chinese Simplified': 'zh-Hans', 'Chinese Traditional': 'zh-Hant'}, 'lingvanex': {'Czech': 'cs_CZ', 'Danish': 'da_DK', 'German': 'de_DE', 'English': 'en_GB', 'Spanish': 'es_ES', 'French': 'fr_FR', 'Hungarian': 'hu_HU', 'Indonesian': 'id_ID', 'Italian': 'it_IT', 'Japanese': 'ja_JP', 'Korean': 'ko_KR', 'Dutch': 'nl_NL', 'Polish': 'pl_PL', 'Portuguese': 'pt_PT', 'Russian': 'ru_RU', 'Swedish': 'sv_SE', 'Turkish': 'tr_TR', 'Chinese Simplified': 'zh-Hans_CN'}, 'itranslate': {'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'English': 'en-US', 'Spanish': 'es-US', 'French': 'fr-FR', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Russian': 'ru', 'Swedish': 'sv', 'Turkish': 'tr', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW'}, 'sysTran': {'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Swedish': 'sv', 'Turkish': 'tr', 'Chinese Simplified': 'zh'}, 'argos': {'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Swedish': 'sv', 'Turkish': 'tr', 'Chinese Simplified': 'zh'}, 'reverso': {'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Swedish': 'sv', 'Turkish': 'tr', 'Chinese Simplified': 'zh'}, 'deepl': {'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Swedish': 'sv', 'Turkish': 'tr', 'Chinese Simplified': 'zh'}, 'cloudTranslation': {'German': 'de', 'English': 'en-us', 'Spanish': 'es', 'French': 'fr', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt', 'Russian': 'ru', 'Turkish': 'tr', 'Chinese Simplified': 'zh-cn', 'Chinese Traditional': 'zh-tw'}, 'qqTranSmart': {'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Dutch': 'nl', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Russian': 'ru', 'Swedish': 'sv', 'Turkish': 'tr', 'Chinese Simplified': 'zh'}, 'translateCom': {'English': 'en-gb', 'French': 'fr-ca', 'German': 'de', 'Italian': 'it', 'Portuguese': 'pt-br', 'Russian': 'ru', 'Spanish': 'es-la', 'Japanese': 'ja', 'Chinese Simplified': 'zh', 'Chinese Traditional': 'zh-TW', 'Korean': 'ko', 'Polish': 'pl', 'Dutch': 'nl', 'Indonesian': 'id', 'Swedish': 'sv', 'Danish': 'da', 'Czech': 'cs', 'Turkish': 'tr', 'Hungarian': 'hu'}, 'sogou': {'Polish': 'pl', 'Danish': 'da', 'German': 'de', 'Russian': 'ru', 'French': 'fr', 'Korean': 'ko', 'Dutch': 'nl', 'Czech': 'cs', 'Portuguese': 'pt', 'Japanese': 'ja', 'Swedish': 'sv', 'Spanish': 'es', 'Hungarian': 'hu', 'English': 'en', 'Italian': 'it', 'Chinese Simplified': 'zh-CHS'}, 'qqFanyi': {'English': 'en', 'Chinese Simplified': 'zh', 'French': 'fr', 'Spanish': 'es', 'Italian': 'it', 'German': 'de', 'Turkish': 'tr', 'Russian': 'ru', 'Portuguese': 'pt', 'Indonesian': 'id'}, 'papago': {'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Portuguese': 'pt', 'Russian': 'ru', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW'}, 'youdao': {'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Indonesian': 'id', 'Japanese': 'ja', 'Korean': 'ko', 'Portuguese': 'pt', 'Russian': 'ru', 'Chinese Simplified': 'zh-CHS'}, 'iflyrec': {'German': 'de', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Russian': 'ru', 'Chinese Simplified': 'zh'}, 'caiyun': {'English': 'en', 'Spanish': 'es', 'French': 'fr', 'Japanese': 'ja', 'Korean': 'ko', 'Russian': 'ru', 'Chinese Simplified': 'zh'}}
"""
import translators as ts
import langcodes
from .settings import SUPPORTED_LANGUAGES, STABLE_TS

print("Start........")

pool_mapping = {  # for langcodes
    "Chinese": "Chinese Simplified",
    "Chinese Simplified": "Chinese Simplified",
    "Chinese (Simplified)": "Chinese Simplified",
    "Chinese (China)": "Chinese Simplified",
    "Chinese (Simplified, China)": "Chinese Simplified",
    "Chinese Traditional": "Chinese Traditional",
    "Chinese (Traditional)": "Chinese Traditional",
    "Chinese (Taiwan)": "Chinese Traditional",
    "Chinese (Simplified, Taiwan)": "Chinese Traditional",
}


def get_lang_name(code):
    try:
        lang = langcodes.get(code, normalize=False)
        if not lang.is_valid():
            return None

        return pool_mapping.get(
            lang.display_name(), lang.language_name()
        )  # 用于不同格式的code对应的相同语言
    except Exception:
        return None


lang_map = {}
for t in STABLE_TS:
    print("Mapping ", t)
    lang_map[t] = {
        get_lang_name(code): code
        for code in ts.get_languages(t)
        if get_lang_name(code) in SUPPORTED_LANGUAGES
    }

print("DONE------------------------------------")
print("Lang Map:")
print(lang_map)
print("----------------------------------------")
print("Not Support Chinese Simplified services:")

for k, v in lang_map.items():
    if "Chinese Simplified" not in v:
        print(k)

print("----------------------------------------")


# for t,map in lang_map.items():
#     print(t,": ",len(map))

# ts.get_languages('yandex')
# ts.preaccelerate_and_speedtest(timeout=5,if_show_time_stat=True)
