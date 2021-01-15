from submit_to_dialog_flow import *
from chatdaddy import *
from process_response import *
from time import sleep
from new_flow import *

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


#   def run(self):
#     while True:
#       print('Running')
#       response, self  = process_need_call_api(submit('我要買呢個'), self)
#       print(response)
#       print(self.covid_data['phone_number'])
#       sleep(2)
#       response, self  = process_need_call_api(submit('我要買五個'), self)
#       print(response)
#       sleep(2)
#       print(self.covid_data['phone_number'])
