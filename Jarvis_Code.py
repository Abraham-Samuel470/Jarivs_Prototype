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
import serial  # For communicating with Arduino
import akinator  # For Akinator integration

# Initialize serial communication with Arduino
try:
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Replace 'COM3' with your Arduino port
    print("Connected to Arduino")
except Exception as e:
    print("Could not connect to Arduino. Ensure the correct port is specified.")
    arduino = None

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=7, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        return "none"
    return query.lower()

def get_date_time():
    now = datetime.now()
    day = now.strftime("%A")
    date = now.strftime("%B %d, %Y")
    time = now.strftime("%I:%M %p")
    return day, date, time

def jarvis_greeting():
    day, date, time = get_date_time()
    hour = int(datetime.now().strftime("%H"))
    if hour >= 0 and hour < 6:
        speak("Sir, it's late. Let's call it a day. If you still have work, I'm here to assist.")
    elif hour >= 6 and hour < 12:
        speak("Good morning, sir.")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon, sir.")
    elif hour >= 16 and hour < 21:
        speak("Good evening, sir.")
    elif hour >= 21 and hour < 23:
        speak("Sir, it's almost bedtime. You should pack things up.")
    speak(f"Today is {day}, the date is {date}, and the current time is {time}.")

# Weather Forecast Function
def get_weather(city):
    API_KEY = "9b8eee7b7de6bcfe4740337c7a786cb1"  # Replace with your OpenWeatherMap API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            temp = main["temp"]
            description = weather["description"]
            humidity = main["humidity"]
            wind_speed = data["wind"]["speed"]

            speak(f"The current temperature in {city} is {temp} degrees Celsius.")
            speak(f"The weather is {description}. Humidity is {humidity}% and the wind speed is {wind_speed} meters per second.")
        else:
            speak("Sorry, I couldn't find weather information for that location. Please try again.")
    except Exception as e:
        speak("There was an error fetching the weather details. Please try later.")

# Akinator Game
import akinator

def play_akinator():
    try:
        aki = akinator.Akinator()
        speak("Think of a character, and I will try to guess it. Say 'Stop' anytime to exit the game.")
        question = aki.start_game()
        
        while True:
            speak(question)
            answer = takecommand().lower()
            
            if "yes" in answer:
                question = aki.answer("yes")
            elif "no" in answer:
                question = aki.answer("no")
            elif "don't know" in answer or "not sure" in answer:
                question = aki.answer("idk")
            elif "probably" in answer:
                question = aki.answer("probably")
            elif "probably not" in answer:
                question = aki.answer("probably not")
            elif "stop" in answer:
                speak("Exiting Akinator. You can play again anytime!")
                break
            else:
                speak("Please answer with yes, no, don't know, probably, or probably not.")

            if aki.progression >= 80:
                speak("I think I know who you are thinking of.")
                aki.win()
                speak(f"Is it {aki.first_guess['name']}? {aki.first_guess['description']}")
                answer = takecommand().lower()
                if "yes" in answer:
                    speak("Yay! I guessed it right!")
                else:
                    speak("Oh no! I'll try better next time.")
                break
    
    except akinator.NoMoreQuestions:
        speak("No questions left to ask. Let me make my guess.")
        aki.win()
        speak(f"My guess is {aki.first_guess['name']} - {aki.first_guess['description']}.")
    except Exception as e:
        speak("An error occurred while playing Akinator.")
        print(f"Error: {e}")




if __name__ == "__main__":
    while True:
        query = takecommand()
        if "wake up" in query:
            jarvis_greeting()
            while True:
                query = takecommand().lower()
                if "go to sleep" in query:
                    speak("OK sir, you can call me anytime.")
                    break
                elif "exit" in query or "stop" in query:
                    speak("Goodbye, sir. Have a great day!")
                elif "lights on" in query and arduino:
                    arduino.write(b"turn on light\n")
                    speak("Turning on the light.")
                elif "lights off" in query and arduino:
                    arduino.write(b"turn off light\n")
                    speak("Turning off the light.")
                    sys.exit()
                elif "play akinator" in query:
                    play_akinator()
                elif "weather in" in query:
                    city = query.replace("weather in", "").strip()
                    get_weather(city)
                elif 'joke' in query:
                    joke = pyjokes.get_joke()
                    speak(joke)
                # Add more functionalities as needed




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
                    speak("Sorry sir, I will come up with something else")

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
