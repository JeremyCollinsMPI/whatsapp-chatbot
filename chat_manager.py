from submit_to_dialog_flow import *
from chatdaddy import *
from process_response import *
from time import sleep
from new_flow import *

class ChatManager:
  def __init__(self, phone_number):
    self.phone_number = phone_number
    self.covid_data = {'phone_number': phone_number}

  def run(self):
    token = get_authorization_token_for_chatdaddy()
    while True:
      print('Running')
      chats = get_chats(token)
      chat = find_chat_by_phone_number(self.phone_number, chats)
      print(chat)
      if not chat == None:
        last_message = find_last_message(chat)
        if not last_message_is_from_me(last_message):
          print('Received text')
          text = get_text_of_message_if_not_from_me(last_message)
          print(text)
          response, self = process_need_call_api(submit(text), self)
          r = send_message(self.phone_number, response, token)
          sleep(2)

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
