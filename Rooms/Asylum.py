from SpeechOutputHelper import *

#changes per room
object_dict = {
    "Rope":"Rope"
}


def get_object_name(room_name):
    return object_dict.get(room_name, "unkn")

def StartAsylum(event, context):

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

    card_title = "Asylum Room"
    speech_output = "Welcome to the Asylum. " \
                    "You are trapped, you must escape!" \
                    "The dirty stained walls may be grey, but the soul of this asylum is pitch black." \
                    "The woes from the inmates fade into eerie background music as you realize that if you don't move soon" \
                    "you will not live to see the outside of this asylum." \
                    "All of you are in tied with ropes. There is nothing in the room, but you realize the door is unlocked." \
                    "Either you figure out how to leave the room or danger will enter."
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