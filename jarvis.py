import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning")
    elif hour>=12 and hour<18:
        speak("good Afternoon")
    else:
        speak("Good evening")
    speak("I am a jarvis sir. Please tell me how may i help you ")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        #r.pause_threshold=1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please....")
        return None
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("noolupremsai.19.it@anits.edu.in","Anits@123")
    server.sendmail('noolupremsai.19.it@anits.edu.in',to,content)
    server.close()

wishMe()
if 1:
    query=takecommand().lower()

    if 'wikipedia' in query:
        speak("searching wikipedia ....")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir,the time is {strTime}")
    elif 'open code' in query:
        codepath="C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    elif 'open chat gpt' in query:
        webbrowser.open("https://chat.openai.com/")

    elif 'email to prem' in query:
        try:
            speak("what should i say")
            content=takecommand()
            to="noolupremsai1@gmail.com"
            sendEmail(to,content)
        except Exception as e:
            print(e)
            speak("sorry my prem  bhai.I am not able to send this email")