# test_easy_translate.py
import pytest
from easytranslator import EasyTranslator, WeightedRoundRobin
from easytranslator.main import EasyTranslatorError
from easytranslator.settings import SUPPORTED_LANGUAGES, STABLE_TS

@pytest.fixture
def et():
    return EasyTranslator()
    
def test_init(et):
    assert len(et.translators) == len(STABLE_TS)
    #assert len(et.top_translators) == 3
    #assert len(et.remaining_translators) == len(STABLE_TS)-3

def test_weighted_round_robin(et):
    wrr = WeightedRoundRobin(et.translators)
    weights = [translator["priority"] for translator in et.translators]

    assert wrr.current_index == -1
    assert wrr.current_weight == 0
    assert wrr.weights == weights
    assert wrr.total_weight == sum(weights)
    
    current_weight = wrr.total_weight - et.translators[0]["priority"]

    translators_len = len(et.translators)
    translators_with_priority = [t["priority"] for t in et.translators]

    current_weight = sum(translators_with_priority)-translators_with_priority[0]
    for i, translator in enumerate(et.translators):
        translator_obj = wrr.get_next_translator()
        assert translator_obj == translator
        assert wrr.current_index == i
        assert wrr.current_weight == current_weight

        if i < translators_len - 1:
            current_weight -= translators_with_priority[i+1]

def test_translate(et):
    result = et.translate('Hello', dest_lang='Chinese Simplified')
    assert result['status'] == 'success'
    assert result['translated_text'] in ['您好','你好']

    result = et.translate('World', dest_lang='Chinese Simplified')
    assert result['status'] == 'success'
    assert result['translated_text'] in ['世界']

    result = et.translate('', dest_lang='Chinese Simplified')
    assert result['status'] == 'error'

    result = et.translate('World', dest_lang='zh-CN')
    assert result['status'] == 'error'

def test_translate_batch(et):
    results = et.translate_batch(['Hello', 'World'], dest_lang='Chinese Simplified', src_lang='en')
    assert len(results) == 2
    assert results['Hello']['status'] == 'success'
    assert results['World']['status'] == 'success' 
    assert results['Hello']['translated_text'] in ['您好','你好']
    assert results['World']['translated_text'] in ['世界']

def test_adjust_translator(et):
    translator = et.translators[1]
    old_priority = translator["priority"]
    
    et.adjust_translator(translator, 1)
    assert translator["priority"] == old_priority + 1
    
    et.adjust_translator(translator, -old_priority)
    assert translator["priority"] == 1

def test_get_translator(et):
    assert et.get_translator('google')
    assert not et.get_translator('haha')

def test_get_supported_language(et):
    assert len(et.get_supported_language()) == len(SUPPORTED_LANGUAGES)

def test_set_priority(et):
    et.set_priority('myMemory', 100)
    assert et.get_translator('myMemory').get('priority') == 100

    with pytest.raises(EasyTranslatorError) as excinfo:
        et.set_priority('haha', 100)
    assert str(excinfo.value) == "Translator haha not supported"

