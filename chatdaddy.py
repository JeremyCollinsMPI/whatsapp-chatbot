import requests

'''
chatdaddy documentation:
https://api-wa.chatdaddy.tech/docs/#/
'''

def get_authorization_token_for_chatdaddy():
  body = {"username": "robotdata.ai",
  "password": "P@ssw0rd"}
  r = requests.post('https://api-auth.chatdaddy.tech/oauth/token', json=body)
  return r.json()['accessToken']

def send_message(phone_number, message, token):
  body = {
  "jid": phone_number + "@s.whatsapp.net",
  "text": message
  }
  headers = {"Authorization": "Bearer " + token}
  r = requests.post('https://api-wa.chatdaddy.tech/messages/' + phone_number + '@s.whatsapp.net', headers=headers, json=body)
  return r

def get_chats(token):
  headers = {"Authorization": "Bearer " + token}
  r = requests.get('https://api-wa.chatdaddy.tech/chats', headers=headers)
  return r.json()

def find_chat_by_phone_number(phone_number, chats):
  for member in chats['chats']:
    if member['jid'] == phone_number + "@s.whatsapp.net":
      return member
  return None
  
def find_last_message(chat):
  return chat['messages'][-1]

def last_message_is_from_me(message):
  return message['key']['fromMe']

def get_text_of_message_if_not_from_me(message):
  return message['message']['conversation']

def check_whatsapp_is_connected():
  token = get_authorization_token_for_chatdaddy()
  headers = {"Authorization": "Bearer " + token}
  r = requests.get('https://api-wa.chatdaddy.tech/', headers=headers)
  return r.json()['connections']['phone'], token

def send_message_with_image(phone_number, url, token):
  if '.png' in url.lower():
    mimetype = 'image/png'
  if '.jpg' in url.lower():
    mimetype = 'image/jpeg'
  print(url)
  body = {
  "jid": phone_number + "@s.whatsapp.net",
  "image": {"url": url, "mimetype": mimetype, "name": "test"}
  }
  headers = {"Authorization": "Bearer " + token}
  r = requests.post('https://api-wa.chatdaddy.tech/messages/' + phone_number + '@s.whatsapp.net', headers=headers, json=body)
  print(body)
  return r
  
def get_messages_by_jid(jid, token):
  headers = {"Authorization": "Bearer " + token}
  r = requests.get('https://api-wa.chatdaddy.tech/messages/' + jid + '?count=20', headers=headers)
  return r.json()

def download_media_by_jid_and_message_id(jid, message_id, token, filename):
  '''
  this should download some media, presumably to whatever download folder is set for whatsapp
  '''
  headers = {"Authorization": "Bearer " + token}
  string = 'https://api-wa.chatdaddy.tech/messages/' + jid + '/' + message_id + '/media'
  r = requests.get(string, headers=headers)
  output = open(filename, 'wb')
  output.write(r.content)
  output.close()