import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print(" Not Understand ")
#sptext()
def text_to_speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()
def Et():
    while(1):
        print("Enter the numbers only between 1 and 10")
        a = int(input("Enter the number: "))
        if(a == 125):
            text_to_speech("Your name is Shubham Yadav")
        elif(a == 127):
            text_to_speech("Your name is Yash Hingad")
        elif(a == 114):
            text_to_speech("Your name is Shrihari")
        else:
            text_to_speech("You entered a wrong number")
Et()
        

