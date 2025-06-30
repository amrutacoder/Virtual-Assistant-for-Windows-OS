from types import coroutine
import pyttsx3
import speech_recognition as sr
from Features1 import GoogleSearch
from win10toast import ToastNotifier
import datetime
import pyaudio
import webbrowser  # Additional


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print("Waiting ")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon!")

    else:
        Speak("Good Evening!")


Speak("Hello sir")


def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print(": Recognizing...")

        query = r.recognize_google(audio, language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()


if __name__ == '__main__':
    wishMe()


def TaskExe():

    while True:

        query = TakeCommand()

        if 'google search' in query:
            GoogleSearch(query)

        elif 'youtube search' in query:
            url = "https://www.youtube.com"
            Query = query.replace("jarvis", "")
            url = Query.replace("youtube search", "")
            from Features1 import YouTubeSearch
            YouTubeSearch(url)  # Additional
            # webbrowser.open_new_tab(url)

        elif 'set alarm' in query:
            from Features1 import Alarm
            Alarm(query)

        elif 'download' in query:
            from Features1 import DownloadYouTube
            DownloadYouTube()

        elif 'speed test' in query:
            from Features1 import SpeedTest
            SpeedTest()

        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message", "")
            name = name.replace("send ", "")
            name = name.replace("to ", "")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations1 import WhatsappMsg
            WhatsappMsg(Name, MSG)

        elif 'call' in query:
            from Automations1 import WhatsappCall
            name = query.replace("call ", "")
            name = name.replace("jarvis ", "")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automations1 import WhatsappChat
            WhatsappChat(name)

        elif 'my location' in query:

            from Features1 import My_Location

            My_Location()

        else:

            from DataBase.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            Speak(reply)

            if 'bye' in query:

                break

            elif 'exit' in query:

                break

            elif 'go' in query:

                break
