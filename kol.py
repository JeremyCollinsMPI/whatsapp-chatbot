import requests
import json
import os


def get_kol_token(): 
  r = requests.post("https://www.kolpartner.cn/kol-rest//auth/login", data={"username":"adminWendy", "password":"admin123"})
  return r.json()['data']['token']

def get_inventory_list(kol_token=None, count=10, page=1):
  if kol_token==None:
    kol_token = get_kol_token()
  r = requests.get("https://www.kolpartner.cn/kol-rest/product?page=" + page + "&count=" + count + "&direction=desc&categoryID=0&status=&declaration=&orderBy=ID", headers={'Authorization': kol_token})
  return r.json()

def search_for_item(search_term, kol_token=None):
  if kol_token==None:
    kol_token = get_kol_token()
  r = requests.get("https://www.kolpartner.cn/kol-rest/product?page=1&count=10&direction=desc&categoryID=0&status=&declaration=&orderBy=ID&search=" + search_term, headers={'Authorization': kol_token})
  return r.json()

def get_entire_inventory_list(kol_token=None):
  if 'inventory_list.json' in os.listdir('.'):
    return json.load(open('inventory_list.json', 'r'))
  if kol_token==None:
    kol_token = get_kol_token()
  result = []
  for i in range(1, 143):
    r = requests.get("https://www.kolpartner.cn/kol-rest/product?page=" + str(i) + "&count=10&direction=desc&categoryID=0&status=&declaration=&orderBy=ID", headers={'Authorization': kol_token})
    inventory_list = r.json()['data']['list']
    result = result + inventory_list
  json.dump(result, open('inventory_list.json', 'w', encoding="utf8"), indent=4, ensure_ascii=False)
  return result
  