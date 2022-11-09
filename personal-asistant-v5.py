import os
import random
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr

def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        voice = r.listen(source)
        try:
            audio = r.recognize_google(voice, language="tr-TR")
        except sr.UnknownValueError:
            speak("Üzgünüm anlayamadım. Lütfen tekrar söyler misin?")
            return record()
        except sr.RequestError:
            speak("Üzgünüm sistem çalışmıyor.")
        except sr.WaitTimeoutError:
            speak("Üzgünüm seni duyamadım. Lütfen tekrar söyler misin?")
            return record()
        return audio

def speak(string):
    tts = gTTS(string, lang="tr")
    rand = random.randint(1,1000)
    file = "ses" + str(rand) + ".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("merhaba")
girdi = record()
print(girdi)