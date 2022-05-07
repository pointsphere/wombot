import sys
import shazam_api.shazam_api.shazam
import re
import json

if sys.version_info[0] > 2:
    import urllib.request as urlreq
else:
    import urllib2 as urlreq
import secrets

shazam_api_key = secrets.shazam_api_key
import logging as LOGGER


api = shazam_api.shazam_api.shazam.ShazamApi(api_key=shazam_api_key)
# station_query = cmd.replace('raid', '').strip()
station_query = "palanga"
LOGGER.error(station_query)
msg = ""

response = urlreq.urlopen("https://radioactivity.directory/api/")

if response.code != 200:
    room.message("RAID Error: " + str(response.code))
else:
    html = response.read().decode("ISO-8859-1")

    ra_stations = json.loads(re.split("<[/]{0,1}script.*?>", html)[1])

    ra_station_names = list(ra_stations.keys())
    print(ra_station_names)
    # if the provided station name is in the list of stations
    if station_query in ra_station_names:
        station_name = station_query
    # try to guess which station is meant
    else:
        station_name = [
            station for station in ra_station_names if station_query in station
        ]

        # if two station have the same distance, choose the first one
        if station_name:
            print(station_name)
        if isinstance(station_name, list):
            print(station_name)
            station_name = station_name[0]

    id_station = ra_stations[station_name]

    # for all stations urls for the given station, run the shazam api and append results to the message
    for stream in id_station["stream_url"]:
        stream_name = stream[0]
        if stream_name == "station":
            stream_name = ""
        stream_url = stream[1]

        # shazam it
        try:
            shazam_result = api.detect(stream_url, rec_seconds=4)
            print(shazam_result)
            result_dict = json.loads(shazam_result.content)
            print(result_dict)
            msg += (
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
        except Exception as e:
            msg += (
                "ID "
                + station_name
                + " "
                + stream_name
                + ": Track could not be identified "
                + str(e)
                + "\n"
            )
    print(msg)
    # room.message(msg)
