import requests
import secrets

def get_id_noods():
  #url = "https://api-v2.acrcloud.com/api/buckets?region=eu-west-1"

  # via broadcast monitoring, does not include some IDs for some reason
  #url = "https://api-v2.acrcloud.com/api/bm-bd-projects/2078/channels/306866/results?type=last"

  # via Broadcast Monitoring Custom Strea
  url = "https://api-v2.acrcloud.com/api/bm-cs-projects/14794/streams/s-o7qMI47t/results?type=last"
  payload={}
  headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' +secrets.acrcloud_token
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  print(response.text)
  jsonresp = response.json()

  print(jsonresp)
  time = jsonresp["data"][0]["metadata"]["timestamp_utc"]
  title = (jsonresp["data"][0]["metadata"]["music"][0]['title'])
  artists = ''
  for item in jsonresp["data"][0]["metadata"]["music"][0]['artists']:
    if artists == '':
      artists = str(item.get('name'))
    else:
      artists = artists + " / " + str(item.get('name'))
    hours = time.split(" ")[1]
    return hours,artists,title

if __name__ == "__main__":
    jsonresp = get_id_noods()
    print(jsonresp)
    