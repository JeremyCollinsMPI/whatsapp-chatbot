from submit_to_dialog_flow import *
from chatdaddy import *
from process_response import *
from time import sleep
from new_flow import *
import os
import json
from use_google_sheet import *
from secrets import *

class ChatManager:

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

#   def run(self):
#     self.running = True
#     token =self.token
#     while self.running:
#       print('Running')
#       print(self.phone_number)
#       print(self.original_phone_number)
#       message = self.make_first_message()
#       print(message)
# #       if can_send_message:
# #         r = send_message(self.phone_number, message, token)
#       self.stop()
#       chats = get_chats(token)
#       chat = find_chat_by_phone_number(self.phone_number, chats)
#       print(chat)
#       if not chat == None:
#         last_message = find_last_message(chat)
#         if not last_message_is_from_me(last_message):
#           print('Received text')
#           text = get_text_of_message_if_not_from_me(last_message)
#           print(text)
#           response, self = process_need_call_api(submit(text), self)
#           r = send_message(self.phone_number, response, token)
#           sleep(2)

  def send_first_message(self):
    token =self.token
    print(self.phone_number)
    print(self.original_phone_number)
    message = self.make_first_message()
    print(message)
    if self.can_send_message():
      r = send_message(self.phone_number, message, token)

class NewCovidChatManager:
  def __init__(self):
    self.token = get_authorization_token_for_chatdaddy()
    self.excel_directory = './data'
    self.chat_managers = {}
    self.PRODUCT_SUPPORT = "85291740469-1606794850@g.us"
    self.running = False
    self.numbers_messaged = json.load(open('data/numbers_messaged.json', 'r'))['numbers_messaged']
    self.df = read_from_google_sheet(SPREADSHEET_ID, value_range='A1:AA1000') 
    self.delay = 6
    
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
    result = []
    for pair in zip(numbers, orders):
      if not pair[0] == None:
        if not len(pair[0]) < 8:
          if not [self.process_phone_number(pair[0]), pair[1]] in self.numbers_messaged:
            result.append([pair[0], pair[1]])
    return result
     
  def message_any_number_with_a_new_order(self):
    numbers_with_new_orders = self.find_numbers_with_new_orders()
    for pair in numbers_with_new_orders:
      number = pair[0]
      order_number = pair[1]
      self.chat_managers[number] = ChatManager(number, order_number, self.token, self.df)
      self.chat_managers[number].send_first_message()
      self.numbers_messaged.append([self.process_phone_number(pair[0]), pair[1]])
      sleep(self.delay)
    json.dump({'numbers_messaged': self.numbers_messaged}, open('data/numbers_messaged.json', 'w'), indent=4)
  
  def check_product_support_channel(self):
    PRODUCT_SUPPORT = self.PRODUCT_SUPPORT
    token = self.token
    print('Token: ', token)
    messages = get_messages_by_jid(self.PRODUCT_SUPPORT, token)
    print(messages)
    self.download_any_not_downloaded_excel_sheet(messages)
#     self.update_google_sheet()

  def check_google_sheet_for_updated_sf_numbers(self):
    return None
  
  def stop(self):
    self.running = False
  
  def run(self):
    self.running = True
    while self.running:
      self.check_product_support_channel()
      self.message_any_number_with_a_new_order()
      sleep(300)
      self.check_google_sheet_for_updated_sf_numbers()
    
  def run(self):
    self.message_any_number_with_a_new_order()

    
    
    