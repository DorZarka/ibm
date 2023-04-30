
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def get_translated(j_format):
    return j_format["translations"][0]["translation"]

def english_to_french(english_text):
    try:
        french_text_json = language_translator.translate(
                                text=english_text,
                                model_id='en-fr-CA').get_result()
    except:
        return None
    french_text = get_translated(french_text_json)
    return french_text

def french_to_english(french_text):
    try:
        english_text_json = language_translator.translate(
                                text=french_text,
                                model_id='fr-CA-en').get_result()
    except:
        return None
    english_text = get_translated(english_text_json)
    return english_text

