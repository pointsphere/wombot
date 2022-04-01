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
#from gif_sort import dance
import secrets
import fortunes
import json
from os import environ
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

myrooms = []
myrooms.append(environ['wombotmainroom'])
myrooms.append(environ['wombottestroom'])

commandlist = ["help","fortune","id1","id2",
                "iddy","ev","eval","e","bbb", 
                "gif", "gift", "bigb","b2b2b"
                "say","kiss","shoutout","chunt","mods","tag","g"]

helpmessage = "your friendly spambot \r here to spam gifs and give trackids \r\r" + \
                "commands: \r \r!id1 for NTS1 \r!id2 for NTS2 \r!iddy for DoYouWorld \r \r " + \
                "GIFs: \r!gif for random dance gif \r!gift or !bigb for gifs from bigbunnybrer's collection \r" + \
                "!b2b back2back of bigbunnybrer gifs \r \r " + \
                "also: !bbbb !fortune !tags  \r \r " + \
                "gifs stolen from oscmal, bigbunnybrer and every poster in this channel \r\r keep chunting"

shoutstart = [
    "out to you, ",
    "out to the absolute legend ",
    "much love out to ",
    "out to the amazing ",
    "out to the unimitable",
    ]

shoutend = ["😘", "❤️", "💙"]

gifhosts = ["https://c.tenor.com/","https://media.giphy.com/"]

basepath = Path().absolute()
bbb_file = os.path.join(basepath, "bbb.txt")
with open(bbb_file) as file:
    bbb_set = set(line.strip() for line in file)

allgif_file = os.path.join(basepath, "allgif.txt")
if not os.path.exists(allgif_file):
    with open(allgif_file,'a') as file:
        pass
else:
    with open(allgif_file) as file:
        allgif_set = set(line.strip() for line in file)

d = defaultdict(list)
d_json_file = os.path.join(basepath, "gif_tagged.json")
if not os.path.exists(d_json_file):
    with open(d_json_file,"w") as f:
        pass
    
else:
    with open(d_json_file) as f:
        d_str = json.loads(f.read())


for k in d_str:
    for value in d_str[k]:
        d[k].append(value)


print(d)

##Dance moves!
# kinda useless

# dancemoves = ["(>^.^)>", "(v^.^)v", "v(^.^v)", "<(^.^<)"]

##Setting Pretty Colors
# Font setting for your bot


