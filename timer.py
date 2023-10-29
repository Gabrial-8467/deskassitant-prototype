import time
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def timer(seconds):
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        timer_display = '{:02d}:{:02d}'.format(minutes, sec)
        print(timer_display, end='\r')  # Clear the line and print the updated time
        time.sleep(1)
        seconds -= 1

    speak("Time's up!")

def set_timer_by_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Say the timer duration in seconds.")
        audio = recognizer.listen(source)

    try:
        duration = int(recognizer.recognize_google(audio))
        speak(f"Setting a timer for {duration} seconds.")
        timer(duration)
    except sr.UnknownValueError:
        speak("Sorry, I could not understand your input.")
    except sr.RequestError as e:
        speak(f"An error occurred: {e}")
