from submit_to_dialog_flow import *
from chatdaddy import *
from process_response import *
from time import sleep
from new_flow import *
from chat_manager import *
from kol import *
import json
from prepare_product_descriptions import *

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
  response = new_submit('我要買五個')
  print(response)
  
def test20():
  print(translate('我要買五個'))

def test21():
  conversation = ['我要買呢個', '我要買五個', '面交', '你幾時閂門？', '我可以五點來']
  for x in conversation:
    response = process_need_call_api(submit(x))
    print(response)
    sleep(2)

def test22():
  token = get_authorization_token_for_chatdaddy()  
  chats = get_chats(token)
  json.dump(chats, open('covid_chats.json', 'w', encoding='utf8', indent=4, ensure_ascii=False))

def test23():
  chat_manager = ChatManager('34508')
  response, chat_manager  = process_need_call_api(submit('我要買呢個'), chat_manager)
  print(response)
  print(chat_manager.covid_data['phone_number'])
  sleep(2)
  response, chat_manager  = process_need_call_api(submit('我要買五個'), chat_manager)
  print(response)
  sleep(2)
  response, chat_manager = process_need_call_api(submit('面交'), chat_manager)
  print(response)

def test24():
  chat_manager = ChatManager('34508')
  chat_manager.run()

def test25():
  chat_manager = ChatManager('447756189127')
  conversation = ['ARISTA 即驗即知 Covid-19 Antigen測試棒訂購', 'Jeremy Collins', '我要買五個', '送貨', '22 Caine Road, Hong Kong', 'yes', 'thanks!']
  for x in conversation:
    response, chat_manager  = process_need_call_api(submit(x), chat_manager)
    print(response)
    sleep(2)

def test26():
  chat_manager = ChatManager('447756189127')
  chat_manager.run()

def test27():
  chat_manager = ChatManager('447756189127')
  conversation = ['ARISTA 即驗即知 Covid-19 Antigen測試棒訂購', 'Jeremy Collins', '3', '取貨', '1', 'yes', '我可以五點來嗎']
  for x in conversation:
    response, chat_manager  = process_need_call_api(submit(x), chat_manager)
    print(response)
    sleep(2)  

def test28():
  thing = get_inventory_list()
  json.dump(thing, open('inventory_list.json', 'w', encoding='utf8'), indent=4, ensure_ascii=False)

def test29():
  chat_manager = ChatManager('85291740469')
  chat_manager.run()

def test30():
  chat_manager = ChatManager('447756189127')
  conversation = ['ARISTA 即驗即知 Covid-19 Antigen測試棒訂購', 'Jeremy Collins', '3', '取貨', '1', 'yes', '我可以五點來嗎']
  for x in conversation:
    response, chat_manager  = process_need_call_api(submit(x), chat_manager)
    print(response)
    sleep(2)

def test31():
  response = process_need_call_api(submit('你有冇merries呢個牌子？'))
  print(response)  
 
def test32():
  chat_manager = ChatManager('447756189127')
  chat_manager.run()

def test33():
  chat_manager = ChatManager('447756189127')
  chat_manager.send_image('http://homepages.cae.wisc.edu/~ece533/images/airplane.png')
#   chat_manager.send_test_message()

def test34():
  chat_manager = ChatManager('447756189127')
  chat_manager.run()

def test35():
  print(recommendation_flow('d'))
  
def test36():
  '''
  now going to use backer in the recommendation flow
  
  '''
  print(recommendation_flow('d'))

def test37():
  '''
  now going to use backer in the recommendation flow
  
  '''
  print(recommendation_flow('Do you have anything for oily skin?'))

def test38():
  chat_manager = ChatManager('447756189127')
  chat_manager.run()

'''
next steps

need to deploy backer on google cloud

need to put the chatbot on the server

need to reconcile this version of the chatbot with the covid order chatbot

need to get the inventory of products from the website and get descriptions for at least some of them

need to have a pipeline of finding the image url to send given a product name or id.




'''

def test39():
  inventory_list = get_entire_inventory_list()

def test40():
  chat_manager = ChatManager('447756189127')
  chat_manager.run()

def test41():
  prepare_product_descriptions()



test40()







