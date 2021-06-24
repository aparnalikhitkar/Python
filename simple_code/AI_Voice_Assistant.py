# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 13:34:30 2021

@author: aparn
"""

import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr #pip install SpeechRecognition 

engine = pyttsx3.init()
voices = engine.getProperty("voices")

#this is for change the assistent voice 0 for male 1 for female 
engine.setProperty("voice",voices[1].id)

#this change the speed of assistant 
# newVoiceRate = 190
engine. setProperty("rate", 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

#it show corrent time 
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
#time()
    
    # it speak current date 
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)
    
#date()


#wish me how can i help you 
def wishme():
    speak("welcome back aparna !")
    time()
    date()
    
    hour = datetime.datetime.now().hour
    
    if hour >= 6 and hour <12:
        speak("Good morning ")
    elif hour >=12 and hour < 18:
        speak("good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("good evening ")
    else :
        speak("Good night")
        
    speak("anay at your service . How can I help you ?")
wishme()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try :
        print("Recogninzing...")
        query = r.recognize_google(audio , language = 'en=US')
        print(query)
    except Exception as e :
        print(e)
        speak("Say that again please ...")
        return "None"
    return query

takeCommand()




































































