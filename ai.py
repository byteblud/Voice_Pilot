import speech_recognition as sr
import pyttsx3
import webbrowser
import requests 
import google.generativeai as genai
import os
import pywhatkit
def google(com):
    webbrowser.open('https://www.google.com')
def youtube(com):
    webbrowser.open('https://www.youtube.com/') 
def songs(com):
    # song=com.replace('song','').replace('play','');
    # for i in song:
    #     if i in music.keys():
    #         webbrowser.open(music[i])
    pywhatkit.playonyt(com);
def shutdown(com):
    speak('Shutting the jarvis down..... ')
    exit()               
def ai(com):
    genai.configure(api_key="AIzaSyAQHOczWOv-vrOIw6QsvyVsod0znCsvsc4")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(com)
    response.text.replace('@,#,$,%,*','')
    print('\n',response.text);
    speak(response.text);
        
def ACtivation():
        speak("Jarvis Activated successfully")
        speak("Sir Welcome to command center")
        speak("How can i help you")
        while True:
            try:
                with sr.Microphone() as source:
                    audio=r.listen(source,phrase_time_limit=5)
                    comand=r.recognize_google(audio);
                    if(comand):
                        os.system('cls');
                        print( 'Task: ',comand);
                    if 'open google' in comand.lower() :
                        google(comand)
                    elif 'play song' in comand.lower():
                        songs(comand)
                    elif 'open youtube' in comand.lower():
                        youtube(comand)
                    elif  ('shutdown' or 'close')in comand.lower():
                        shutdown(comand)   
                    else:
                        ai(comand)    
            except Exception as e:
                speak("THe Waiting  for Your command ")
                    
# for the frist voice
def speak(aud):
    engine=pyttsx3.init()
    engine.say(aud)
    engine.setProperty('rate',120)
    engine.runAndWait()
if __name__=='__main__' :
    speak("Initiallizing   Jarvis.") 
    r=sr.Recognizer()
    while True:
            with sr.Microphone() as source:
                print('listning......')
                audio=r.listen(source,phrase_time_limit=5)
                comand=r.recognize_google(audio)
                if  'activate jarvis' in comand.lower() :
                    ACtivation()
                else:
                    speak("Sir please Spell the Activation key")    
 
          