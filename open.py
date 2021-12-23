from speak_engine import speak
import time
import webbrowser

def open(text):
    if "open youtube" in text:
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
    elif 'open whatsapp' in text:
        webbrowser.open_new_tab("https://web.whatsapp.com/")
        speak("Whatsapp open now")
        time.sleep(2)
    elif 'open amazon' in text:
        webbrowser.open_new_tab("https://amazon.in/")
        speak("Amazon open now")
        time.sleep(2)
    elif 'open meet' in text:
        webbrowser.open_new_tab("https://meet.google.com/")
        speak("Google meet open now")
        time.sleep(2)
    elif 'open github' in text:
        webbrowser.open_new_tab("https://github.com/")
        speak("Github open now")
        time.sleep(2)
    
