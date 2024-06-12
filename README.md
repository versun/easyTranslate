## easytranslator

A Python package for reliable text translation using multiple free engines with automatic failover.

Currently, it supports the following languages:
- English
- Chinese Simplified
- Chinese Traditional
- Russian
- Japanese
- Korean
- Czech
- Danish
- German
- Spanish
- French
- Indonesian
- Italian
- Hungarian
- Dutch
- Polish
- Portuguese
- Swedish
- Turkish


Installation
-----------
1. Install: `pip install easytranslator`
1. Translate a text:
    ```
    from easytranslator import EasyTranslator

    et = EasyTranslator()
    results = et.translate(
        text="Hello, world!", 
        dest_lang="Chinese Simplified", 
        src_lang="auto", 
        proxies=[])
    print(results) 
    '''
    {
        "translated_text": "你好，世界！",
        "status": "success",
    }
    '''
    ```
1. More details can be found in the [main.py](/easytranslator/main.py) file.