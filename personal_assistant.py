import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import time
import wolframalpha
import requests
import webbrowser
import subprocess
num = 1
def speaks(output): 
    global num 
    num += 1
    print("Nes : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    
    file = str(num)+".mp3 "
    toSpeak.save(file) 
    
    playsound.playsound(file, True)  
    os.remove(file) 
  
def get_audio(): 
  
    rec_obj = sr.Recognizer() 
    audio = '' 
    with sr.Microphone() as source: 
        print("Speak...") 
        audio = rec_obj.listen(source, phrase_time_limit =30)  
    print("Stop.")
  
    try: 
        text = rec_obj.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        return text 
  
    except: 
        speaks("Could not understand your audio, PLease try again !") 
        return
  
def process_text(input): 
    try: 
        if "hey" in input or "hi" in input or "hello" in input:
            speaks("hi")
        elif "search" in input or "google" in input or "play" in input or "youtube" in input or "online" in input: 
            search_web(input) 
            return
        elif 'open' in input: 
            open_application(input.lower())  
            return
        elif 'what is your name' in input:
            speak="Nes."
            speaks(speak)
            return
        elif "who are you" in input or "define yourself" in input: 
            speak = '''Hello, I am Nes. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra'''
            speaks(speak) 
            return
        elif "who made you" in input or "created you" in input: 
            speak = "I have been created by someone like you,just smarter."
            speaks(speak) 
            return
  
        elif "calculate" in input.lower(): 
            app_id = "WE6LL5-2A95EYT22P" 
            client = wolframalpha.Client(app_id) 
            indx = input.lower().split().index('calculate') 
            query = input.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            speaks("The answer is " + answer) 
            return

        elif 'what time' in input.lower() or 'tell time' in input.lower():
            t=time.ctime()
            speaks(t)

       

        elif 'joke' in input:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
            if res.status_code == requests.codes.ok:
                speaks(str(res.json()['joke']))
            else:
                speaks('oops!I ran out of jokes')
    
        else: 
            speaks("I can search the web for you, Do you want to continue?") 
            ans = get_audio() 
            if 'yes' in str(ans) or 'yeah' in str(ans): 
                search_web(input) 
            else: 
                return
    except : 
        speaks("I don't understand, I can search the web for you, Do you want to continue?") 
        ans = get_audio() 
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            search_web(input)
        elif 'no' in str(ans) or 'nope' in str(ans):
            exit
   

def search_web(input): 
    
    if 'youtube' in input.lower(): 
        speaks("Opening in youtube") 
        indx = input.lower().split().index('youtube') 
        query = input.split()[indx + 1:] 
        url="http://www.youtube.com/results?search_query="+'+'.join(query) 
        webbrowser.get().open(url)
        return
  
    elif 'wikipedia' in input.lower(): 
        speaks("Opening Wikipedia") 
        indx = input.lower().split().index('wikipedia') 
        query = input.split()[indx + 1:] 
        url="https://en.wikipedia.org/wiki/" + '_'.join(query)
        webbrowser.get().open(url)
        return
  
    else: 
        if 'google' in input: 
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            url="https://www.google.com/search?q="+'+'.join(query)
            webbrowser.get().open(url)
  
        elif 'search' in input: 
            indx = input.lower().split().index('search') 
            query = input.split()[indx + 1:] 
            url="https://www.google.com/search?q="+'+'.join(query)
            webbrowser.get().open(url)
  
        else: 
            url="https://www.google.com/search?q"+'+'.join(query)
            webbrowser.get().open(url)
        return
  
  
# function used to open application 
# present inside the system. 
def open_application(input): 
  
    if "chrome" in input: 
        os.system('start chrome.exe')
        return
    
    elif "microsoft edge" in input:
        os.system('start msedge.exe') 

    elif "wordpad" in input:
        subprocess.Popen('C:\\Windows\\System32\\write.exe')

    elif "word" in input: 
        os.system('start WINWORD.EXE')
        return
  
    elif "excel" in input: 
        os.system('start EXCEL.EXE')
        return
    
    elif "powerpoint" in input or "power point" in input:
        os.system('start POWERPNT.EXE')
        return

    elif "paint" in input:
        os.system('start mspaint.exe')
        return
    elif "notepad" in input:
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        return
    else: 
        speaks("cannot find Application") 
        return

if __name__ == "__main__": 

    try:
        speaks("What's your name?") 
        name = get_audio() 
        speaks("Hello, " + name + '.') 
    except:
        speaks("What's your name?") 
        name = get_audio() 
        speaks("Hello, " + name + '.') 
    while(True): 
            speaks("What can i do for you?") 
            text =get_audio()
    
            if text == 0: 
                continue
    
            if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
                speaks("Ok bye, "+ name+'.') 
                break
            process_text(text)  
