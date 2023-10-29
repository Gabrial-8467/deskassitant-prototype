import webbrowser
import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import wikipedia
from pywikihow import search_wikihow

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
        
def google_search():
    query=takecommand()
    speak('what do you want to search.')
    if 'google' in query:
          query=query.replace("jarvis","")
          query=query.replace("google","")
          speak('searching...')
          kit.search(query)
          speak("i found sir.")
    else:
        speak('Sorry, I could not understand.')

def yt_search():
    query=takecommand()
    speak('what do you want to search.')
    if'youtube search'in query:
          speak("ok sir,I found this on your search!")
          query=query.replace("jarvis","")
          query=query.replace("Youtube search","")
          web='https://www.youtube.com/results?search_query='+query
          webbrowser.open(web)
          speak("i found sir")
    else:
        speak('Sorry, I could not understand.')

def wiki():
    speak('what do you want to search on wikipedia.')
    query=takecommand()
    if'wikipedia'in query:
          speak("searching Wikipedia......")
          query=query.replace("jarvis","")
          query = query.replace("wikipedia","")
          wiki=wikipedia.summary(query,5)
          speak(f"According to wikipedia:{wiki}")
    else:
        speak('Sorry, i could not understand.')

def how_to_searches():
    query=takecommand()
    speak('what do you want to search.')
    if'how to'in query:
          speak("Getting data from internet!")
          op=query.replace("jarvis","")
          max_result=1
          how_to_func=search_wikihow(op,max_result)
          assert len(how_to_func)==1
          how_to_func[0].print()
          speak(how_to_func[0].summary)
    else:
        speak('Sorry, I could not understand.')
