import speech_recognition as sr
import pywhatkit as kit
import pyttsx3

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

def play_music_on_youtube():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Listening for music title or artist...")
        audio = recognizer.listen(source)

    try:
        music_query = recognizer.recognize_google(audio).lower()
        speak(f"You said: {music_query}")
        speak(f"Playing {music_query} on YouTube.")
        kit.playonyt(music_query)

    except sr.UnknownValueError:
        speak("Sorry, I could not understand your music choice.")
    except sr.RequestError as e:
        speak(f"An error occurred: {e}")

if __name__ == "__main__":
    play_music_on_youtube()
