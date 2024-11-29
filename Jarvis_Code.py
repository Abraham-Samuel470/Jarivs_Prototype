import os
import pyttsx3
import speech_recognition as sr
import pyaudio
from datetime import datetime
import wikipedia
import requests
import webbrowser
import sys
import pyjokes
import subprocess


# inititalzing text to speech engine
engine=pyttsx3.init('sapi5') # init will inititalize it
voice=engine.getProperty('voices')# stroes the voice in voice variable
engine.setProperty('voice',voice[0].id)# give the voice to speak
# 0= male voice and 1= female voice or cn change between 0-1(i.e 0.2,0.5)

# by this Jarvis will speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
# our voice to text in runtime
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio= r.listen(source,timeout=7,phrase_time_limit=5)
    try:
        print("Recognizing")
        query= r.recognize_google(audio, language='en-in')
        print(f"user said :{query}")
    except Exception as e :
        #speak("Sir, i couldn't get it , please say that again please")
        return "none"
    return query
#date,day,time
def get_date_time():
    now=datetime.now()
    day=now.strftime("%A")
    date=now.strftime("%B %d, %Y")
    time=now.strftime("%I:%M %p")
    return day,date,time

def jarvis_greeting():
    day,date,time=get_date_time()
    hour = int(datetime.now().strftime("%H"))
    #speak(f"Today is {day}, the date is {date}, and the current time is {time}.")
    if hour>0 and hour<=6:
        speak("Sir, it's so late, let's call it a day and you should go to sleep ")
        speak("If you still have any work at this hour i will assist you but please take care of your health ")
        speak(f"Today is {day}, the date is {date}, and the current time is {time}.")
    elif hour>6 and hour<=12:
        speak("Good morning sir ")
        speak(f"Today is {day}, the date is {date}, and the current time is {time}.")

    elif(hour>12 and hour<=16):
        speak("Good Afternoon Sir ")
        speak(f"Today is {day}, the date is {date}, and the current time is {time}.")

    elif(hour>16 and hour<=21):
        speak("Good Evening sir")
        speak(f"Today is {day}, the date is {date}, and the current time is {time}.")
    elif(hour>21 and hour<23):
        speak("Sir, it's almost your bedtime, you should pack things up")


if __name__=="__main__":
    while True:
        query = takecommand().lower()
        if "wake up" in query:
            #wish()
            jarvis_greeting()
            while True:
                query = takecommand().lower()
                if "go to sleep" in query :
                    speak("OK sir, you can call me anytime")
                    break
                # This command will stop the program completely.
                elif "exit" in query or "stop" in query:
                    speak("Goodbye, sir. Have a great day!")
                    sys.exit()  

                # logic building for tasks
    #1 notepad
                elif 'how are you' in query:
                    speak("I am fine sir, what about you")
                elif 'doing great' in query:
                    speak("Good to hear sir")
                    speak("Tell me how can i help")
                elif 'yes i found it useful' in query:
                    speak("Thank you sir")

                elif "open notepad" in query:
                    npath="C:\\Windows\\system32\\notepad.exe"
                    os.startfile(npath)
                    speak("Opening Notepad Sir")
                # elif " close it " in query:
                #     os.system("taskkill /f im notepad.exe")
                #     speak("Closing notepad sir")
                elif " close notepad" in query:
                    notepad_windows = gw.getWindowsWithUntitle('Notepad')
                    for window in notepad_windows:
                        window.close()
                    speak("Notepad is now closed.")
                            #OR use the below
        # elif "open youtube" in query:
        #     npath="https://www.youtube.com/?bp=wgUCEAE%3D "
        #     os.startfile(npath)
        #     speak("Opening Youtube Sir")
    #2 cmd prompt
                elif "open command prompt" in query:
                    os.system("start cmd")
                    speak("Opening command prompt sir ")
    #3 ip address
                elif "ip address" in query:
                    ip = requests.get('https://httpbin.org/ip').json()['origin']
                    speak(f'Your public IP address is: {ip}')
                    print(f"your IP address is {ip}")
    #4 wikipedia
                elif " wikipedia" in query:
                    speak("searching wikipedia")
                    query = query.replace("wikipedia"," ")
                    results = wikipedia.summary(query,sentences=2)
                    speak("thanks for waiting here's what i found")
                    speak("according to wikipedia")
                    speak(results)
                    speak("hope you find it useful")
                    print(results)
                elif "yes" in query:
                    speak("It's my pleasure sir")
                elif "no "in query:
                    speak("Sorry sir, I will come up with something else"

    #5 webbrowser
                 #OR use the below
                
        # elif " open youtube " in query:
        #     webbrowser.open("www.youtube.com")
        #     speak("opening youtube")
                elif "open youtube" in query:
                    npath="https://www.youtube.com/"
                    os.startfile(npath)
                    speak("opening youtube")
                elif " are you deaf" in query:
                    speak("no you is blind and i don't have ears")
                    
                            #OR use the below
                
                # elif "open youtube " in query:
                #     webbrowser.open_new_tab('https://www.youtube.com/')
                #     speak("opening youtube")
    #6 chrome
                elif "open chrome" in query:
                    webbrowser.open('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
                    speak('Opening chrome')
    #7 chatgpt
                elif "open chat gpt" in query:
                    webbrowser.open('https://chatgpt.com/')
                    speak("opening chat GPT")
                elif "open google" in query:
                    speak("sir, what should i search for")
                    cm = takecommand().lower()
                    webbrowser.open(f"{cm}")
                    speak("here's what i found")
    #8 Jokes
                elif 'joke' in query:
                    joke = pyjokes.get_joke()
                    speak(joke)
                

