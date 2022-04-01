import requests
import random


TenorToken = ""
searchTerm = "emojify"


def get_gif(searchTerm):
    response = requests.get(
        "https://g.tenor.com/v1/search?q={}&key={}&limit=50".format(
            searchTerm, TenorToken
        )
    )
    data = response.json()
    print(data)
    # see urls for all GIFs
    # for result in data['results']:
    # for media in result['media']:
    # print(data['results'][0]['media'][0]['gif']['url'])
    # return data['results'][0]['media'][0]['gif']['url']
    gifrand = random.choice(data["results"])
    gifone = gifrand["media"][0]["tinygif"]["url"]
    gifrand = random.choice(data["results"])
    giftwo = gifrand["media"][0]["tinygif"]["url"]
    gifrand = random.choice(data["results"])
    gifthree = gifrand["media"][0]["tinygif"]["url"]
    # print(gifone)
    print((gifone + " " + giftwo + " " + gifthree))
    return gifone + " " + giftwo + " " + gifthree


if __name__ == "__main__":
    gallery = input("gallery url: ")
    get_gif(searchTerm)
