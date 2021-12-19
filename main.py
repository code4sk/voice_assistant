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

engine=pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[1].id)

link = ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

# speak("Hello, this is just the begining")


with sr.Microphone() as source:
    def takeInput():
        while True:
            try:
                r = sr.Recognizer()
                # r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                command = r.recognize_google(audio, language='en-in')
                return command
            except Exception as e:
                # print("hello")
                continue
        return "null"


    def listen():
        while True:
            text = takeInput().lower()
            print(text)
            if 'wikipedia' in text:
                speak('Searching Wikipedia...')
                # text = text.replace("wikipedia", "0000")
                text = text.split("wikipedia")[1]
                text = text.lstrip()
                print(text)
                try:
                    results = wikipedia.summary(text, sentences=3, auto_suggest=False)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                    # link = wikipedia.page(text).links[0]
                except Exception as e:
                    print("ok")
                    # s = random.choice(e.options)
                    if len(e.options) > 0:
                        s = e.options[0]
                        results = wikipedia.page(s)
                        speak("This is what i found on Wikipedia")
                        speak(results.title)
                        speak(results.content[:250])
                        link = results.links[0]
                    else:
                        speak("No result found on Wikipedia")
                # print(link)
            elif 'open youtube' in text:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(2)
            elif 'open google' in text:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(2)

            elif 'open gmail' in text:
                webbrowser.open_new_tab("https://mail.google.com")
                speak("Google Mail open now")
                time.sleep(2)
            elif 'open news' in text:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(2)
            elif 'search'  in text:
                text = text.split("search")[1]
                base_url = "https://www.google.com/search?q="
                query = text
                final_url = base_url + query.replace(" ","%20")
                webbrowser.open_new_tab(final_url)
                time.sleep(2)
            elif 'bob' in text:
                engine.setProperty('voice', engine.getProperty('voices')[0].id)
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
                engine.setProperty('voice', engine.getProperty('voices')[1].id)
            else:
                speak(text)
                
    speak("what is today's date")
    print("start")
    listen()

