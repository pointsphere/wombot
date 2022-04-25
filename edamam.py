import requests
import secrets

def scran(q):
  #url = "https://api-v2.acrcloud.com/api/buckets?region=eu-west-1"
  url = "https://api.edamam.com/api/recipes/v2"
  params={
      "type": "public",
      "app_id": "69b36727",
      "app_key": "279e31ad74b2d652be7d7d0a5c3ffee0",
      "random": "true",
      "q": q
  }
  '''headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer 1b47aee2dba1dd811452e2eae5bfb5a5' 
  }'''

  response = requests.request("GET", url, params=params)
  print(response.url)
  print(response.status_code)
  print(response.text)
  jsonresp = response.json()

  print(jsonresp)

  #time = jsonresp["data"][0]["metadata"]["timestamp_utc"]
  #title = (jsonresp["data"][0]["metadata"]["music"][0]['title'])
  artists = ''
  for item in jsonresp["data"][0]["metadata"]["music"][0]['artists']:
    if artists == '':
      artists = str(item.get('name'))
    else:
      artists = artists + " / " + str(item.get('name'))
    hours = time.split(" ")[1]
    return hours,artists,title

if __name__ == "__main__":
    jsonresp = scran("vegetarian")
    print(jsonresp)
    