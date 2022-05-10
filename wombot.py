import get_id_nts
import get_id_doyou
import ch
import random
import sys
import re
from pathlib import Path
import os
import os.path
import time
from collections import defaultdict
import validators
import search_google
import logging as LOGGER
from datetime import datetime

import secrets
import data_pics_wombat
import data_pics_capybara
import data_pics_otter
import data_pics_quokka
import data_txt_fortunes as fortunes

import sqliteclass
import acrcloud
import ntsweirdo
from datetime import datetime, date
import pytz
import edamam
from os import environ

import shazam_api.shazam
import json


db = sqliteclass.sqlite3class()

# environ['VAR_NAME']


if sys.version_info[0] > 2:
    import urllib.request as urlreq
else:
    import urllib2 as urlreq

nts_user = secrets.nts_user
nts_pass = secrets.nts_pass
giphy_key = secrets.giphy_key
chatango_user = secrets.chatango_user
chatango_pass = secrets.chatango_pass
tenor_key = secrets.tenor_key

shazam_api_key = secrets.shazam_api_key

myrooms = []
myrooms.append(environ["wombotmainroom"])
myrooms.append(environ["wombottestroom"])


commandlist = [
    "help",
    "fortune",
    "id1",
    "id2",
    "iddy",
    "ev",
    "eval",
    "e",
    "bbb",
    "gif",
    "gift",
    "bigb",
    "b2b2b",
    "say",
    "kiss",
    "shoutout",
    "chunt",
    "mods",
    "tag",
    "g",
    "wombat",
    "capybara",
    "otter",
    "quokka",
    "ntsweirdo",
]

helpmessage = (
    "commands: \r \r "
    + "GIFs: \r!gif (random dance gif) \r!gift / !b2b / !bbb (more gifs) \r"
    + "!shoutout [user]  \r "
    + "!fortune (your daily fortune)  \r \r "
    + "!id1 for NTS1 \r!id2 for NTS2 \r!iddy for DoYouWorld \r \r"
    + "gifs curated by oscmal, bigbunnybrer and others \r \r"
    + "keep chuntin!"
)

shoutstart = [
    "out to you, ",
    "out to the absolute legend ",
    "much love out to ",
    "out to the amazing ",
    "out to the unimitable",
]

shoutend = ["😘", "❤️", "💙", "*h*", "<3"]

gifhosts = ["https://c.tenor.com/", "https://media.giphy.com/"]

basepath = Path().absolute()

allgif_file = os.path.join(basepath, "allgif.txt")
if not os.path.exists(allgif_file):
    with open(allgif_file, "a") as file:
        pass
else:
    with open(allgif_file) as file:
        allgif_set = set(line.strip() for line in file)

print("init variables done")
##Dance moves!
# kinda useless

# dancemoves = ["(>^.^)>", "(v^.^)v", "v(^.^v)", "<(^.^<)"]

##Setting Pretty Colors
# Font setting for your bot


