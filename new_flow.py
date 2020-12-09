from translation import *


def translate_from_chinese(text):
  if method == 'google-translate':
    return translate(text)
  else:
    return None

def boolean_ask(text, query):
  if text == 'I want to buy it' and query == '我要買呢個':
    return True
  elif text == '我要買五個' and query == 'I want to buy five':
    return True
  else:
    return False

def ask_how_many(text):
  return 'five'

def extract_amount(text):
  how_many = ask_how_many(text)
  if how_many.lower() == 'five':
    return 5

def respond(text, query):
  if query == 'I want to buy it':
    return '你要買幾多？'
  if query == 'I want to buy five':
    return 'multiply_by ' + str(extract_amount(text))
  return None

def new_submit(text):
  text = translate_from_chinese(text, method='google-translate')
  to_query = ['我要買呢個', '我要買五個']
  for query in to_query:
    if boolean_ask(text, query):
      return respond(text, query)
  return None
