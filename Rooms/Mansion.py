from SpeechOutputHelper import *

object_dict = {
    "Bookshelf": "BkShelf",
    "Fireplace": "FrPlc",
    "Desk":"Desk",
    "Left Painting" : "LftPtn",
    "Right Painting" : "RtPtn",
    "Lion Head" : "LnHd",
    "Firewood" : "FireWood",
    " ":" "
}


def get_object_name(object_name):
    return object_dict.get(object_name, "unkn")

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
                    "You are trapped, you must escape." \
                    "Look around you, you are in a giant study. Your friends stand close by in confusion, wondering how they got here." \
                    "In front of you is a brick stucco wood burning fireplace. On the mantel of the fire hangs the head of a Lion." \
                    "Below you is a velvet rug. To your starboard is davenport desk oh the surface rests a book a quill and a bottle of ink." \
                    "To your port sits a book shelf against the wall brimming with knowledge. The walls you can see adorn two paintings, one on" \
                    "the left wall of the fireplace and one on the right, depicting scenes of war and bloodshed." \
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

    session_attributes = {}
    card_title = "Escape Room"
    speech_output = "I'm not sure what direction you would like to look. " \
                    "Please try again."
    reprompt_text = "I'm not sure what direction that is."

    should_end_session = False

    if "Direction" in intent["slots"]:
        view_name = intent["slots"]["Direction"]["value"]
        view_code = get_view_name(view_name.lower())
        if (view_code != "unkn"):
            reprompt_text = ""
            if (view_code == "above" |  view_code == "up"):
                speech_output = ""
            else:
                speech_output = ""



    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def ExamineObject(intent):
    return