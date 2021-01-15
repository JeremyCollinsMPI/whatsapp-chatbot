from submit_to_dialog_flow import *
from chatdaddy import *
from process_response import *
from time import sleep
from new_flow import *
import os
import json
from use_google_sheet import *
from secrets import *
import logging

logging.basicConfig(filename='chat_manager.log', level=logging.CRITICAL)

class ChatManager:
  def __init__(self, phone_number):
    self.phone_number = phone_number
    self.covid_data = {'phone_number': phone_number}
    self.token = get_authorization_token_for_chatdaddy()

  def send_image(self, url):
    r = send_message_with_image(self.phone_number, url, self.token)
    print(r.json())

  def send_test_message(self):
    r = send_message(self.phone_number, 'hello', self.token)

  def need_to_send_image(self, item):
    if item['type'] == 'image':
      return True
    return False

  def send_image_for_item(self, item):
    '''
    structure will be 'send_image [url]'
    actually could make this better; you could use a dict in the response.
    e.g. {'type': 'text'/'image', 'url': }
    '''
    url = item['url']
    self.send_image(url)
    
  def send_item(self, item):
    if self.need_to_send_image(item):
      self.send_image_for_item(item)
    if item['type'] == 'text':
      r = send_message(self.phone_number, item['text'], self.token)
      print(r.json())

  def run(self):
    token = get_authorization_token_for_chatdaddy()
    while True:
      print('Running')
      chats = get_chats(token)
      chat = find_chat_by_phone_number(self.phone_number, chats)
#       print(chat)
      if not chat == None:
        last_message = find_last_message(chat)
        if not last_message_is_from_me(last_message):
          print('Received text')
          text = get_text_of_message_if_not_from_me(last_message)
          print(text)
          response = process_response(text)  
          for item in response:
            sleep(2)
            self.send_item(item)
      sleep(5)          


from submit_to_dialog_flow import *
from chatdaddy import *
from process_response import *
from time import sleep
from new_flow import *
import os
import json
from use_google_sheet import *
from secrets import *
import logging

logging.basicConfig(filename='chat_manager.log', level=logging.CRITICAL)



class CovidChatManager:

  def process_phone_number(self, x):
    x = x.replace(' ', '')
    if len(x) < 9:
      x = '852' + x
    return x

  def __init__(self, phone_number, order_number, token, df):
    self.original_phone_number = phone_number
    self.token = token
    self.running = False
    self.df = df
    self.phone_number = self.process_phone_number(self.original_phone_number)
    self.order_number = order_number
    self.pickup_locations = {'MK': '旺角', 'TST': '尖沙嘴', 'LAFORD': '勵豐中心'}
    self.mode = 'production'

  def stop(self):
    self.running = False
   
  def make_first_message(self):
    df = self.df
    row = df.loc[(df['客人電話'] == self.original_phone_number) & (df['客人編號'] == self.order_number)]
    name = row['客人姓名'].values[0]
    pickup_method = row['取貨方式'].values[0]
    if pickup_method.upper() in ['MK', 'TST', 'LAFORD']:
      print('*****')
      print(self.original_phone_number)
      print(pickup_method)
      logging.critical('*****')
      logging.critical(self.original_phone_number)
      logging.critical(pickup_method)
      address = self.pickup_locations[pickup_method.upper()]
      address_type = "取貨地址"
    else:
      address_type = "收件地址"
      address = row['取貨地址'].values[0]
    amount = row['貨數量'].values[0]
    order_id = row['客人編號'].values[0]
    message =  "你好,我們是STAY GOLD😊\n\n已收到你的訂單\n\n產品名稱: Arista 即驗即知「新冠病毒」快速測試棒\n\n數量: " + amount + "\n\n收件人: " + name + "\n\n" + address_type + ": " + address + "\n\n訂單編號:" + order_id + "\n請問資料正確嘛?😊"
    return message

  def can_send_message(self):
    return True    

  def send_first_message(self):
    token =self.token
    print(self.phone_number)
    print(self.original_phone_number)
    logging.critical(self.phone_number)
    logging.critical(self.original_phone_number)
    message = self.make_first_message()
    print(message)
    logging.critical(message)
    if self.can_send_message() and not self.mode == 'testing':
      r = send_message(self.phone_number, message, token)
    return r

  def send_sf_number(self, sf_number):
    token =self.token
    message = '你的SF號碼是' + sf_number
    print('----')
    print(self.phone_number)
    print(message)
    logging.critical('----')
    logging.critical(self.phone_number)
    logging.critical(message)
    if not self.mode == 'testing':
      r = send_message(self.phone_number, message, token)
    return r

  def see_if_they_have_confirmed(self, text):
    if text == '正確':
      return True
    else:
      return False

  def check_response_to_first_message(self):
    token = self.token
    chats = get_chats(token)
    chat = find_chat_by_phone_number(self.phone_number, chats)
    can_confirm = False
    if not chat == None:
      last_message = find_last_message(chat)
      print('Last message: ', last_message)
      print('Here')
      if not last_message_is_from_me(last_message):
        print('Received text')
        text = get_text_of_message_if_not_from_me(last_message)
        print(text)
        can_confirm = self.see_if_they_have_confirmed(text)
        if can_confirm:
          message = '謝謝！'
          if not self.mode == 'testing':
            r = send_message(self.phone_number, message, token)

    return can_confirm

    

