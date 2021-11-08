import speech_recognition as sr
from search import search_google
from gtts import gTTS
from search import *
from nltk_bot import *
import subprocess
import os

def response_to_voice(response):
    language = 'en'
    myobj = gTTS(text=response, lang=language, slow=False)
    myobj.save("response.mp3")
    return_code = subprocess.call(["afplay", "./response.mp3"])

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) 
        return_code = subprocess.call(["afplay", "./start.wav"])
        audio = recognizer.listen(source)
        return_code = subprocess.call(["afplay", "./welcome.mp3"])

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable/unresponsive"

    return response


if __name__ == "__main__":
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    response = recognize_speech_from_mic(recognizer, mic)
    if(response['success']):
        query = str(response['transcription']).lower()
        print(query)
        addr = search_google(query)
        print(addr)
        response = bot_response(query, addr)
        print(response)
        response_to_voice(response)
    else:
        print('Error: ' + str(response['error']))