class WomBot(ch.RoomManager):
    def onInit(self):
        self.setNameColor("255")
        self.setFontColor("F33")
        self.setFontFace("0")
        self.setFontSize(10)
        self.enableBg()
        self.enableRecording()

    ##Connecting
    # This is what will be printed on your python console when event called

    def onConnect(self, room):
        print("Connected")

    def onReconnect(self, room):
        print("Reconnected")

    def onDisconnect(self, room):
        print("Disconnected")

    def onMessage(self, room, user, message):
        try:
            if room.getLevel(self.user) > 0:
                print(user.name, message.body)
            else:
                print(user.name, message.body)
            if self.user == user:
                return

            
            if message.body[0] == "!":  ##Here is the Prefix part
                data = message.body[1:].split(" ", 1)
                if len(data) > 1:
                    cmd, args = data[0], data[1]
                else:
                    cmd, args = data[0], ""

                ##COMMANDS!
                # Setting up commands for your bot

                ##Eval
                ##You may want/need to evaluate something about your bot.
                '''
                if cmd == "ev" or cmd == "eval" or cmd == "e":
                    room.delete(message)
                    ret = eval(args)
                    if ret == None:
                        room.message("Done.")
                        return
                    room.message(str(ret))
                    '''
                    
                if cmd == "help":
                    print(helpmessage)
                    room.delete(message)
                    self.pm.message(user,helpmessage)

                elif cmd == "fortune":
                    room.delete(message)
                    room.message("your fortune, " + user.name + " : " + (random.choice(fortunes.fortunecookie)).replace(".","").lower())

                elif cmd == "tags":
                    room.delete(message)
                    dict_keys = d.keys()
                    taglist = []
                    for key in dict_keys:
                        #print(key)
                        taglist.append(key)
                    thelongeststring = 'to tag a gif: !tag link-to-the-gif tagname \r'
                    for key in taglist:
                        thelongeststring +=  "!" + key + " "
                    print(thelongeststring)
                        
                    self.pm.message(user,str(thelongeststring))

                elif cmd == "id1":
                    room.delete(message)
                    trackid_unstripped = get_id_nts.run("1")
                    trackid_split = trackid_unstripped.split("\n")
                    stripped = trackid_unstripped.replace("\n", " - ").replace(
                        "\r", " - "
                    )
                    googlequery = trackid_split[1] + " " + trackid_split[2]
                    res = search_google.search(googlequery)
                    if res is not None:
                        bc_link = res[0]["link"]
                        room.message("ID1: " + stripped + " | maybe it's: " + bc_link)
                    else:
                        room.message("ID1: " + stripped + " | no bandcamp found. ")

                elif cmd == "id2":
                    room.delete(message)
                    trackid_unstripped = get_id_nts.run("2")
                    trackid_split = trackid_unstripped.split("\n")
                    stripped = trackid_unstripped.replace("\n", " - ").replace(
                        "\r", " - "
                    )
                    googlequery = trackid_split[1] + " " + trackid_split[2]
                    res = search_google.search(googlequery)
                    if res is not None:
                        bc_link = res[0]["link"]
                        room.message("ID2: " + stripped + " | maybe it's: " + bc_link)
                    else:
                        room.message("ID2: " + stripped + " | no bandcamp found. ")

                elif cmd == "iddy":
                    room.delete(message)
                    doyou_id_str = get_id_doyou.get()
                    #print(doyou_id_str)
                    #room.message( doyou_id_str)
                    room.message("ID DoYou " + doyou_id_str)

                elif cmd in ["bbb", "bigb","gift"]:
                    room.delete(message)
                    gifone = random.choice(tuple(bbb_set))
                    room.message(gifone + " " + gifone + " " + gifone)

                elif cmd in ["gif"]:
                    room.delete(message)
                    gifone = random.choice(d["dance"])
                    room.message(gifone + " " + gifone + " " + gifone)

                elif cmd == "b2b":
                    room.delete(message)
                    gifone = random.choice(tuple(bbb_set))
                    giftwo = random.choice(tuple(bbb_set))

                    room.message(gifone + " " + giftwo + " " + gifone)

                elif cmd in ["b2b2b","bbbb"]:
                    room.delete(message)
                    gifone = random.choice(tuple(bbb_set))
                    giftwo = random.choice(tuple(bbb_set))
                    gifthree = random.choice(tuple(bbb_set))

                    room.message(gifone + " " + giftwo + " " + gifthree)

                ##Say
                # Make your bot say what you want
                elif cmd == "say":
                    room.delete(message)
                    room.message(args)

                elif cmd == "kiss":
                    room.delete(message)
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
                    room.delete(message)
                    room.message("I'm chuntin")

                ##List Mods
                # List of Mods and Owner name in the current room you're in
                elif cmd == "mods":
                    room.delete(message)
                    room.message(", ".join(room.modnames + [room.ownername]))

                
                elif cmd == "shoutout":
                    room.delete(message)
                    if args:
                        # print(args)
                        # print('.......')
                        splitargs = args.split(" ")
                        # for arg in splitargs:
                        # if arg.startswith('@'):
                        # print(arg)
                        room.message(
                            random.choice(shoutstart)
                            + " "
                            + (splitargs[0])
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


                elif cmd == "tag":
                    room.delete(message)
                    splitmsg = message.body.split(" ")
                    if len(splitmsg) > 2:
                        maybegif = splitmsg[1]
                        maybekey = splitmsg[2]
                        if (maybegif.startswith("http") and maybegif.endswith(".gif")):
                            print("might be gif")
                            if maybegif in allgif_set:
                                pass

                            else:
                                print('not in set')
                                allgif_set.add(maybegif)
                                with open(allgif_file,'a') as file:
                                    file.write(maybegif + "\n")

                            if len(maybekey)<20:
                                print(maybekey)
                                if maybekey not in commandlist:
                                    if maybekey in d:
                                        d[maybekey].append(maybegif)
                                    else:
                                        d[maybekey] = []
                                        d[maybekey].append(maybegif)

                                    with open(d_json_file, 'w') as fp:
                                        json.dump(d, fp)

                else:
                    if cmd in d:
                        room.delete(message)
                        room.message(random.choice(d[cmd]))



            else:
                # very crude way to catch posted gifs and add them to allgif_set and allgif_file
                splitmsg = message.body.split(" ")
                for word in splitmsg:
                    if (any(word.startswith(host) for host in gifhosts) and word.endswith(".gif") and (len(word)<75)):
                        print("might be gif")
                        if word in allgif_set:
                            pass

                        else:
                            print('not in set')
                            allgif_set.add(word)
                            with open(allgif_file,'a') as file:
                                file.write(word + "\n")
                                



        except Exception as e:
            try:
                et, ev, tb = sys.exc_info()
                lineno = tb.tb_lineno
                fn = tb.tb_frame.f_code.co_filename
                room.message(
                    "[Expectation Failed] %s Line %i - %s" % (fn, lineno, str(e))
                )
                return
            except:
                room.message("Undescribeable error detected !!")
                return

    def onFloodWarning(self, room):
        print("received Floodwarning!")
        time.sleep(5)
        room.reconnect()
    '''
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
                '''

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
