import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyjokes
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
       
    elif hour>=12 and hour<18:
        print("Good Afernoon!")
        speak("Good Afternoon!")
  
    else:
        print("Good Evening!")
        speak("Good Evening!")
    
    print("I am Jarvis Sir. Please tell me how may I help you ?")
    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us') 
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('selim15-12020@diu.edu.bd', 'selim1234')
    server.sendmail('selim15-12020@diu.edu.bd', to, content)
    server.close()

if __name__ == "__main__":

    wishMe()

    query =""
    while (query!="exit now"):
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'tell me about' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'Who' in query:
            print('I am Jarvis and you are my boss.')
            speak('I am Jarvis and you are my boss.')

        elif 'play a music' in query:
            music_dir = 'G:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%p") 
            print(strTime)   
            speak('Sir, the time is'+ strTime)

        elif 'open picture' in query:
            codePath = "G:\\picture"
            os.startfile(codePath)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playig...'+song)
            pywhatkit.playonyt(song)
            

        elif 'joke' in query:
            speak(pyjokes.get_joke()) 


        elif 'date' in query:
            speak('Sorry boss, But i need a girl friend')
            print('Sorry boss, But i need a girl friend')     
     
        elif 'send email to niloy' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "asif15-11895@diu.edu.bd"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my boss Selim Reza. I am not able to send this email")
