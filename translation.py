from google.cloud import translate_v2 as translate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/src/backer-1585550181964-0c56f7cc1569.json"
translator = translate.Client()


def translate(item):
  return translator.translate(item,target_language='en')['translatedText']


















