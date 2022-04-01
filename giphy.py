import json

from urllib import parse, request


def giphysearch(search_request):
    url = "http://api.giphy.com/v1/gifs/search"

    params = parse.urlencode({"q": search_request, "api_key": giphykey, "limit": "5"})

    with request.urlopen("".join((url, "?", params))) as response:

        data = json.loads(response.read())

    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == "__main__":
    search_request = input("search: ")
    giphysearch(search_request)
