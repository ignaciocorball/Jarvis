from playsound import playsound
from datetime import datetime
from os import system
from os import system, name 
import win32gui
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import subprocess
import time
import requests
import json
import pathlib

#Enviroment Config
appname = 'Command Prompt'
xpos = 1260
ypos = 1
width = 600
length = 1200
myCoolTitle = "JARVIS - AI FOR GAMERS"
system("title " + myCoolTitle)

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if appname in win32gui.GetWindowText(hwnd):
            win32gui.MoveWindow(hwnd, xpos, ypos, width, length, True)
win32gui.EnumWindows(enumHandler, None)



#STRINGS AND VARIABLES
currentProgramPath = pathlib.Path().absolute()
supremePath = r"C:\\Program Files\\Supreme\\SUPREME.exe"
gamersclubPath = r"C:\Users\GhostY\AppData\Local\Programs\gcac-launcher\\Gamers Club AC Launcher.exe"
microsoftTeamsArgs = [r'C:\Users\GhostY\AppData\Local\Microsoft\Teams\Update.exe', '--processStart', 'Teams.exe']
photoshopPath = r"C:\Program Files\Adobe\Adobe Photoshop 2020\Photoshop.exe"
spotifyPath = r"C:\Users\GhostY\AppData\Roaming\Spotify\Spotify.exe"
vegasPath = r"C:\Program Files\VEGAS\VEGAS Pro 17.0\vegas170.exe"
whoIsJarvisWAV = r'C:\Users\GhostY\OneDrive\Documentos\Local Repository\Python Practice\Jarvis-Python\resources\\whoIsJarvis.wav'
goodMorningJarvis = r'C:\Users\GhostY\OneDrive\Documentos\Local Repository\Python Practice\Jarvis-Python\resources\\goodMorningJarvis.wav'
# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def setup_Enviroment():
    system("cls")
    os.system('mode con: cols=80 lines=100')
    print("                                                                      ")
    print("         ____      __        _______  ___      ___  __      ________            ")
    print(r"""         |"  |    /""\      /"      \|"  \    /"  ||" \    /"       )      """)
    print(r"         ||  |   /    \    |:        |\   \  //  / ||  |  (:   \___/           ")
    print(r"         |:  |  /' /\  \   |_____/   ) \\  \/. ./  |:  |   \___  \             ")
    print(r"      ___|  /  //  __'  \   //      /   \.    //   |.  |    __/  \\            ")
    print(r"     /  :|_/ )/   /  \\  \ |:  __   \    \\   /    /\  |\  \" \   :)           ")
    print(r"    (_______/(___/    \___)|__|  \___)    \__/    (__\_|_)(_______/            ")
    print(u"\u001b[37m                                                                     ")
    print(r"                                  _..._                                     ")
    print(r"                                .'     '.      _                            ")
    print("                               /    .-\"\"-\   _/ \                         ")
    print(r"                             .-|   /:.   |  |   |                           ")
    print(r"                             |  \  |:.   /.-'-./                            ")
    print(r"                             | .-'-;:__.'    =/                             ")
    print("                             .'=  *=|\u001b[36;1mSpaceX\u001b[37m_.='          ")
    print(r"                           /   _.  |    ;'                                   ")
    print(r"                          ;-.-'|    \   |                                   ")
    print(r"                         /   | \    _\  _\                                ")
    print(r"                         \__/'._;.  ==' ==\                               ")
    print(r"                                  \    \   |                              ")
    print(r"                                  /    /   /                              ")
    print(r"                                 /-._/-._/                                ")
    print(r"                                 \   `\  \                                ")
    print(r"                                  `-._/._/                                ")
    print(r"                                                                            ")
    print(r"                                                                            ")




    print("                          \u001b[32mDeveloped by \u001b[36mGhostY\u001b[32m                                  ")
    print("                              \u001b[1m\u001b[36mMIT Licence\u001b[32m                                      ")
    print("                                                                               ")


