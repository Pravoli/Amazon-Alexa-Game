import urllib2
import json
from Rooms import *

def lambda_handler(event, context):
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.45fa333f-e6c8-457c-b471-97ed2458243b"):
        raise ValueError("Invalid Application ID")


def StartRoom(intent):
    if "Room" in intent["slots"]:
        room_name = intent["slots"]["Room"]["value"]
        room_code = get_room_name(room_name.lower())
        if (room_code != "unkn"):
            room_code = "Start{}()".format(room_code)
            eval(room_code)

def get_room_name(room_name):
    return {
        "Mansion": "Mansion",
        "Prison":"Prison",
        "Crypt" :"Crypt",
        "Asylum":"Asylum",
        "University": "Uni"
    }.get(room_name, "unkn")


