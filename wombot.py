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
import data_pics_wombat
import data_pics_capybara
import data_pics_otter
import data_pics_quokka
import data_txt_fortunes as fortunes
import data_gif_hardcoded
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
                "say","kiss","shoutout","chunt","mods","tag","g","wombat","capybara","otter","quokka"]

helpmessage = "commands: \r \r " + \
                "GIFs: \r!gif (random dance gif) \r!gift / !b2b / !bbb (more gifs) \r" + \
                "!shoutout [user]  \r " + \
                "!fortune (your daily fortune)  \r \r " + \
                "!id1 for NTS1 \r!id2 for NTS2 \r!iddy for DoYouWorld \r \r" + \
                "gifs curated by oscmal, bigbunnybrer and others \r \r" + \
                "keep chuntin!" 

shoutstart = [
    "out to you, ",
    "out to the absolute legend ",
    "much love out to ",
    "out to the amazing ",
    "out to the unimitable",
    ]

shoutend = ["😘", "❤️", "💙","*h*","<3"]

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
print('init variables done')
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
        self.enable_recording()
        print('wombot on_init')

    ##Connecting
    # This is what will be printed on your python console when event called

    def on_connect(self, room):
        print("Connected")

    def on_reconnect(self, room):
        print("Reconnected")

    def on_disconnect(self, room):
        print("Disconnected")
        time.sleep(5)
        room.reconnect()
        

    def on_message(self, room, user, message):
        try:
            if room.get_level(self.user) > 0:
                print(user.name, message.body,room.get_level(user))
            else:
                print(user.name, message.body,room.get_level(user))
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
                '''
                if cmd == "ev" or cmd == "eval" or cmd == "e":
                    room.delete_message(message)
                    ret = eval(args)
                    if ret == None:
                        room.message("Done.")
                        return
                    room.message(str(ret))
                    '''
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
                        self.pm.message(user,helpmessage)

                    elif cmd == "fortune":
                        room.delete_message(message)
                        room.message("your fortune, " + user.name + " : " + (random.choice(fortunes.fortunecookie)).replace(".","").lower())
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
                        room.delete_message(message)
                        room.message(random.choice(data_pics_quokka.pics))

                    elif cmd == "fesh":
                        room.delete_message(message)
                        room.message(data_gif_hardcoded.fesh)

                    elif cmd == "tags":
                        room.delete_message(message)
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

                    elif cmd in ["id1","idch1"]:
                        room.delete_message(message)
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

                    elif cmd in ["id2","idch2"]:
                        room.delete_message(message)
                    
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
                        room.delete_message(message)
                        doyou_id_str = get_id_doyou.get()
                        if doyou_id_str != None:
                            print(doyou_id_str)
                            #room.message( doyou_id_str)
                            room.message("ID DoYou: " + doyou_id_str)
                        else:
                            room.message("ID DoYou: No ID found, sorry")

                    elif cmd in ["bbb", "bigb","gift"]:
                        room.delete_message(message)
                        gifone = random.choice(tuple(bbb_set))
                        room.message(gifone + " " + gifone + " " + gifone)

                    elif cmd in ["gif"]:
                        room.delete_message(message)
                        gifone = random.choice(d["dance"])
                        room.message(gifone)

                    elif cmd == "b2b":
                        room.delete_message(message)
                        gifone = random.choice(tuple(bbb_set))
                        giftwo = random.choice(tuple(bbb_set))

                        room.message(gifone + " " + giftwo + " " + gifone)

                    elif cmd in ["b2b2b","bbbb"]:
                        room.delete_message(message)
                        gifone = random.choice(tuple(bbb_set))
                        giftwo = random.choice(tuple(bbb_set))
                        gifthree = random.choice(tuple(bbb_set))

                        room.message(gifone + " " + giftwo + " " + gifthree)

                    ##Say
                    # Make your bot say what you want
                    elif cmd == "say":
                        room.delete_message(message)
                        room.message(args)

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

                    ##List Mods
                    # List of Mods and Owner name in the current room you're in
                    elif cmd == "mods":
                        room.delete_message(message)
                        room.message(", ".join(room.modnames + [room.ownername]))

                    
                    elif cmd == "shoutout":
                        room.delete_message(message)
                        if args:
                            # print(args)
                            # print('.......')
                            splitargs = args.split(" ")
                            if args.startswith("@"):
                                for arg in splitargs:
                                    print('arg ',arg)
                                    if arg.startswith('@'):
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


                    elif cmd == "tag":
                        room.delete_message(message)
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
                            room.delete_message(message)
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
