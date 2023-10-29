import webbrowser
import pyttsx3
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    print("    ")
    engine.say(audio)
    print(f": {audio}")
    print("    ")
    engine.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language='en-in')
            print(query)
            return query.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

def launch_site():
    speak('Which website do you want to open.')
    name=takecommand()
    web='https://www.'+name+'.com'
    webbrowser.open(web)
    speak('Done sir!')
   
