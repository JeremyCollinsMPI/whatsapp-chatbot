from backer.example_flows import *
import json

def load_product_to_image_dictionary():
  product_to_image_dictionary = json.load(open('product_to_image_dictionary.json', 'r'))
  return product_to_image_dictionary 

def load_product_descriptions_and_names():
  dir_name = 'product_descriptions'
  dir = os.listdir(dir_name)
  product_descriptions = []
  product_names = []
  for i in range(0,10000):
    if str(i) + '.json' in dir:
      with open(dir_name + '/' + str(i) + '.json', 'r') as file:
        dict = json.load(file)
        product_descriptions.append(dict['description'])
        product_names.append(dict['name'])  
  return product_descriptions, product_names


def recommendation_flow(text):
  product_descriptions, product_names = load_product_descriptions_and_names()
  product_to_image_dictionary = load_product_to_image_dictionary()
  query = text
  print(product_descriptions)
  print(product_names)
  text_response, product = find_most_relevant_products(query, product_names, product_descriptions, use_api=True)
  image = product_to_image_dictionary[product]
  response = [{'type': 'text', 'text': text_response}, {'type': 'image', 'url': image}]
  return response
  

  
  
  
# def find_most_relevant_products(query, product_names, product_descriptions):
#   relevant_descriptions = is_most_relevant_document(query, product_descriptions)['result']
#   to_search_through = zip(product_names, product_descriptions)
#   result = [x[0] for x in to_search_through if x[1] in relevant_descriptions]
#   if result == []:
#     return '[transfer to agent]'
#   elif len(result) == 1:
#     return '我們可以推薦' + result[0]
#   elif len(result) > 1:
#     return "我們可以推薦一下的產品: \n" + "\n".join(result)
# 
# def load_product_descriptions():
#   dir_name = 'product_descriptions'
#   dir = os.listdir(dir_name)
#   result = []
#   for i in range(0,10000):
#     if str(i) + '.txt' in dir:
#       with open(dir_name + '/' + str(i) + '.txt', 'r') as file:
#         result.append(file.read())
#   return result