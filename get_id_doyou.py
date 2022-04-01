import requests
import re
import bs4
import os
import time
from pathlib import Path


def get():
    s = requests.Session()
    r = s.get("https://doyoutrackid.com/tracks/today")
    soup = bs4.BeautifulSoup(r.text, features="lxml")
    ultag = soup.find("ul")
    firstli = ultag.find("li")
    
    tracktime = firstli.find(("p", {"class": re.compile(r"^Track_time")}))
    trackartist = firstli.find(("h2", {"class": re.compile(r"^Track_artist")}))
    tracktitle = firstli.find(("h1", {"class": re.compile(r"^Track_title")}))
   
    return tracktime.text + ": " + trackartist.text + " - " + tracktitle.text


if __name__ == "__main__":
    get()
