import speech_recognition as sr

def takeInput(source):
        while True:
            try:
                r = sr.Recognizer()
                # r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                # print(audio)
                command = r.recognize_google(audio, language='en-in')
                return command
            except Exception as e:
                # print("hello", e)
                continue
        return "null"
