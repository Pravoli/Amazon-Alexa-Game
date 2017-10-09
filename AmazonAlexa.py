import urllib2
import json
from Rooms import *

def lambda_handler(event, context):
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.45fa333f-e6c8-457c-b471-97ed2458243b"):
        raise ValueError("Invalid Application ID")

    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])

def on_launch(launch_request, session):
    return get_welcome_response()

def get_welcome_response():
    session_attributes = {}
    card_title = "BART"
    speech_output = "Welcome to the Alexa BART times skill. " \
                    "You can ask me for train times from any station, or " \
                    "ask me for system status or elevator status reports."
    reprompt_text = "Please ask me for trains times from a station, " \
                    "for example Fremont."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }


def on_session_started(session_started_request, session):
    print "Starting new session."

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


