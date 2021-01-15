from serpapi import GoogleSearch

params = {
  "api_key": serp_api_key,
  "engine": "google",
  "q": "100%有機護眼補腦草本口服液 59毫升",
  "location": "Hong Kong",
  "google_domain": "google.com.hk",
  "gl": "hk",
  "hl": "en"
}

def search_on_google(query):
  params['q'] = query
  search = GoogleSearch(params)
  results = search.get_dict()
  return results

