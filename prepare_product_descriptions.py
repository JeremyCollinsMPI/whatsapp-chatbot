from kol import *
from serp_api import *
import json
from translation import *
import os

def make_product_description_file(id, name, description):
  dir = 'product_descriptions'
  dict = {'name': name, 'description': description}
  json.dump(dict, open(dir + '/' + str(id) + '.json', 'w',  encoding='utf8'), indent=4, ensure_ascii=False)
  
def find_description(name, id):
  query = name
  result = search_on_google(query)
  json.dump(result, open('google_results/' + id + '.json', 'w', encoding='utf8'), ensure_ascii=False)
  snippet = result['organic_results'][0]['snippet']
  snippet = translate(snippet)
  return snippet

def prepare_product_descriptions():
  product_to_image_dictionary = {}
  inventory_list = get_entire_inventory_list()[0:100]
#   if not 'google_results' in os.listdir('.'):
#     os.mkdir('google_results')
  for item in inventory_list:
    name = item["nameHk"]
    id = item["ID"]
    print(name, id)
    if name == "" or 'testing' in name:
      continue
    image_url = "https://www.kolpartner.cn/kol-rest/" + item["imageMain"]
#     description = find_description(name, id)
#     make_product_description_file(id, name, description)
    product_to_image_dictionary[name] = image_url
  json.dump(product_to_image_dictionary, open('product_to_image_dictionary.json', 'w', encoding='utf8'), indent=4, ensure_ascii=False)
  
  