from kol import *
from submit_to_dialog_flow import *
from ocr import *



def recognise_image_text(image):
  return detect_text('1.png')

def recognise_brand_in_image_text(image_text):
  return image_text

def need_to_call_api(text):
  if 'call_api' in text:
    return True
  else:
    return False
  
def get_item(response):
  try:
    return response['result']['contexts']['item']
  except:
    return None

def search_for_brand_in_parameters(response):
  try:
    return response['result']['parameters']['brand']
  except:
    return None

def search_for_brand_crude(response):
  print(response)
  response = response['result']['resolvedQuery'].replace('你有冇', '')
  print(response)
  response = response.replace('?', '')
  response = response.replace('？', '')
  response = response.replace('呢個牌子','')
  print(response)
  return response

def get_brand(response):
  brand = None
  try:
    contexts = response['result']['contexts']
    for context in contexts:
      if 'brand-' in context['name']:
        brand = context['name'].replace('brand-', '')
        return brand
    if brand == None:
      brand = search_for_brand_in_parameters(response)
    print("&&&&")
    print(brand)
    print(response)
    if brand == None or brand == '':
      print('MATEY')
      
      brand = search_for_brand_crude(response)
    return brand      

  except:
    return None

def need_to_multiply(text):
  if 'multiply_by' in text:
    return True
  else:
    return False

def process_need_call_api(response):
  text = get_text(response)
  if need_to_call_api(text):
    print('TRUE')
    item = get_item(response)
    brand = get_brand(response)
    print(brand)
    print('***result***')    
    result = search_for_item(brand)

    if result['data']['list'] == []:
      response = submit('product not available')
      return get_text(response)
    else:
      response = '我哋有呢個牌子：\n' + '\n'.join([x['nameHk'] for x in result['data']['list']])
      return response 
  if need_to_multiply(text):
    amount = int(text.replace('multiply_by ', ''))
    return 'Total: $90 x ' + str(amount) + ' = $' + str(amount * 90) + '\n' + '請問你想以咩方式交收？'

  else:
    return get_text(response)