import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import time
import random
import pyautogui
import requests
from bs4 import BeautifulSoup
from num2words import num2words

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine. setProperty("rate", 170)
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 00 and hour < 12:
        speak("Good Morning Boss, How can i help you")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss, How can i help you")
    else:
        speak("Good Evening Boss, How can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print()
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print("Couldn't recognize. Try Again.")
        return "None"
    return query   


if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            query = query.replace("Wikipedia", "")
            try:
                speak("Searching on wikipedia")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak("Here is what I found")
                speak(results)
            except :
                print("No Results Found!")
                speak("No Results Found related to "+query+" on wikipedia")
                
        elif 'weather' in query:
            city = "noida"
 
            url = "https://www.msn.com/en-in/weather/forecast/in-Sadar,Up?loc=eyJsIjoiU2FkYXIiLCJyIjoiVXAiLCJjIjoiSW5kaWEiLCJpIjoiSU4iLCJnIjoiZW4taW4iLCJ4Ijo3Ny40NTk5OTkwODQ0NzI3LCJ5IjoyOC41MjAwMDA0NTc3NjM3fQ%3D%3D&weadegreetype=C&ocid=winp2sv1plus&cvid=55554a143c6b43c4bd7404e65c51a9ea"
            html = requests.get(url).content
 
            soup = BeautifulSoup(html, features="html.parser")

            temp = soup.find('a', attrs={'class': 'summaryTemperatureCompact-E1_1 summaryTemperatureHover-E1_1'}).text
            sky = soup.find('div', attrs={'class': 'summaryCaptionCompact-E1_1'}).text
            temp = temp.replace("°C ", "")
            temp = temp[0]+temp[1]
            temp = int(temp)
            temp = num2words(temp)
            temp = "Currently, temperatue is "+temp+" degree celcius outside."
            sky = "the sky is expected to remain "+sky+" today"

            speak(temp)
            speak(sky)

        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open('https://www.youtube.com/')
            exit(0)

        elif 'open github' in query:
            speak("Opening github")
            webbrowser.open('https://www.github.com/')    
            exit(0)

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open('https://www.google.com/')  
            exit(0)

        elif 'random song' in query:
            list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
            num = random.choice(list1)
            dir = 'C:\\Users\\asmit\\Music\\Punjabi Songs'
            songs = os.listdir(dir)
            speak("Playing a random song from your playlist boss")
            os.startfile(os.path.join(dir, songs[num]))
            exit(0)

        elif 'favourite song' in query:
            dir = 'C:\\Users\\asmit\\Music\\Punjabi Songs'
            songs = os.listdir(dir)
            speak("Playing your favourite song boss")
            os.startfile(os.path.join(dir, songs[16]))
            exit(0)
        
        elif 'shiva' in query:
            speak("What's your message boss?")
            msg = takeCommand()
            num = "919927113426"
            webbrowser.open("https://web.whatsapp.com/send?phone="+num+"&type=phone_number&app_absent=0")
            time.sleep(10)
            pyautogui.typewrite(msg)
            pyautogui.press('enter')
            speak("Message sent successfully")
            exit(0)

        elif 'pranjal' in query:
            speak("What's your message boss?")
            msg = takeCommand()
            num = "918595854148"
            webbrowser.open("https://web.whatsapp.com/send?phone="+num+"&type=phone_number&app_absent=0")
            time.sleep(10)
            pyautogui.typewrite(msg)
            pyautogui.press('enter')
            speak("Message sent successfully")
            exit(0)

        elif 'vedansh' in query:
            speak("What's your message boss?")
            msg = takeCommand()
            num = "917291873228"
            webbrowser.open("https://web.whatsapp.com/send?phone="+num+"&type=phone_number&app_absent=0")
            time.sleep(10)
            pyautogui.typewrite(msg)
            pyautogui.press('enter')
            speak("Message sent successfully")
            exit(0)

        elif 'mummy' in query:
            speak("What's your message boss?")
            msg = takeCommand()
            num = "918368283735"
            webbrowser.open("https://web.whatsapp.com/send?phone="+num+"&type=phone_number&app_absent=0")
            time.sleep(10)
            pyautogui.typewrite(msg)
            pyautogui.press('enter')
            speak("Message sent successfully")
            exit(0)  
  
        elif 'quit' in query:  
            speak("okay, Goodbye boss")    
            exit(0)

        elif 'stop' in query:  
            speak("okay, Goodbye boss")  
            exit(0)   

        elif 'exit' in query:  
            speak("okay, Goodbye boss") 
            exit(0)      

        elif 'shut' in query:  
            speak("Goodbye boss, shutting down") 
            os.system("shutdown /s /t 5")    
            exit(0)   

        elif 'stupid' in query:
            speak("I wish I was as smart as you, boss")

        elif 'introduce' in query:
            speak("okay, so, I am jarvis, an AI assistant made by asmit chauhan, just for fun")
        
        elif 'who' in query:
            speak("okay, so, I am jarvis, an AI assistant made by asmit chauhan, just for fun")

        elif "not funny" in query:
            speak("I am an AI, not a joker, boss")

        elif "how are you" in query:
            speak("I am totally in a mood to help you with all of my potential")