class WomBot(ch.RoomManager):
    def on_init(self):
        self.set_name_color("255")
        self.set_font_color("0C96E4")
        self.set_font_face("0")
        self.set_font_size(10)
        self.enable_bg()
        print("wombot on_init")

    ##Connecting
    # This is what will be printed on your python console when event called

    def on_connect(self, room):
        print("Connected")

    def on_reconnect(self, room):
        print("Reconnected")

    def on_disconnect(self, room):
        print("wombot.py, on_disconnect, Disconnected")

    def on_message(self, room, user, message):
        try:
            if room.get_level(self.user) > 0:
                print(user.name, message.body, room.get_level(user))
            else:
                print(user.name, message.body, room.get_level(user))
            if self.user == user:
                return

            if message.body[0] == "!":  ##Here is the Prefix part
                data = message.body[1:].split(" ", 1)
                if len(data) > 1:
                    orig_cmd, args = data[0], data[1]
                else:
                    orig_cmd, args = data[0], ""
                cmd = orig_cmd.lower()
                ##COMMANDS!
                # Setting up commands for your bot

                ##Eval
                ##You may want/need to evaluate something about your bot.
                """
                if cmd == "ev" or cmd == "eval" or cmd == "e":
                    room.delete_message(message)
                    ret = eval(args)
                    if ret == None:
                        room.message("Done.")
                        return
                    room.message(str(ret))
                    """
                if self._sleepmode == True:
                    if cmd == ("start"):
                        room.delete_message(message)
                        if room.get_level(user) > 0:
                            self._sleepmode = False
                else:

                    if cmd == ("stop" or "sleep"):
                        room.delete_message(message)
                        if room.get_level(user) > 0:
                            self._sleepmode = True

                    elif cmd == "help":
                        print(helpmessage)
                        room.delete_message(message)
                        room.message(helpmessage)
                        self.pm.message(user, helpmessage)

                    elif cmd == "disconnect":
                        room.delete_message(message)
                        if room.get_level(user) > 0:
                            print("should now disconnect")
                            room.disconnect()

                    elif cmd == "fortune":
                        room.delete_message(message)
                        room.message(
                            "your fortune, "
                            + user.name
                            + " : "
                            + (random.choice(fortunes.fortunecookie))
                            .replace(".", "")
                            .lower()
                        )

                    elif cmd in [
                        "legalize",
                        "legalizeit",
                        "legalise",
                        "legalize it",
                        "legalise it",
                        "blaze",
                        "420",
                        "blazeit",
                        "blaze it",
                        "blazin",
                    ]:
                        room.delete_message(message)
                        room.message(
                            random.choice(db.fetch_gif("bbb"))
                            + " "
                            + "https://media.giphy.com/media/VeGFReghsvt05wD341/giphy.gif"
                        )

                    elif cmd in ["whatdoesthatmean", "benufo", "bufo"]:
                        room.delete_message(message)
                        room.message(
                            "https://f001.backblazeb2.com/file/chuntongo/ben_ufo-whatdoesthatmean.mp3"
                        )

                    elif cmd == "wombat":
                        room.delete_message(message)
                        room.message(random.choice(data_pics_wombat.pics))

                    elif cmd == "capybara":
                        room.delete_message(message)
                        room.message(random.choice(data_pics_capybara.pics))

                    elif cmd == "otter":
                        room.delete_message(message)
                        room.message(random.choice(data_pics_otter.pics))

                    elif cmd == "quokka":
                        print("quokka")
                        room.delete_message(message)
                        room.message(random.choice(data_pics_quokka.pics))

                    elif cmd == "tags":
                        room.delete_message(message)
                        taglist_all = db.cursor.execute(
                            "SELECT tag_name FROM tag_table"
                        )
                        taglist = db.cursor.fetchall()

                        thelongeststring = (
                            "to tag a gif: !tag link-to-the-gif tagname \r"
                        )
                        for key in taglist:
                            thelongeststring += "!" + key + " "
                        print(thelongeststring)

                        self.pm.message(user, str(thelongeststring))

                    elif cmd == "tag":
                        room.delete_message(message)
                        if room.get_level(user) > 0:
                            if args:
                                args = args.replace(",", " ")
                                splitargs = args.split(" ")
                                inurl = splitargs[0]
                                intags = splitargs[1:]
                                if not inurl.startswith("http"):
                                    room.message("!tag url-to-gif tag1 tag2 tag3")
                                else:
                                    for intag in intags:
                                        intag = intag.strip()
                                        db.tag(inurl, intag)

                    elif cmd == "untag":
                        room.delete_message(message)
                        if room.get_level(user) > 0:
                            if args:
                                splitargs = args.split(" ")
                                inurl = splitargs[0]
                                intag = splitargs[1]
                                db.untag(inurl, intag)

                    elif cmd in ["id1", "idch1", "idnts1", "nts1"]:
                        room.delete_message(message)
                        # room.message('!id maintenance. please visit https://www.nts.live/live-tracklist/1')
                        time, artists, title = acrcloud.get_id_nts_one()
                        print(time, artists, title)

                        tz = pytz.timezone("UTC")
                        naive_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                        utc_time = naive_time.replace(tzinfo=pytz.UTC)
                        london_tz = pytz.timezone("Europe/London")
                        london_time = utc_time.astimezone(london_tz)
                        string_time = str(london_time)
                        lesstime = string_time.split(" ")[1].split(":")
                        hoursmins = str(lesstime[0]) + ":" + str(lesstime[1])
                        print(hoursmins)
                        googlequery = artists + " " + title
                        res = search_google.search(googlequery)
                        print(res)
                        if res is not None:
                            bc_link = res[0]["link"]
                            print(bc_link)
                            if ("track" or "album") in bc_link:
                                room.message(
                                    "ID NTS1: "
                                    + hoursmins
                                    + " - "
                                    + artists
                                    + " - "
                                    + title
                                    + " | maybe it's: "
                                    + bc_link
                                )
                            else:
                                room.message(
                                    "ID NTS1: "
                                    + hoursmins
                                    + " - "
                                    + artists
                                    + " - "
                                    + title
                                    + " | no bandcamp found. "
                                )
                        else:
                            room.message(
                                "ID NTS1: "
                                + hoursmins
                                + " - "
                                + artists
                                + " - "
                                + title
                                + " | no bandcamp found. "
                            )

                        # code if ID ripped from website
                        """
                        trackid_unstripped = get_id_nts.run("1")
                        trackid_split = trackid_unstripped.split("\n")
                        stripped = trackid_unstripped.replace("\n", " - ").replace(
                            "\r", " - "
                        )
                        googlequery = trackid_split[1] + " " + trackid_split[2]
                        res = search_google.search(googlequery)
                        if res is not None:
                            bc_link = res[0]["link"]
                            if ("track" or "album") in bc_link:
                                room.message(
                                    "ID NTS1: " + stripped + " | maybe it's: " + bc_link
                                )
                            else:
                                room.message(
                                    "ID NTS1: " + stripped + " | no bandcamp found. "
                                )
                        else:
                            room.message(
                                "ID NTS1: " + stripped + " | no bandcamp found. "
                            )
                            """

                    elif cmd in ["id2", "idch2", "idnts2", "nts2"]:
                        room.delete_message(message)
                        time, artists, title = acrcloud.get_id_nts_two()
                        tz = pytz.timezone("UTC")
                        naive_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                        utc_time = naive_time.replace(tzinfo=pytz.UTC)
                        london_tz = pytz.timezone("Europe/London")
                        london_time = utc_time.astimezone(london_tz)
                        string_time = str(london_time)
                        splittime = string_time.split(" ")
                        lesstime = splittime[1].split(":")
                        hoursmins = str(lesstime[0]) + ":" + str(lesstime[1])
                        googlequery = artists + " " + title
                        res = search_google.search(googlequery)
                        if res is not None:
                            bc_link = res[0]["link"]
                            print(bc_link)
                            if ("track" or "album") in bc_link:
                                room.message(
                                    "ID NTS2: "
                                    + hoursmins
                                    + " - "
                                    + artists
                                    + " - "
                                    + title
                                    + " | maybe it's: "
                                    + bc_link
                                )
                            else:
                                room.message(
                                    "ID NTS2: "
                                    + hoursmins
                                    + " - "
                                    + artists
                                    + " - "
                                    + title
                                    + " | no bandcamp found. "
                                )
                        else:
                            room.message(
                                "ID NTS2: "
                                + hoursmins
                                + " - "
                                + artists
                                + " - "
                                + title
                                + " | no bandcamp found. "
                            )

                        """
                        trackid_unstripped = get_id_nts.run("2")
                        trackid_split = trackid_unstripped.split("\n")
                        stripped = trackid_unstripped.replace("\n", " - ").replace(
                            "\r", " - "
                        )
                        googlequery = trackid_split[1] + " " + trackid_split[2]
                        res = search_google.search(googlequery)
                        if res is not None:
                            bc_link = res[0]["link"]
                            if ("track" or "album") in bc_link:
                                room.message(
                                    "ID NTS2: " + stripped + " | maybe it's: " + bc_link
                                )
                            else:
                                room.message(
                                    "ID NTS2: " + stripped + " | no bandcamp found. "
                                )
                        else:
                            room.message(
                                "ID NTS2: " + stripped + " | no bandcamp found. "
                            )
                        """

                    elif cmd in ["iddy", "iddoyou"]:
                        room.delete_message(message)
                        tracktime, trackartist, tracktitle = get_id_doyou.get()
                        doyou_id_str = (
                            tracktime + " - " + trackartist + " - " + tracktitle
                        )
                        # print('tracktime ',tracktime)
                        if tracktitle != None:
                            "print we have a tracktitle"
                            googlequery = trackartist + " " + tracktitle
                            res = search_google.search(googlequery)
                            if res is not None:
                                bc_link = res[0]["link"]
                                if ("track" or "album") in bc_link:
                                    room.message(
                                        "ID DoYou: "
                                        + doyou_id_str
                                        + " | maybe it's: "
                                        + bc_link
                                    )
                                else:
                                    print(doyou_id_str)
                                    # room.message( doyou_id_str)
                                    room.message(
                                        "ID DoYou: "
                                        + doyou_id_str
                                        + " | no bandcamp found. "
                                    )
                        else:
                            print("no id from doyou")
                            room.message("ID DoYou: No ID found, sorry")

                    elif cmd in ["bollwerk","radiobollwerk"]:
                        room.delete_message(message)
                        # code if acrcloud is used
                        """
                        time, artists, title = acrcloud.get_id_noods()
                        tz = pytz.timezone("UTC")
                        naive_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                        utc_time = naive_time.replace(tzinfo=pytz.UTC)
                        london_tz = pytz.timezone("Europe/London")
                        london_time = utc_time.astimezone(london_tz)
                        string_time = str(london_time)
                        splittime = string_time.split(" ")
                        lesstime = splittime[1].split(":")
                        hoursmins = str(lesstime[0]) + ":" + str(lesstime[1])
                        """

                        now = datetime.now()
                        hoursmins = now.strftime("%H:%M")

                        api = shazam_api.shazam.ShazamApi(api_key=shazam_api_key)
                        station_query = "noods"

                        msg = ""
                        '''
                        response = urlreq.urlopen(
                            "https://radioactivity.directory/api/"
                        )

                        if response.code != 200:
                            room.message("RAID Error: " + str(response.code))
                        else:
                            html = response.read().decode("ISO-8859-1")
                            ra_stations = json.loads(
                                re.split("<[/]{0,1}script.*?>", html)[1]
                            )
                            ra_station_names = list(ra_stations.keys())
                            if station_query in ra_station_names:
                                station_name = station_query
                            else:
                                station_name = [
                                    station
                                    for station in ra_station_names
                                    if station_query in station
                                ]
                                if isinstance(station_name, list):
                                    station_name = station_name[0]

                            id_station = ra_stations[station_name]

                            for stream in id_station["stream_url"]:
                                stream_name = stream[0]
                                if stream_name == "station":
                                    stream_name = ""
                                stream_url = stream[1]
                        '''
                        try:
                            shazam_result = api.detect(
                                "https://radiobollwerk.out.airtime.pro/radiobollwerk_a", rec_seconds=4
                            )
                            result_dict = json.loads(shazam_result.content)
                            artists = result_dict["track"]["subtitle"]
                            title = result_dict["track"]["title"]
                        except Exception as e:
                            LOGGER.error(e)
                            artists = ""
                            title = ""

                        print("are we even getting this far?")
                        print(artists)
                        print(title)
                        print((artists and title) is not None)
                        if artists and title:
                            LOGGER.error("artist and title exist")
                            print("artist and title exist:" + artists + " " + title)

                            googlequery = artists + " " + title
                            res = search_google.search(googlequery)
                            print(res)
                            if res is not None:
                                bc_link = res[0]["link"]
                                print(bc_link)
                                if ("track" or "album") in bc_link:
                                    room.message(
                                        "ID Radio Bollwerk: "
                                        + hoursmins
                                        + " - "
                                        + artists
                                        + " - "
                                        + title
                                        + " | maybe it's: "
                                        + bc_link
                                    )
                                else:
                                    room.message(
                                        "ID Radio Bollwerk: "
                                        + hoursmins
                                        + " - "
                                        + artists
                                        + " - "
                                        + title
                                        + " | no bandcamp found. "
                                    )
                            else:
                                room.message(
                                    "ID Radio Bollwerk: "
                                    + hoursmins
                                    + " - "
                                    + artists
                                    + " - "
                                    + title
                                    + " | no bandcamp found. "
                                )
                        else:
                            LOGGER.error("artist and title dont even exist")
                            print("artist and title not found")
                            room.message(
                                "ID Radio Bollwerk: " + hoursmins + " | sorry, found nothing. "
                            )

                    elif cmd in ["idnoods"]:
                        room.delete_message(message)
                        # code if acrcloud is used
                        """
                        time, artists, title = acrcloud.get_id_noods()
                        tz = pytz.timezone("UTC")
                        naive_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                        utc_time = naive_time.replace(tzinfo=pytz.UTC)
                        london_tz = pytz.timezone("Europe/London")
                        london_time = utc_time.astimezone(london_tz)
                        string_time = str(london_time)
                        splittime = string_time.split(" ")
                        lesstime = splittime[1].split(":")
                        hoursmins = str(lesstime[0]) + ":" + str(lesstime[1])
                        """

                        now = datetime.now()
                        hoursmins = now.strftime("%H:%M")

                        api = shazam_api.shazam.ShazamApi(api_key=shazam_api_key)
                        station_query = "noods"

                        msg = ""

                        response = urlreq.urlopen(
                            "https://radioactivity.directory/api/"
                        )

                        if response.code != 200:
                            room.message("RAID Error: " + str(response.code))
                        else:
                            html = response.read().decode("ISO-8859-1")
                            ra_stations = json.loads(
                                re.split("<[/]{0,1}script.*?>", html)[1]
                            )
                            ra_station_names = list(ra_stations.keys())
                            if station_query in ra_station_names:
                                station_name = station_query
                            else:
                                station_name = [
                                    station
                                    for station in ra_station_names
                                    if station_query in station
                                ]
                                if isinstance(station_name, list):
                                    station_name = station_name[0]

                            id_station = ra_stations[station_name]

                            for stream in id_station["stream_url"]:
                                stream_name = stream[0]
                                if stream_name == "station":
                                    stream_name = ""
                                stream_url = stream[1]

                                try:
                                    shazam_result = api.detect(
                                        stream_url, rec_seconds=4
                                    )
                                    result_dict = json.loads(shazam_result.content)
                                    artists = result_dict["track"]["subtitle"]
                                    title = result_dict["track"]["title"]
                                except Exception as e:
                                    LOGGER.error(e)
                                    artists = ""
                                    title = ""

                        print("are we even getting this far?")
                        print(artists)
                        print(title)
                        print((artists and title) is not None)
                        if artists and title:
                            LOGGER.error("artist and title exist")
                            print("artist and title exist:" + artists + " " + title)

                            googlequery = artists + " " + title
                            res = search_google.search(googlequery)
                            print(res)
                            if res is not None:
                                bc_link = res[0]["link"]
                                print(bc_link)
                                if ("track" or "album") in bc_link:
                                    room.message(
                                        "ID Noods: "
                                        + hoursmins
                                        + " - "
                                        + artists
                                        + " - "
                                        + title
                                        + " | maybe it's: "
                                        + bc_link
                                    )
                                else:
                                    room.message(
                                        "ID Noods: "
                                        + hoursmins
                                        + " - "
                                        + artists
                                        + " - "
                                        + title
                                        + " | no bandcamp found. "
                                    )
                            else:
                                room.message(
                                    "ID Noods: "
                                    + hoursmins
                                    + " - "
                                    + artists
                                    + " - "
                                    + title
                                    + " | no bandcamp found. "
                                )
                        else:
                            LOGGER.error("artist and title dont even exist")
                            print("artist and title not found")
                            room.message(
                                "ID Noods: " + hoursmins + " | sorry, found nothing. "
                            )

                    elif cmd in ["idpalanga"]:
                        room.delete_message(message)

                        # code for recognition via acrccloud
                        """
                        print("palanga")
                        time, artists, title = acrcloud.get_id_palanga()
                        print(time, artists, title)
                        tz = pytz.timezone("UTC")
                        naive_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                        utc_time = naive_time.replace(tzinfo=pytz.UTC)
                        london_tz = pytz.timezone("Europe/London")
                        london_time = utc_time.astimezone(london_tz)
                        string_time = str(london_time)
                        lesstime = string_time.split(" ")[1].split(":")
                        hoursmins = str(lesstime[0]) + ":" + str(lesstime[1])
                        print(hoursmins)
                        """
                        now = datetime.now()
                        hoursmins = now.strftime("%H:%M")

                        api = shazam_api.shazam.ShazamApi(api_key=shazam_api_key)
                        station_query = "palanga"

                        msg = ""

                        response = urlreq.urlopen(
                            "https://radioactivity.directory/api/"
                        )

                        if response.code != 200:
                            room.message("RAID Error: " + str(response.code))
                        else:
                            html = response.read().decode("ISO-8859-1")
                            ra_stations = json.loads(
                                re.split("<[/]{0,1}script.*?>", html)[1]
                            )
                            ra_station_names = list(ra_stations.keys())
                            if station_query in ra_station_names:
                                station_name = station_query
                            else:
                                station_name = [
                                    station
                                    for station in ra_station_names
                                    if station_query in station
                                ]
                                if isinstance(station_name, list):
                                    station_name = station_name[0]

                            id_station = ra_stations[station_name]

                            for stream in id_station["stream_url"]:
                                stream_name = stream[0]
                                if stream_name == "station":
                                    stream_name = ""
                                stream_url = stream[1]

                                try:
                                    shazam_result = api.detect(
                                        stream_url, rec_seconds=4
                                    )
                                    result_dict = json.loads(shazam_result.content)
                                    artists = result_dict["track"]["subtitle"]
                                    title = result_dict["track"]["title"]
                                except Exception as e:
                                    LOGGER.error(e)
                                    artists = ""
                                    title = ""

                        if artists and title:

                            googlequery = artists + " " + title
                            res = search_google.search(googlequery)
                            print(res)
                            if res is not None:
                                bc_link = res[0]["link"]
                                print(bc_link)
                                if ("track" or "album") in bc_link:
                                    room.message(
                                        "ID Palanga: "
                                        + hoursmins
                                        + " - "
                                        + artists
                                        + " - "
                                        + title
                                        + " | maybe it's: "
                                        + bc_link
                                    )
                                else:
                                    room.message(
                                        "ID Palanga: "
                                        + hoursmins
                                        + " - "
                                        + artists
                                        + " - "
                                        + title
                                        + " | no bandcamp found. "
                                    )
                            else:
                                room.message(
                                    "ID Palanga: "
                                    + hoursmins
                                    + " - "
                                    + artists
                                    + " - "
                                    + title
                                    + " | no bandcamp found. "
                                )
                        else:
                            room.message(
                                "ID Palanga: " + hoursmins + " | sorry, found nothing. "
                            )

                    elif cmd.startswith("id") or cmd.startswith("raid"):
                        room.delete_message(message)
                        api = shazam_api.shazam.ShazamApi(api_key=shazam_api_key)
                        station_query = cmd.replace("ra", "", count=1).strip()
                        station_query = station_query.replace("id", "", count=1).strip()
                        msg = ""

                        response = urlreq.urlopen(
                            "https://radioactivity.directory/api/"
                        )

                        if response.code != 200:
                            room.message("RAID Error: " + str(response.code))
                        else:
                            html = response.read().decode("ISO-8859-1")

                            ra_stations = json.loads(
                                re.split("<[/]{0,1}script.*?>", html)[1]
                            )

                            ra_station_names = list(ra_stations.keys())

                            # if idlist was requested return list of possible ids to user via private message
                            if station_query == "list":
                            # if the provided station name is in the list of stations
                                self.pm.message(user, "Possible ID stations: !id + " + str(ra_station_names))
                            elif station_query in ra_station_names:
                                station_name = station_query
                            # try to guess which station is meant
                            else:
                                station_name = [
                                    station
                                    for station in ra_station_names
                                    if station_query in station
                                ]

                                # if two station have the same distance, choose the first one
                                if isinstance(station_name, list):
                                    station_name = station_name[0]

                            if station_query != "list":

                                id_station = ra_stations[station_name]

                                # for all stations urls for the given station, run the shazam api and append results to the message
                                for stream in id_station["stream_url"]:
                                    stream_name = stream[0]
                                    if stream_name == "station":
                                        stream_name = ""
                                    stream_url = stream[1]

                                    # shazam it
                                    try:
                                        shazam_result = api.detect(
                                            stream_url, rec_seconds=4
                                        )
                                        result_dict = json.loads(shazam_result.content)
                                        msg = (
                                            "ID "
                                            + station_name
                                            + " "
                                            + stream_name
                                            + ": "
                                            + result_dict["track"]["subtitle"]
                                            + " - "
                                            + result_dict["track"]["title"]
                                            + "\n"
                                        )
                                        room.message(msg)
                                    except Exception as e:
                                        msg = (
                                            "ID "
                                            + station_name
                                            + " "
                                            + stream_name
                                            + ": sorry, found nothing. "
                                        )
                                        LOGGER.error(e)
                                        room.message(msg)

                    elif cmd in ["bbb", "bigb", "gift"]:
                        room.delete_message(message)
                        gifone = random.choice(db.fetch_gif("bbb"))
                        room.message(gifone + " " + gifone + " " + gifone)

                    elif cmd in ["gif"]:
                        room.delete_message(message)
                        # gifone = random.choice(d["dance"])
                        gifone = random.choice(db.fetch_gif("dance"))
                        room.message(gifone)

                    elif cmd == "b2b":
                        room.delete_message(message)
                        gifone = random.choice(db.fetch_gif("bbb"))
                        giftwo = random.choice(db.fetch_gif("bbb"))
                        room.message(gifone + " " + giftwo + " " + gifone)

                    elif cmd in ["b2b2b", "bbbb", "b3b"]:
                        room.delete_message(message)
                        gifone = random.choice(db.fetch_gif("bbb"))
                        giftwo = random.choice(db.fetch_gif("bbb"))
                        gifthree = random.choice(db.fetch_gif("bbb"))
                        room.message(gifone + " " + giftwo + " " + gifthree)

                    # get a recent tweet from the ntsweirdo twitter account
                    elif cmd in ["ntsweirdo"]:
                        room.delete_message(message)
                        weird_tweet = ntsweirdo.get_random_tweet()
                        room.message("anon1111: " + weird_tweet)

                    ##Say
                    # Make your bot say what you want
                    elif cmd == "say":
                        room.delete_message(message)
                        room.message(args)
                    elif cmd == "bg":
                        room.delete_message(message)
                        if args:
                            print(args)
                            print(".......")
                            splitargs = args.split(" ")
                            for arg in splitargs:
                                if arg.startswith("@"):
                                    print(arg)
                                    room.message("You are a bg, " + (arg) + "!")

                    elif cmd == "kiss":
                        room.delete_message(message)
                        if args:
                            print(args)
                            print(".......")
                            splitargs = args.split(" ")
                            for arg in splitargs:
                                if arg.startswith("@"):
                                    print(arg)
                                    room.message("😘 " + (arg))
                        else:
                            room.message("😘 " + ("@" + user.name))

                    elif cmd == "chunt":
                        room.delete_message(message)
                        room.message("I'm chuntin")

                    elif cmd in ["heart", "hearts"]:
                        room.delete_message(message)
                        a = random.randint(1, 10)
                        heart = ""
                        for i in range(0, a):
                            heart = heart + "*h* "

                        room.message(heart)

                    elif cmd in ["scran", "recipe", "food", "hungry"]:
                        room.delete_message(message)
                        if args:
                            q = args
                        else:
                            q = "vegetarian"
                        title, url = edamam.scran(q)
                        room.message("hungry? how about: " + title + " | " + url)

                    ##List Mods
                    # List of Mods and Owner name in the current room you're in
                    # elif cmd == "mods":
                    #    room.delete_message(message)
                    #    room.message(", ".join(room.modnames + [room.ownername]))

                    elif cmd in ["shoutout", "shout", "out"]:
                        room.delete_message(message)
                        if args:
                            # print(args)
                            # print('.......')
                            splitargs = args.split(" ")
                            if args.startswith("@"):
                                for arg in splitargs:
                                    print("arg ", arg)
                                    if arg.startswith("@"):
                                        room.message(
                                            random.choice(shoutstart)
                                            + " "
                                            + (arg)
                                            + " ! "
                                            + random.choice(shoutend)
                                        )

                            else:
                                room.message(
                                    random.choice(shoutstart)
                                    + " "
                                    + (args)
                                    + " ! "
                                    + random.choice(shoutend)
                                )

                        else:
                            room.message(
                                random.choice(shoutstart)
                                + " "
                                + random.choice(room.usernames)
                                + "! "
                                + random.choice(shoutend)
                            )

                    else:
                        try:
                            gifres = db.fetch_gif(cmd)
                        except Exception as e:
                            print(e)
                        if gifres:
                            room.delete_message(message)
                            print(gifres)
                            room.message(random.choice(gifres))
                        else:
                            print("no result for gif search")

            else:
                # very crude way to catch posted gifs and add them to allgif_set and allgif_file
                splitmsg = message.body.split(" ")
                for word in splitmsg:
                    if (word.endswith(".gif") or word.endswith(".gifv")) and (
                        len(word) < 75
                    ):
                        print("might be gif")
                        if word in allgif_set:
                            pass

                        else:
                            print("not in set")
                            allgif_set.add(word)
                            with open(allgif_file, "a") as file:
                                file.write(word + "\n")

        except Exception as e:
            try:
                et, ev, tb = sys.exc_info()
                lineno = tb.tb_lineno
                fn = tb.tb_frame.f_code.co_filename
                """room.message(
                    "[Expectation Failed] %s Line %i - %s" % (fn, lineno, str(e))
                )"""
                return
            except:
                """
                room.message("Undescribeable error detected !!")
                """
                return

    def on_flood_warning(self, room):
        print("received Floodwarning!")
        time.sleep(5)
        room.reconnect()

    # apparently pm. is the wrong object, triggers 2 times but crashes 2nd time because it's "None". where is right pm.?
    """
    def onPMMessage(self, pm, user, body):
        print("PM recvd")
        print('pm obj',pm)
        print('user obj',user)
        print('print body',body)
        #pm.message(user,"hello")
        #print(body)

        if body is not None:
            print('body is not none')
            type(body)
            print(body)
            if body[0] is not None:
                print('body0 is not none')
            if body[0] == "!":  ##Here is the Prefix part
                data = body[1:].split(" ", 1)
                if len(data) > 1:
                    cmd, args = data[0], data[1]
                else:
                    cmd, args = data[0], ""

                ##COMMANDS!
                # Setting up commands for your bot

                ##Eval
                ##You may want/need to evaluate something about your bot.
                if cmd == "ev" or cmd == "eval" or cmd == "e":
                    ret = eval(args)
                    if ret == None:
                        self.pm.message("Done.")
                        return
                    self.pm.message(str(ret))
                    
                elif cmd == "help":
                    print(helpmessage)
                    self.pm.message(user,helpmessage)

                elif cmd in ["b2b2b","bbbb"]:
                        gifone = random.choice(tuple(allgif_set))
                        giftwo = random.choice(tuple(allgif_set))
                        gifthree = random.choice(tuple(allgif_set))

                        self.pm.message(user,gifone + " " + giftwo + " " + gifthree)

                else:
                        if cmd in d:
                            self.pm.message(user,random.choice(d[cmd]))
            else:
                pass
                """

    def onJoin(self, room, user):
        print(user.name + " joined the chat!")

    def onLeave(self, room, user):
        print(user.name + " left the chat!")

    def onUserCountChange(self, room):
        print("users: " + str(room.usercount))

    def onMessageDelete(self, room, user, msg):
        print("MESSAGE DELETED: " + user.name + ": " + msg.body)


if __name__ == "__main__":
    WomBot.easy_start(rooms=myrooms, name=chatango_user, password=chatango_pass)
