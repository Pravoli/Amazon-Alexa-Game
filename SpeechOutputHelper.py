view_dict = {
    "above": "above",
    "up" : "up",
    "behind": "behind",
    "back" : "back"
}

def get_view_name(view_name):
    return view_dict.get(view_name, "unkn")

def handle_session_end_request():
    card_title = "Escape Room - Thanks"
    speech_output = "Thank you for entering the Escape Room.  See you next time!"
    should_end_session = True

    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))


def on_session_ended(session_ended_request, session):
    print "Ending session."
    # Cleanup goes here...

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
