import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)
def userInit():
    print("Login Name : ",end='')
    _name_=input()
    return _name_ 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(User):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Evening")


    speak("Jarvis here {}, whatcha wanna do?".format(User))       

def takeCommand():
    #It takes mocrophone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)



if __name__ == "__main__":
    User=userInit()
    wishMe(User)
