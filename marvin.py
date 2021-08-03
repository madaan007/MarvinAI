import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import random
import pywhatkit as kit
import smtplib
import sys
import urllib
import requests
from  requests import get

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
 #print(voices[1].id)       two voices 
engine.setProperty('voice', voices[0].id)

# text to speech

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wish function for greeting

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Sir!')
    
    elif hour>=12 and hour<18:
        speak('Good Afternoon Sir!')
    else:
        speak('Good evening sir!')

    speak('I am Marvin sir. please tell me how may I assist you today!')

    
# speech totext

def takeCommand():
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am Listening....')
        r.pause_threshold = 1
        audio =  r.listen(source)

    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')

    except Exception as e:
        speak("Please perdon")
        #print("Please perdon")

        return "None"

    return query


# to send email

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)  # 587 server name (open source)
    server.ehlo()
    server.starttls()
    server.login("your email id", "password")
    server.sendmail("from_addr", to,content )
    server.close()
    
       

if __name__ == "__main__":
    wish_me()
    while True:

        query= takeCommand().lower()
        # logic for tasked based on query

        if "wikipedia" in query:
            
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 2)
            
            speak(results)

        elif " open youtube" in query:
            webbrowser.open("youtube.com")

        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir the time is {strTime}")

        
        elif "open code" in query:
            codePath = "C:\\Users\\hp1\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "vlc" in query:
            path = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(path)
        
        elif "command prompt" in query:
            os.system("start cmd")

        elif "how are you" in query:
            speak("I am fine sir. Thankyou for asking!")

        elif "play music" in query:
            music_dir = "G:\\fav\\songs"
            songs = os.listdir(music_dir)   
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd ))

        elif "open google" in query:
            speak("Sir, what should I search")
            query = takeCommand().lower()
            webbrowser.open(f"{query}")
            speak("here is what I found for" + query)
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        elif "play youtube" in query:
            kit.playonyt("see you again")

        elif "email to me" in query:
            try:
                speak("what should i mail")
                content = takeCommand().lower()
                to = "manshumadaan69@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry sir, email not sent")

        elif "ip address" in query:
            
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"your ip address is {ip}")

        elif "find location" in query:
            speak("what is the location")
            query = takeCommand().lower()
            url = 'https://google.nl/maps/place/'+ query + '/&amp;'
            webbrowser.open(url)
            speak("here is the location of" + query)

        # to find my location using ip address

        elif "locate me" in query:
            speak("wait sir, let me check")
            try:

                ipadd = get('https://api.ipify.org').text
                print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json' 
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                print(geo_data)
                city = geo_data['city']
                continent= geo_data['continent_code']
                country = geo_data['country']
                
                speak(f"sir i think we are in {city} city of {country} country having {continent} continent")

            except Exception as e:
                speak("sorry sir, due to some network issue i am unable to locate us")
                pass

        
        elif "no thanks" in query:
            speak("Sir! It was a pleasure assisting you. Have a great day ahead")
            sys.exit()
        


        speak("Sir, is there any other work to do")


        


       