def take_commands():
    setup_Enviroment()
    win32gui.EnumWindows(enumHandler, None)
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print("    ┍╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼┑  ")
        print(u"    |~   [\u001b[31mSTATUS\u001b[32m]    \u001b[36mListening\u001b[32m       ~|  ")
        print("    ┕╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼┙  ")
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("    ┍╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼┑  ")
            print("    |~   [\u001b[31mSTATUS\u001b[32m]    \u001b[36mRecognizing\u001b[32m     ~|  ")
            print("    ┕╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼┙  ")
            # Recognizing audio using google api
            Query = r.recognize_google(audio) # r.recognize_google(audio, language='es-ES') #Set Spanish
            print("Query='", Query, "'")
        except Exception as e:
            print(e)
            # returning none if there are errors
            return "None"
    # returning audio as text
    return Query

# creating Speak() function to giving Speaking power
# to our voice assistant 
def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    #engine.setProperty('voice', 'spanish') #Speak in Spanish
    engine.say(audio) 
    engine.runAndWait()


# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        #ENGLISH COMMANDS

        #VOICE COMMANDS
        if "exit" in command:
            Speak("Sure sir! as your wish, bai")
            break

        if "learn" in command:
            Speak("copyassignment website is best to learn python")

        if "code" in command:
            Speak("You can get this code from copyassignment website")

        if "destroy Google" in command:
            Speak("Hacking google Sir")

        if "ey Jarvis" in command:
            Speak("Yes Sir?")

        if "enable secure mode" in command:
            Speak("Setting up the secure mode sir")

        if "what do you think about Alexa" in command:
            Speak("I think she conspires with google to dominate the world")

        if "disable secure" in command:
            Speak("Setting down the secure mode sir")
        
        if "thank you" in command:
            Speak("as your wish sir")

        
        if "hello Jarvis" in command:
            Speak("Hello Ghost e")
            time.sleep(0.5)
            Speak("Today's gonna be a good day")

        if "who are you" in command:
            playsound(whoIsJarvisWAV)

        if "good morning" in command:
            playsound(goodMorningJarvis)
        
        if "is the math test difficult" in command:
            Speak("No, is not difficult, it is imposible")

        if "speak in chileno" in command:
            Speak("Que wea queri que te diga")

        #TASK COMMANDS
        if "time to study" in command:
            Speak("Setting up the study enviroment sir")
            subprocess.call(microsoftTeamsArgs)

        if "black hat environment" in command:
            Speak("Loading and Setting up the black hat hacking environment.")
            time.sleep( 5 )
            Speak("The weapons are loaded sir")

        if "open Instagram" in command:
            Speak("Opening instagram sir")
            webbrowser.open(r'https:\\instagram.com\GhostY.xyz', new=2)

        if "open University" in command:
            Speak("Opening C F T webpage sir")
            webbrowser.open(r'https://adfs.inacap.cl/adfs/ls/?wtrealm=https://siga.inacap.cl/sts/&wa=wsignin1.0&wreply=https://siga.inacap.cl/sts/&wctx=https%3a%2f%2fadfs.inacap.cl%2fadfs%2fls%2f%3fwreply%3dhttps%3a%2f%2fwww.inacap.cl%2ftportalvp%2fintranet-alumno%26wtrealm%3dhttps%3a%2f%2fwww.inacap.cl%2f', new=2)

        if "open GC" in command:
            Speak("Opening Gamers Club Sir")
            os.startfile(gamersclubPath)

        if "open Supreme" in command:
            Speak("Opening Supreme Sir")
            os.startfile(supremePath)

        if "open Photoshop" in command:
            Speak("Opening photo shop Sir")
            os.startfile(photoshopPath)       

        if "open Sony Vegas" in command:
            Speak("Opening Vegas Pro Sir")
            os.startfile(vegasPath)   


        #INFORMATION GATHERING
        if "open Spotify" in command:
            os.startfile(spotifyPath) 
            Speak("Opening Spotify Sir")

        if "stop music" in command:

            Speak("Music has been paused sir")

        if "what time is it" in command:
            Speak("are ")
            Speak(datetime.now().strftime("%I"));
            time.sleep(0.1)
            Speak(datetime.now().strftime("%M %p"))

        if "open cheats" in command:

            Speak("cheats are loaded sir")
        


        

        




