import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import random
import pyjokes
from speak_engine import speak, bring_in_bob, bring_in_alice
from open import open
from wiki import wiki
from microphone import takeInput
from weather_api import weather_forcast

link = ""



# speak("Hello, this is just the begining")

hibernate = False

with sr.Microphone() as source:

    def listen():
        while True:
            text = takeInput(source).lower()
            print(text)
            global hibernate
            if "hibernate" in text:
                hibernate = True
                speak("Ok understood, I am hibernating now")
                continue
            if "wake up" in text:
                hibernate = False
                speak("I am awake now, you can ask me anything")
                continue
            if hibernate:
                continue

            if 'wikipedia' in text:
                wiki(text)
            elif 'open' in text:
                open(text)
            elif 'search'  in text:
                text = text.split("search")[1]
                base_url = "https://www.google.com/search?q="
                query = text
                final_url = base_url + query.replace(" ","%20")
                webbrowser.open_new_tab(final_url)
                time.sleep(2)
            elif 'bob' in text:
                bring_in_bob()
                try:
                    text = text.split("bob")[1]
                    app_id = "VKYJYH-YVYV2X93QW"
                    client = wolframalpha.Client('R2K75H-7ELALHR35X')
                    res = client.query(text)
                    answer = next(res.results).text
                    speak(answer)
                    print(answer)
                except:
                    speak("Sorry no idea!")
                bring_in_alice()

            elif "weather" in text:
                weather_forcast(text, source)
            elif 'joke' in text:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)   
            else:
                speak(text)
                
    speak("welcome")
    print("start")
    listen()

