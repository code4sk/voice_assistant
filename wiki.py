from speak_engine import speak
import wikipedia

def wiki(text):
    speak('Searching Wikipedia...')
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
        try:
            s = e.options[0]
            results = wikipedia.page(s)
            speak("This is what i found on Wikipedia")
            speak(results.title)
            speak(results.content[:250])
            link = results.links[0]
        except:
            speak("No result found on Wikipedia")
    # print(link)