import os, json
import requests


def notification(message):
    # try:
    print("notification(message) 1")
    message = json.loads(message)
    mp3_fid = message["mp3_fid"]
    receiver_address = message["username"]
    print('sent #########', mp3_fid, message)


    #return requests.post(
    #"https://api.mailgun.net/v3/sandbox<var>.mailgun.org/messages",
    #auth=("api", "<key>"),
    #data={"from": "Backups Mac <postmaster@sandbox<var>.mailgun.org>",
    #      "to": "r.buzatu90@gmail.com",
    #      "subject": "Hello",
    #      "text": "Tdsa {mp3_fid}"})


