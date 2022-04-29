import requests
import secrets


def scran(q):
    # url = "https://api-v2.acrcloud.com/api/buckets?region=eu-west-1"
    url = "https://api.edamam.com/api/recipes/v2"
    params = {
        "type": "public",
        "app_id": secrets.edamam_app_id,
        "app_key": secrets.edamam_app_key,
        "random": "true",
        "q": q,
    }

    response = requests.request("GET", url, params=params)
    #print(response.url)
    #print(response.status_code)
    #print(response.text)
    jsonresp = response.json()
    recipe = jsonresp
    print(jsonresp["hits"][0])

    # time = jsonresp["data"][0]["metadata"]["timestamp_utc"]
    # title = (jsonresp["data"][0]["metadata"]["music"][0]['title'])
    return recipe


if __name__ == "__main__":
    scran("vegetarian")
