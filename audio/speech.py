import pyttsx3
import speech_recognition as sr
import ui.gui as gui

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    gui.update_text_speaker(text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        #audio = r.listen(source)
        #Adjust or remove the phrase_time_limit as per your needs
        audio = r.listen(source, phrase_time_limit=10)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        gui.update_text_listener(query)
    except Exception as e:
        query = None 
    return query

if __name__ == '__main__':
    speak("Hello, how are you doing?")
    audio_text = listen()
    print(audio_text)
