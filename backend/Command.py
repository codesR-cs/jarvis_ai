import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")      # Update the frontend display
        r.pause_threshold = 1  # seconds of silence before ending phrase
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 7)
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)                       # frontend display updated with recognized text
        speak(query)                                    # speak function called here 
        eel.Show()
    except Exception as e:
        print("Say that again please...")
        eel.DisplayMessage("Say that again please...")
        time.sleep(1)
        eel.Show()
        return ""

    return query.lower() #lower case


