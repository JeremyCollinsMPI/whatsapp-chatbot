from submit_to_dialog_flow import *
from chatdaddy import *
from process_response import *
from time import sleep
from new_flow import *
from chat_manager import *
from kol import *
import json
from prepare_product_descriptions import *
from use_google_sheet import *
from secrets import *
from new_orders_workflow import *

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

def test42():
  '''
  test writing to/from a google sheet
  '''
  x = read_from_google_sheet('12sqCOpDyM2phs4sqakVoJ24JjVGPgNGY0f7NIyixgII')
  print(x)

def test43():
  new_covid_chat_manager = NewCovidChatManager()
  new_covid_chat_manager.run()

def test44():
  x = read_from_google_sheet('1KJn6tZ39o4lQNGZgAqGZy9HjVFyjUjGFcGrPE8u8Ftg', make_into_df=False)
  print(x) 

def test45():
  new_covid_chat_manager = NewCovidChatManager()
  new_covid_chat_manager.run()

def test46():
  whatsapp_connected, token = check_whatsapp_is_connected()
  print(whatsapp_connected)
  print(token)

def test47():
  token = get_authorization_token_for_chatdaddy()
  r = send_message('447756189127', 'test', token)
  print('hello')
  print(r.json())

def test48():
  chat_manager = ChatManager('447756189127')
  chat_manager.run()

def test49():
  print(classify_chatbot_query('i would like to buy a toothbrush')) 
  chat_manager = ChatManager('447756189127')
  chat_manager.run()

def test50():
  '''
  when a new message comes in, then a chatmanager needs to be created for that number
  passing a token as well
  
  
  '''
  chat_manager_creator = ChatManagerCreator()
  chat_manager_creator.run()

def test51():
  prepare_product_descriptions()

def test52():
  chat_manager_creator = ChatManagerCreator()
  chat_manager_creator.run()

def test53():
  product_descriptions, product_names = load_product_descriptions_and_names()
  product_name_translations = load_product_name_translations(product_names)
  
def test54():
  chat_manager_creator = ChatManagerCreator()
  chat_manager_creator.run()

def test55():
  orders = json.load(open('list_of_orders.json', 'r'))
  for order in orders['data']['list']:
    print(make_message_from_new_order(order))

def test56():
  chat_manager_creator = ChatManagerCreator()
  chat_manager_creator.message_any_new_orders()

def test57():
  '''
  someone asks about a product, and also not necessarily in the same message asks about the price
  let's say in the most recent set of messages
  let's also say there is a check that the user is talking about only one product;
  or alternatively, could return a list of product names and prices
  so you get the most recent sent messages
  so you also need to have it wait a while to make sure all the messages come in, rather than responding immediately
  
  another thing would be if someone asks how much something is when the product is actually named by the chatdaddy user e.g. Queenie.
  
  sticking with the first case for now.
  steps:
  1. get new messages sent by someone.  
  2. have a very strict screening for whether the chatbot can be used to respond.  in this case, you are asking it
  to recognise messages asking about a price of a product.  but the other flow asking for recommendations also has
  to be updated to be stricter.
  3. if one of the messages is asking about the price of a product, it then needs to go back through the most recent
  sent messages by that person (in the first use case) to find the mention of the product.  if it cannot be found, then do not answer.
  4. find products on the website that are most relevant
  5. return a list of products that are relevant with the prices.
  
  '''


  '''
  the next flow I want is images.  a user sends something like 你有冇呢個牌子? and an image.
  the steps:
  1. get new messages sent by someone
  2. screen for whether there is a query about whether they have a certain product; or alternatively whether they are asking for a price.
  perhaps can combine anyway, since it would be usual to give the price. 
  3. go through the messages to find a mention of a product.  if there are messages that are images, then turn them into ocr'd text.  
  if the product mention cannot be found, then do not answer.
  4. find products on the website that are most relevant
  5. return a list of products that are relevant with the prices.
  '''


test57()







