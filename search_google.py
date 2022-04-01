import requests
import urllib.parse as urlparse
import secrets

def search(query):
    params = {
        "key": secrets.google_key,
        "cx": secrets.google_cx,
        "q": query,
        "start": 0,
        "num": 1,
    }

    gcse_base_url = "https://www.googleapis.com/customsearch/v1"
    url_parts = list(urlparse.urlparse(gcse_base_url))
    url_parts[4] = urlparse.urlencode(params)
    gcse_url = urlparse.urlunparse(url_parts)
    data = requests.get(gcse_url).json()
    if "items" in data.keys():
        items = data["items"]
    else:
        items = None
    # print(items)
    return items


if __name__ == "__main__":
    # check what happens when there is no result on bandcamp
    # search("öfdsouhpvuhpoiuhsdfpouvh")
    search("love")
