import speech_recognition
import pyttsx3
import os
import sys
import keyboard
from datetime import datetime

import recordingState

def speechToText():
    recogniser=speech_recognition.Recognizer()
    resText = ""
    while True:
        try:
            if recordingState.in_progress == False:
                break
            with  speech_recognition.Microphone() as mic:
                recogniser.adjust_for_ambient_noise(mic)
                audio=recogniser.listen(mic)

                text=recogniser.recognize_google(audio)
                resText += text.lower()
        except Exception:
            continue


    name=sys.path[0]+"\\Recordings\\TextFile_" + str(datetime.today().strftime("%Y_%m_%d"))+"_"+str(datetime.now().strftime("%H_%M_%S"))+".txt"
    f=open(name,"w")
    f.write(resText)
    f.close()
