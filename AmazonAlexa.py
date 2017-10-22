import urllib2
import json
from Rooms import *
import random
from SpeechOutputHelper import *

room_dict = {
    "Mansion": "Mansion",
    "Asylum": "Asylum"
}

def lambda_handler(event, context):
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.45fa333f-e6c8-457c-b471-97ed2458243b"):
        raise ValueError("Invalid Application ID")

    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])

def StartRoom(intent):

    session_attributes = {}
    card_title = "Escape Room"
    speech_output = "I'm not sure what room you are looking for. " \
                    "Please try again."
    reprompt_text = "I'm not sure what room you are looking for. " \
                    "Try asking for Prison or University for example."
    should_end_session = False


    if "Room" in intent["slots"]:
        room_name = intent["slots"]["Room"]["value"]
        room_code = get_room_name(room_name.lower())
        if (room_code != "unkn"):
            room_code = "Start{}()".format(room_code)
            reprompt_text = ""
            eval(room_code)

    else:
        room_code = random.randint(0,len(room_dict))
        room_code = "Start{}()".format(room_dict(room_code))
        reprompt_text = ""
        eval(room_code)

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def on_session_started(session_started_request, session):
    print "Starting new session."


def on_launch(launch_request, session):
    return get_welcome_response()


def get_welcome_response():
    session_attributes = {}

    card_title = "Escape Room"
    speech_output = "Welcome to the Alexa Escape Room. " \
                    "Which room would you like to enter?"\
                    "The Mansion, Prison, Asylum, University, or Crypt"
    reprompt_text = "Please select a valid room"

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "EnterEscapeRoom":
        return StartRoom(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def get_room_name(room_name):
    return room_dict.get(room_name, "unkn")




