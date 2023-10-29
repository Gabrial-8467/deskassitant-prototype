import pyttsx3
import speech_recognition as sr
import apphandler as ah  # Assuming your app_handler script is in the same directory
import alarm
import timer
import music
import searches as s
import launch_website as lw

engine=pyttsx3.init()
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[1].id)
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

def taskexe():
    while True:
        query = takecommand()

        if 'jarvis' in query:
            speak('Yes, sir.')
        elif 'take some rest' in query:
            speak('Okay, sir. You can call me anytime!')
            break
        elif 'open code' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open camera' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open c compiler' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open whatsapp' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open wordpad' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open powerpoint' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open excel' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open browser' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open brave' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open maps' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open instagram' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open snapchat' in query:
            ah.openapp(query)  # Use the openapp function from app_handler
        elif 'open youtube' in query:
            ah.openapp(query)  # Use the openapp function from app_handlers
        elif 'close code' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close camera' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close c compiler' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close whatsapp' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close word' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close powerpoint' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close excel' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close browser' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close brave' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close maps' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close instagram' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close snapchat' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'close youtube' in query:
            ah.closeapp(query)  # Use the closeapp function from app_handler
        elif 'set alarm' in query:
            speak('Sure, please provide alarm details.')
            alarmhour, alarmmin = alarm.addalarms()
            speak('Alarm set. I will notify you at the specified time.')
            alarm.playalarm(alarmhour, alarmmin)
        elif'set a timer'in query:
            timer.set_timer_by_voice()
        elif'play music'in query:
            music.play_music_on_youtube()
        elif'search on internet'in query:
            s.google_search()
        elif'search on youtube'in query:
            s.yt_search()
        elif'open wikipedia'in query:
            s.wiki()
        elif'open searches'in query:
            s.how_to_searches()
        elif'open website' in query:
            lw.launch_site()
        
        

if __name__ == "__main__":
    speak('I am ready to help you.')

taskexe()
