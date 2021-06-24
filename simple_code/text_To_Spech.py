# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 13:55:17 2021

@author: aparn
"""

# Python program to show
# how to convert text to speech
import pyttsx3

# Initialize the converter
converter = pyttsx3.init()

# Set properties before adding
# Things to say

# Sets speed percent
# Can be more than 100
converter.setProperty('rate', 150)
# Set volume 0-1
converter.setProperty('volume', 0.7)
voices = converter.getProperty('voices')

for voice in voices:
	# to get the info. about various voices in our PC
	print("Voice:")
	print("ID: %s" %voice.id)
	print("Name: %s" %voice.name)
	print("Age: %s" %voice.age)
	print("Gender: %s" %voice.gender)
	print("Languages Known: %s" %voice.languages)

# Queue the entered text
# There will be a pause between
# each one like a pause in
# a sentence
converter.say("Hello GeeksforGeeks")
converter.say("I'm also a geek")

# Empties the say() queue
# Program will not continue
# until all speech is done talking
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# Use female voice
converter.setProperty('voice', voice_id)

converter.runAndWait()
