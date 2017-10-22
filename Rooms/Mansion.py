from SpeechOutputHelper import *

object_dict = {
    "Bookshelf": "BkShelf",
    "Fireplace": "FrPlc",
    "": ""
}


def get_object_name(room_name):
    return object_dict.get(room_name, "unkn")

def StartMansion(event, context):

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])

    return

def on_launch(launch_request, session):
    return get_welcome_response()

def get_welcome_response():
    session_attributes = {}

    card_title = "Mansion Room"
    speech_output = "Welcome to the Mansion. " \
                    "You are trapped, you must escape!" \
                    "Look around you, you are in a giant study. Your friends stand close by in confusion, wondering how they got here." \
                    "In front of you is a brick stucco wood burning fireplace. On the mantel of the fire hangs the head of a Lion." \
                    "Below you is a velvet rug. To your starboard is davenport desk oh the surface rests a book a quill and a bottle of ink." \
                    "To your port sits a book shelf against the wall brimming with knowledge. The walls you can see adorn two paintings depicting scenes of war and bloodshed."\
                    "From what you can see there are no doors. How will you escape?"
    reprompt_text = "What is you next bet?"

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "ExamineObject":
        return ExamineObject(intent)
    elif intent_name == "OrientView":
        return OrientView(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def OrientView(intent):
    return

def ExamineObject(intent):
    return