class NewCovidChatManager:
  def __init__(self):
    self.token = ''
    self.excel_directory = './data'
    self.chat_managers = {}
    self.PRODUCT_SUPPORT = "85291740469-1606794850@g.us"
    self.running = False
    self.numbers_messaged = json.load(open('data/numbers_messaged.json', 'r'))['numbers_messaged']
    self.df = read_from_google_sheet(SPREADSHEET_ID, value_range='A1:AA1000') 
    self.delay = 300
    self.delay2 = 10
    self.sf_numbers_messaged = json.load(open('data/sf_numbers_messaged.json', 'r'))['sf_numbers_messaged']
    self.orders_confirmed = json.load(open('data/orders_confirmed.json', 'r'))['orders_confirmed']
    self.write_to_files = True
    self.mode = 'production'
    
  def download_excel(self, message_id, jid):
    result = download_media_by_jid_and_message_id(jid, message_id, self.token, 'data/data.xls')
      
  def download_any_not_downloaded_excel_sheet(self, messages):
    with open('excel_download_record.json', 'r') as file:
      excel_download_record = json.load(file)
    downloaded_message_ids = excel_download_record['message_ids']
    for message in messages['messages']:
      try:
        keys = message['message'].keys()
      except:
        continue
      if 'documentMessage' in keys:
        message_id = message['key']['id']
        if message_id not in downloaded_message_ids:
          jid = message['key']["remoteJid"]
          if jid == self.PRODUCT_SUPPORT:
            self.download_excel(message_id, jid)
            excel_download_record['message_ids'].append(message_id)
            with open('excel_download_record.json', 'w') as file:
              json.dump(excel_download_record, file)
    
  def update_google_sheet(self):
    return None

  def process_phone_number(self, x):
    x = x.replace(' ', '')
    if len(x) < 9:
      x = '852' + x
    return x
    
  def find_numbers_with_new_orders(self):
    self.df = read_from_google_sheet(SPREADSHEET_ID, value_range='A1:AA1000')   
    df = self.df 
    numbers = df['客人電話']
    orders = df['客人編號']
    names = df['客人姓名']
    amounts = df['貨數量']
    methods = df['取貨方式']
    
    result = []
    for pair in zip(numbers, orders, names, amounts, methods):
      if not pair[0] == None:
        if not len(pair[0]) < 8:
          if not [self.process_phone_number(pair[0]), pair[1]] in self.numbers_messaged:
            print(pair[2])
            print(pair[3])
            if not pair[2] == None and not pair[3] == None and not pair[2] == '' and not pair[3] == '':
              if not pair[4] == None and not pair[4] == '':
                result.append([pair[0], pair[1]])
    return result
     
  def message_any_number_with_a_new_order(self):
    numbers_with_new_orders = self.find_numbers_with_new_orders()
    for pair in numbers_with_new_orders:
      number = pair[0]
      order_number = pair[1]
      self.chat_managers[number] = CovidChatManager(number, order_number, self.token, self.df)
      try:
        r = self.chat_managers[number].send_first_message()
        logging.critical(r)
        logging.critical(r.json())
      except Exception as e:
        logging.exception('', exc_info=e)
      try:
        code = r.json()['code']
      except:
        code = 'none'
      if not code == 401:
        self.numbers_messaged.append([self.process_phone_number(pair[0]), pair[1]])
      sleep(self.delay2)
    if self.write_to_files:
      json.dump({'numbers_messaged': self.numbers_messaged}, open('data/numbers_messaged.json', 'w'), indent=4)
  
  def check_product_support_channel(self):
    PRODUCT_SUPPORT = self.PRODUCT_SUPPORT
    token = self.token
    print('Token: ', token)
    messages = get_messages_by_jid(self.PRODUCT_SUPPORT, token)
    print(messages)
    self.download_any_not_downloaded_excel_sheet(messages)
