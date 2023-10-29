import os
import webbrowser
import pyttsx3
import keyboard

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def openapp(query):
    speak('OK, sir. Please wait a moment.')
    if 'code' in query:
        os.startfile("C:\\Users\\gabri\\OneDrive\\Desktop\\Visual Studio Code.lnk")
    elif 'camera' in query:
        os.startfile("C:\\Users\\gabri\\OneDrive\\Desktop\\Camera.lnk")
    # Add more application paths here following the same pattern
    elif'c compiler'in query:
        os.startfile("C:\\Users\\gabri\\OneDrive\\Desktop\\Embarcadero Dev-C++.lnk")
    elif'whatsapp'in query:
        os.startfile("C:\\Users\\gabri\OneDrive\\Desktop\\WhatsApp.lnk")
    elif'wordpad'in query:
        os.startfile("C:\\Users\\gabri\\OneDrive\\Desktop\\Word.lnk")
    elif'powerpoint'in query:
        os.startfile("C:\\Users\\gabri\\OneDrive\\Desktop\\PowerPoint.lnk")
    elif'excel'in query:
        os.startfile("C:\\Users\\gabri\\OneDrive\\Desktop\\Excel.lnk") 
    elif'browser'in query:
        os.startfile("C:\\Users\\Public\\Desktop\\MS Edge.lnk")  
    elif'brave'in query:
        os.startfile("C:\\Users\\gabri\\OneDrive\\Desktop\\Gabrial - Brave.lnk")
    elif'maps'in query:
        webbrowser.open('https://www.google.co.in/maps')
    elif'instagram'in query:
        webbrowser.open('https://www.instagram.com/')
    elif'snapchat'in query:
        webbrowser.open("https://www.snapchat.com/")
    elif'youtube'in query:
        webbrowser.open('https://www.youtube.com/')
    else:
        speak('File not found.')

def closeapp(query):
    speak('OK, sir. Please wait a moment.')
    if 'code' in query:
        os.system("TASKKILL /F /im Code.exe")
    elif 'camera' in query:
        os.system("TASKKILL /F /im Camera.exe")
    # Add more application names here for closing
    elif'c compiler'in query:
        os.system("TASKKILL /F /im devcpp.exe")
    elif'whatsapp'in query:
        os.system("TASKKILL /F /im WhatsApp.exe")
    elif'wordpad'in query:
       os.system("TASKKILL /F /im Word.exe")
    elif'powerpoint'in query:
       os.system("TASKKILL /F /im PowerPnt.exe")
    elif'excel'in query:
       os.system("TASKKILL /F /im Excel.exe") 
    elif'browser'in query:
        os.system("TASKKILL /F /im MSEdge.exe")  
    elif'brave'in query:
        os.system("TASKKILL /F /im brave.exe")
    elif'maps'in query:
        keyboard.press_and_release('ctrl+w')
        keyboard.press_and_release('ctrl+n')
    elif'instagram'in query:
        keyboard.press_and_release('ctrl+w')
        keyboard.press_and_release('ctrl+n')
    elif'snapchat'in query:
        keyboard.press_and_release('ctrl+w')
        keyboard.press_and_release('ctrl+n')
    elif'youtube'in query:
        keyboard.press_and_release('ctrl+w')
        keyboard.press_and_release('ctrl+n')
    else:
        speak("I can't understand.")
    
