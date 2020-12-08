from submit_to_dialog_flow import *
from chatdaddy import *
from process_response import *
from time import sleep

def test1():
  send_message('hello')

def test2():
  response = submit('i am a cat')
  print(response)

def test3():
  run_api()

def test4():
  convert_csv_to_chatbot()

def test5():
  token = get_authorization_token_for_chatdaddy()
  print(token)

def test6():
  token = get_authorization_token_for_chatdaddy()
  send_message('447756189127', 'test', token)

def test7():
  token = get_authorization_token_for_chatdaddy()
  r = send_message('447756189127', 'test', token)
  chats = get_chats(token)
  
def test8():
  token = get_authorization_token_for_chatdaddy()
  r = send_message('447756189127', 'test', token)
  chats = get_chats(token)
  chat = find_chat_by_phone_number('447756189127', chats)
  last_message = find_last_message(chat)
  if last_message_is_not_from_me(last_message):
    text = get_text_of_message(last_message)
  response = submit(text)
  sleep(5)
  r = send_message('447756189127', response, token)
  
def test9():
  response = process_need_call_api(submit('你有冇呢個牌子？'))
  print(response)
  
def test10():
  response = process_need_call_api(submit('sulhwasoo'))
  print(response)
  response = process_need_call_api(submit('你有冇呢個牌子？'))
  print(response)

def test11():
  image = ''
  image_text = recognise_image_text(image)
  brand = recognise_brand_in_image_text(image_text) 
  response = process_need_call_api(submit(brand))
  response = process_need_call_api(submit('你有冇呢個牌子？'))
  print(get_text(response))

def test12():
  response = process_need_call_api(submit('你有冇arista？'))
  print(response)

def test13():
  response = process_need_call_api(submit('你有冇merries？'))
  print(response) 

def test14():
  response = process_need_call_api(submit('你有冇merries呢個牌子？'))
  print(response)   

def test15():
  response  = process_need_call_api(submit('我要買呢個'))
  print(response)

def test16():
  token = get_authorization_token_for_chatdaddy()
  r = send_message('447756189127', 'test', token)
  while True:
    print('Running')
    chats = get_chats(token)
    chat = find_chat_by_phone_number('447756189127', chats)
    last_message = find_last_message(chat)
    if not last_message_is_from_me(last_message):
      print('Received text')
      text = get_text_of_message_if_not_from_me(last_message)
      print(text)
      response = process_need_call_api(submit(text))
      sleep(2)
      r = send_message('447756189127', response, token)
    sleep(2)
    
def test17():
  response  = process_need_call_api(submit('我要買呢個'))
  print(response)
  sleep(10)
  response  = process_need_call_api(submit('我要買五個'))
  print(response)
  sleep(10)
  response = process_need_call_api(submit('面交'))
  print(response)

def test18():
  token = get_authorization_token_for_chatdaddy()  
  chats = get_chats(token)
  json.dump(chats, open('chats.json', 'w', encoding='utf8'), indent=4, ensure_ascii=False)

def test19():
  response = new_submit('我要買呢個')
  print(response)
  sleep(3)
  response = process_need_call_api(new_submit('我要買五個'))
  print(response)
  

test17()