#     self.update_google_sheet()

  def is_sf_number(self, sf_number):
    if 'SF' in sf_number:
      return True
    else:
      return False

  def check_google_sheet_for_updated_sf_numbers(self):
    self.df = read_from_google_sheet(SPREADSHEET_ID, value_range='A1:AA1000')   
    df = self.df 
    result = []
    for index, row in df.iterrows():
      sf_number = row['SF NO.']
      phone_number = row['客人電話']
      order_number = row['客人編號']
      if not sf_number == None and not phone_number == None:
        if len(sf_number) > 3 and len(phone_number) >= 8:
          if self.is_sf_number(sf_number):
            sf_number = sf_number.replace(' ', '')
            sf_number = sf_number.upper()
            sf_number = sf_number.split('(')[0]
            if not [phone_number, order_number, sf_number] in self.sf_numbers_messaged:
              result.append([phone_number, order_number, sf_number])
    return result

  def send_any_new_sf_numbers(self):
    new_sf_numbers = self.check_google_sheet_for_updated_sf_numbers()
    for item in new_sf_numbers:
      phone_number = item[0]
      order_number = item[1]
      sf_number = item[2]
      try:
        chat_manager = self.chat_managers[phone_number]
      except:
        chat_manager = CovidChatManager(phone_number, order_number, self.token, self.df)
      r = chat_manager.send_sf_number(sf_number)
      logging.critical(r)
      logging.critical(r.json())
      try:
        code = r.json()['code']
      except:
        code = 'none'
      if not code == 401:
        self.sf_numbers_messaged.append([phone_number, order_number, sf_number])
    if self.write_to_files:
      json.dump({'sf_numbers_messaged': self.sf_numbers_messaged}, open('data/sf_numbers_messaged.json', 'w'), indent=4)

  def check_chats_for_response_to_first_message(self):
    for item in self.numbers_messaged:
      phone_number = item[0]
      order_number = item[1]
      print(item)
      if not item[1] in self.orders_confirmed:
        try:
          chat_manager = self.chat_managers[item[0]]
        except:
          chat_manager = CovidChatManager(phone_number, order_number, self.token, self.df)
        can_confirm = chat_manager.check_response_to_first_message()
        if can_confirm:
          self.orders_confirmed.append(order_number)        
#           values = read_from_google_sheet(SPREADSHEET_ID, value_range='A1:AA1000',make_into_df=False)
#           print(values)
#           self.df = read_from_google_sheet(SPREADSHEET_ID, value_range='A1:AA1000')
    if self.write_to_files:
      json.dump({'orders_confirmed': self.orders_confirmed}, open('data/orders_confirmed.json', 'w'), indent=4)        
  def stop(self):
    self.running = False
  


    
  def run(self):
    self.running = True
    while self.running:
      try:
        whatsapp_connected, self.token = check_whatsapp_is_connected()
        if not whatsapp_connected and not self.mode == 'testing':
          print('Whatsapp not connected')
          logging.critical('Whatsapp not connected')
          sleep(600)
          continue
        print('Messaging new orders')
        logging.critical('Messaging new orders')
        self.message_any_number_with_a_new_order()
#         print('Checking chats for responses to first message')
#         self.check_chats_for_response_to_first_message()
        print('Messaging new SF numbers')
        self.send_any_new_sf_numbers()
        sleep(self.delay)
        print('Finished')
        logging.critical('Finished')
      except Exception as e:
        logging.critical(repr(e))

    

