import speech_recognition as sr
import cv2
import numpy as np
import os
import pyttsx3
import webbrowser
from pydub import AudioSegment
from pydub.playback import play
import datetime
import openai
from config import apikey
import random

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
chatStr = ""

openai.api_key = "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"

def chat(query):
    global chatStr
    chatStr += f"Bishal: {query}\n Bella:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.2
    )

    engine = pyttsx3.init()
    engine.say(response.choices[0].text)
    engine.runAndWait()
    chatStr += f"{response.choices[0].text}\n"
    return response.choices[0].text


def ai(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.2
    )
    return response.choices[0].text.strip()

def take_command(use_speech_recognition=True):
    if use_speech_recognition:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand.")
            return ""
    else:
        return input("Enter the command: ").lower()




def take_photo():
    #opening the default camera (index 0)
    
    cap = cv2.VideoCapture(0)

# Checking if the camera is opened successfully
    if not cap.isOpened():
        engine = pyttsx3.init()
        engine.say("Failed to open the camera, sorry")
        engine.runAndWait()
            
    # Reading a frame from the camera

    ret, frame = cap.read()

    if ret:

        # Displaying the captured frame
        cv2.imshow("Photo", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Saving the frame as an image
        cv2.imwrite("photo.jpg", frame)

        
        engine.say("Photo captured successfully")
        engine.runAndWait()

    else:
        # engine = pyttsx3.init()
        engine.say("Failed to capture photo, sorry")
        engine.runAndWait()

    cap.release()

if __name__ == '__main__':

    print("\n*****************        Bella   1.O       ******************\n\n")

    engine.say("Hello, I am Bella, your personal assistant. How may i help you")
    engine.runAndWait()

    while True:
    

        text = take_command()
        # engine.say(text)
    
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], 
        ["instagram", "https://www.instagram.com"], ["flipkart", "https://www.flipkart.com"], ["amazon", "https://www.amazon.com"], ["netflix", "https://www.netflix.com"], ["facebook", "https://www.facebook.com"], ["whatsapp", "https://www.whatsapp.com"]]
        for site in sites:
            if f"open {site[0]}" in text:
                engine.say(f"Opening {site[0]}")
                webbrowser.open(site[1])
                # print(f"Opening {site[0]}, sir...")
                engine.runAndWait()

        if "thank you" in text:
            engine = pyttsx3.init()
            engine.say("Thank You for using Bella. Have a nice day")
            engine.runAndWait()
            exit()


        elif "play songs" in text:
            engine = pyttsx3.init()
            engine.say("Which song you want to play ")
            print("\nWhich song you want to play : \n1. Tum hi ho\n2. LSD\n3. Rashiya\n4. Subhanallah\n5. Deva Deva\n\n")
            engine.runAndWait()

            engine = pyttsx3.init()
            engine.say("Enter the song number")
            song_choice = input("Enter the song number:\n")
            engine.runAndWait()

            if song_choice=="1":
                musicPath = r"C:\Users\basfo\Downloads\_Tum Hi Ho_ Aashiqui 2 Full Song With Lyrics  Aditya Roy Kapur, Shraddha Kapoor.mp3"
                webbrowser.open(musicPath)
                engine.runAndWait 
            
            elif song_choice=="2":
                musicPath = r"C:\Users\basfo\Downloads\LSD - Audio (Official Video) ft. Sia, Diplo, Labrinth.mp3"
                webbrowser.open(musicPath)
                engine.runAndWait 
            
            elif song_choice=="3":
                musicPath = r"C:\Users\basfo\Downloads\Rasiya - Lyric Video Brahmāstra Amitabh ,Ranbir, Alia Pritam Tushar, Shreya.mp3"
                webbrowser.open(musicPath)
                engine.runAndWait 

            elif song_choice=="4":
                musicPath = r"C:\Users\basfo\Downloads\_Subhanallah_  Full Video Song  Yeh Jawaani Hai Deewani  Pritam  Ranbir Kapoor, Deepika Padukone.mp3"
                webbrowser.open(musicPath)
                engine.runAndWait 

            elif song_choice=="5":
                musicPath = r"C:\Users\basfo\Downloads\Deva Deva - Extended Film VersionBrahmāstraAmitabh BRanbir @aliabhatt@pritam7415 ArijitJonita.mp3"
                webbrowser.open(musicPath)
                engine.runAndWait 

            else:
                engine = pyttsx3.init()
                engine.say("Invalid choice")
                song_choice = input("Invalid choice")
                engine.runAndWait()
                
        elif "what is the time now" in text:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            engine.say(f"Sir, the current time is {strfTime}")
            engine.runAndWait()
        
        elif "take photo" in text:
            take_photo()

        elif "restart pc" in text:
            engine = pyttsx3.init()
            engine.say("Are you sure , you want to restart your pc ")
            confirm = input("\n\n1. Yes\n2. No\n")
            engine.runAndWait()

            if confirm == '1':
                engine.say("Restarting you PC, do not click any key")
                engine.runAndWait()
                os.system("shutdown/r /t 0")
                break
            else:
                engine.say("PC restart cancelled")
                engine.runAndWait()
                



        elif "open ai" in text:

            engine = pyttsx3.init()
            engine.say("what to do using open a i")
            print("Please provide the command.\n\n")
            engine.runAndWait()
            voice = take_command()
            engine.runAndWait()
            prompt = voice.replace("using artificial intelligence", "").strip()
            res = ai(prompt)
            print("\n\n", res)

            
        else:
            res = chat(text)
            engine = pyttsx3.init()
            engine.say("res")
            print(res)
            engine.runAndWait()
        







