import time
import threading
from SpeechOutputHelper import *

def tenMinuteTimer():

    mins = 0
    while mins != 10:
        print ">>>>>>>>>>>>>>>>>>>>>", mins
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1
    raise TimeComplete

class TimeComplete (Exception):
    pass

def StartAsylum():

    session_attributes = {}
    card_title = "Escape Room"

    try:
        timerThread = threading.Thread(target=tenMinuteTimer())
        timerThread.start()

        AsylumBuildRoom()

    except TimeComplete:

        speech_output = "The killer has entered the room, you have no escape!" \
                        "Please try again!"
        reprompt_text = "Please select a valid room"
        should_end_session = False

        return build_response(session_attributes, build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))


def AsylumBuildRoom():
    session_attributes = {}
    card_title = "Escape Room"
    speech_output = "The"

    reprompt_text = "Please select a valid room"
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session)) 