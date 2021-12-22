import pyttsx3

engine=pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def bring_in_bob():
    engine.setProperty('voice', engine.getProperty('voices')[0].id)

def bring_in_alice():
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
