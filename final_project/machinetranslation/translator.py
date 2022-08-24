import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """ Takes English text as input, 
        and returns French translation."""
    try:
        translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
        french_dump = json.dumps(translation, indent=2, ensure_ascii=False)
        french_text = json.loads(french_dump)
        return french_text["translations"][0]['translation']
    except:
        return "Value cannot be empty."

def french_to_english(french_text):
    """ Takes French text as input, 
        and returns English translation."""
    try:
        translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
        english_dump = json.dumps(translation, indent=2, ensure_ascii=False)
        english_text = json.loads(english_dump)
        return english_text["translations"][0]["translation"]
    except ValueError:
        return "Value cannot be empty."

