import requests




def get_kol_token(): 
  r = requests.post("https://www.kolpartner.cn/kol-rest//auth/login", data={"username":"adminWendy", "password":"admin123"})
  return r.json()['data']['token']

def get_inventory_list(kol_token=None):
  if kol_token==None:
    kol_token = get_kol_token()
  r = requests.get("https://www.kolpartner.cn/kol-rest/product?page=1&count=10&direction=desc&categoryID=0&status=&declaration=&orderBy=ID", headers={'Authorization': kol_token})
  return r.json()

def search_for_item(search_term, kol_token=None):
  if kol_token==None:
    kol_token = get_kol_token()
  r = requests.get("https://www.kolpartner.cn/kol-rest/product?page=1&count=10&direction=desc&categoryID=0&status=&declaration=&orderBy=ID&search=" + search_term, headers={'Authorization': kol_token})
  return r.json()

