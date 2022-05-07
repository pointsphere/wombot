import requests
import secrets



def get_id_nts_one():
    # via broadcast monitoring, does not include some IDs for some reason
    # url = "https://api-v2.acrcloud.com/api/bm-bd-projects/2078/channels/306866/results?type=last"

    # via Broadcast Monitoring Custom Stream
    # https://stream.palanga.live:8443/palanga128.mp3
    url = "https://api-v2.acrcloud.com/api/bm-cs-projects/14794/streams/s-D4qSSvT6/results?type=last"
    payload = {}
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + secrets.acrcloud_token,
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    jsonresp = response.json()
    time = jsonresp["data"][0]["metadata"]["timestamp_utc"]
    title = jsonresp["data"][0]["metadata"]["music"][0]["title"]
    artists = ""
    for item in jsonresp["data"][0]["metadata"]["music"][0]["artists"]:
        if artists == "":
            artists = str(item.get("name"))
        else:
            artists = artists + " / " + str(item.get("name"))

        return time, artists, title

def get_id_nts_two():
    # via broadcast monitoring, does not include some IDs for some reason
    url = "https://api-v2.acrcloud.com/api/bm-bd-projects/2078/channels/100265/results?type=last"

    # via Broadcast Monitoring Custom Stream
    # url = "https://api-v2.acrcloud.com/api/bm-cs-projects/14794/streams/s-o7qMI47t/results?type=last"
    payload = {}
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + secrets.acrcloud_token,
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    jsonresp = response.json()
    print(jsonresp)
    time = jsonresp["data"][0]["metadata"]["timestamp_utc"]
    title = jsonresp["data"][0]["metadata"]["music"][0]["title"]
    artists = ""
    for item in jsonresp["data"][0]["metadata"]["music"][0]["artists"]:
        if artists == "":
            artists = str(item.get("name"))
        else:
            artists = artists + " / " + str(item.get("name"))

        return time, artists, title

def get_id_noods():
    # via broadcast monitoring, does not include some IDs for some reason
    url = "https://api-v2.acrcloud.com/api/bm-bd-projects/2078/channels/280334/results?type=last"

    # via Broadcast Monitoring Custom Stream
    # url = "https://api-v2.acrcloud.com/api/bm-cs-projects/14794/streams/s-o7qMI47t/results?type=last"
    payload = {}
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + secrets.acrcloud_token,
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    jsonresp = response.json()
    print(jsonresp)
    time = jsonresp["data"][0]["metadata"]["timestamp_utc"]
    title = jsonresp["data"][0]["metadata"]["music"][0]["title"]
    artists = ""
    for item in jsonresp["data"][0]["metadata"]["music"][0]["artists"]:
        if artists == "":
            artists = str(item.get("name"))
        else:
            artists = artists + " / " + str(item.get("name"))

        return time, artists, title


def get_id_palanga():
    # via broadcast monitoring, does not include some IDs for some reason
    # url = "https://api-v2.acrcloud.com/api/bm-bd-projects/2078/channels/306866/results?type=last"

    # via Broadcast Monitoring Custom Stream
    # https://stream.palanga.live:8443/palanga128.mp3
    url = "https://api-v2.acrcloud.com/api/bm-cs-projects/14794/streams/s-o7qMI47t/results?type=last"
    payload = {}
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + secrets.acrcloud_token,
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    jsonresp = response.json()
    time = jsonresp["data"][0]["metadata"]["timestamp_utc"]
    title = jsonresp["data"][0]["metadata"]["music"][0]["title"]
    artists = ""
    for item in jsonresp["data"][0]["metadata"]["music"][0]["artists"]:
        if artists == "":
            artists = str(item.get("name"))
        else:
            artists = artists + " / " + str(item.get("name"))

        return time, artists, title


if __name__ == "__main__":
    jsonresp = get_id_noods()
    print(jsonresp)
