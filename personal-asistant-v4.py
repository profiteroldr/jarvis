import os
import random
from playsound import playsound
from gtts import gTTS

def speak(string):
    tts = gTTS(string, lang="tr")
    rand = random.randint(1,1000)
    file = "ses" + str(rand) + ".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("merhaba")