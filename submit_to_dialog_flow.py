from secrets import *

import requests
import json


def submit(sentence):
  headers = {'Content-Type': 'application/json', 'Authorization': bearer_string}
  dict = {"contexts": ["shop"], "lang": 'en', "query": sentence, "sessionId": "12345", "timezone": "America/New_York"}
  r = requests.post('https://api.dialogflow.com/v1/query?v=20150910', headers=headers, data=json.dumps(dict))
  return r.json()

def get_text(response):
  try:
    return response['result']['fulfillment']['speech']
  except:
    return None

def simple_submit(sentence):
  response = submit(sentence)
  return get_text(response)


