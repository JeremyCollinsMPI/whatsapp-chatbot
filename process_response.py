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

def show_covid_landing_message(text):
  if 'covid_landing_message' in text:
    return True
  else:
    return False

def store_name(text):
  if 'store_name' in text:
    return True
  else:
    return False

def store_amount(text):
  if 'store_amount' in text:
    return True
  else:
    return False  

def store_address(text):
  if 'store_address' in text:
    return True
  else:
    return False  

def store_location_number(text):
  if 'store_location_number' in text:
    return True
  else:
    return False  

def finished_delivery(text):
  if 'finished_delivery' in text:
    return True
  else:
    return False  

def finished_pickup(text):
  if 'finished_pickup' in text:
    return True
  else:
    return False 

def produce_report(chat_manager):
  file = open('Orders.csv', 'a')
  file.write('\n')
  file.write('\t'.join([chat_manager.covid_data['name'], chat_manager.covid_data['address'], chat_manager.covid_data['phone_number'], chat_manager.covid_data['amount']]))
  file.close()

def process_need_call_api(response, chat_manager=None):
  text = get_text(response)
  if need_to_call_api(text):
    item = get_item(response)
    brand = get_brand(response)
    result = search_for_item(brand)
    if result['data']['list'] == []:
      response = submit('product not available')
      return get_text(response), chat_manager
    else:
      response = '我哋有呢個牌子：\n' + '\n'.join([x['nameHk'] for x in result['data']['list']])
      return response, chat_manager
  if need_to_multiply(text):
    amount = int(text.replace('multiply_by ', ''))
    return 'Total: $90 x ' + str(amount) + ' = $' + str(amount * 90) + '\n' + '請問你想以咩方式交收？', chat_manager
  if show_covid_landing_message(text):
    response = '''你好,我們是STAY GOLD😊 
這是訂ARISTA 即驗即知 Covid-19 Antigen測試棒的服務。
你叫咩名？ '''
    return response, chat_manager
  if store_name(text):
    name = text.split('store_name')[1]
    chat_manager.covid_data['name'] = name
    return '你想要幾多? (每人限量購買10枝)', chat_manager
  if store_amount(text):
    amount = text.split('store_amount')[1]
    chat_manager.covid_data['amount'] = amount
    return '你要來我哋嘅分店取定係畀一個送貨地址？', chat_manager
  if store_address(text):
    address = text.split('store_address')[1]
    chat_manager.covid_data['address'] = address
    return '''產品名稱: Arista 即驗即知「新冠病毒」快速測試棒 
    數量: ''' + chat_manager.covid_data['amount'] + '''
    收件人: ''' + chat_manager.covid_data['name'] + '''
    收件地址: ''' + chat_manager.covid_data['address'] + '''
    訂單編號: 1234
    請問資料正確嘛?😊 ''', chat_manager   
  if store_location_number(text):
    location_number = text.split('store_location_number')[1]
    locations = ['瓏門冰室銅鑼灣分店', '瓏門冰室尖沙嘴分店', '瓏門冰室沙田分店', '瓏門冰室荃灣分店', '瓏門冰室屯門分店', 'Maxi House 黃竹坑道49號得力工業大廈16樓F室']
    location = locations[int(location_number)]
    chat_manager.covid_data['address'] = location
    return '''產品名稱: Arista 即驗即知「新冠病毒」快速測試棒 
    數量:''' + chat_manager.covid_data['amount'] + '''
    收件人''' + chat_manager.covid_data['name'] + '''
    取貨地址: ''' + location + '''
    訂單編號: 1234
    請問資料正確嘛?😊''', chat_manager
  if finished_delivery(text):
    produce_report(chat_manager)
    return '謝謝😊我們寄出後會給你順豐號的🙏', chat_manager
  if finished_pickup(text):
    produce_report(chat_manager)
    return '最快需要明天。你要幾時來攞?', chat_manager
  return get_text(response), chat_manager
  
  
  
  
  
  