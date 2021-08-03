import speech_recognition as sr
import wolframalpha
import wikipedia
import time


app_id = "UVV4RK-5QA95K34VR"
wolf_client = wolframalpha.Client(app_id)


def get_info(request):
    """Passed a string, returns the result of an answer from either Wolfram Alpha or Wikipedia"""
    try:
        wolfram_req = wolf_client.query(request)
        answer = next(wolfram_req.results).text
    except:
        answer = wikipedia.summary(request)

    print("\n" + answer + "\n")


def recognise_speech():
    """Takes input from the microphone, displays appropriate error messages accordingly, returns text spoken."""

    print("Ask a question...")
    # obtain audio from the microphone
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recogniser.listen(source)

    try:
        return recogniser.recognize_google(audio)
    except sr.UnknownValueError:
        print("Audio could not be recognised.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    time.sleep(5)


while True:
    get_info(recognise_speech())