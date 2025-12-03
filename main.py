

import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import datetime
import wikipedia
import subprocess

recognizer = sr.Recognizer()






def talk (text) :      
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id) 
    voice = engine.getProperty('voices')
    engine.setProperty("voice",voice[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine


def take_command():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out...")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            return ""


talk("Hi, I am ready. Say hello to wake me up!")

awake = False

while True:
    command = take_command()

    if not awake and "hello" in command:
        awake = True
        talk("Hello! How can I help you?")
        print("Assistant Activated!")

    elif awake:
        if "time" in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The time is {current_time}")
        elif "open youtube" in command:
            talk("Opening YouTube")
            webbrowser.open("https://youtube.com")
        elif "open google" in command:
            talk("Opening Google")
            webbrowser.open("https://google.com")
        elif "open facebook" in command:
            talk("Opening Facebook")
            webbrowser.open("https://facebook.com")
        elif "open linkedin" in command:
            talk("Opening LinkedIn")
            webbrowser.open("https://linkedin.com")
        elif "open excel" in command:
            talk("Opening Excel")
            subprocess.Popen(r"C:\Users\Jatin\Desktop\2025-26.xlsx",shell=True)
        elif "go to desktop" in command:
            talk("Going to desktop")
            pyautogui.hotkey("win", "d")
        elif "stop" in command or "exit" in command:
            talk("Goodbye!")
            break  # End the loop instead of continuing silently
        elif command == "":
            talk("Deactivated")
        elif command != "" :
            try :
                info = wikipedia.summary(command,sentences=3)
                talk(info)
            except Exception as e :
                talk("Sorry I not Found !")
        else:
            talk("Sorry, I didn't catch that.")

        print("Deactivated!")
        awake = False




