import os
import random
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr

# Metinden -> Konuşmaya
def speak(string):
    tts = gTTS(string, lang="tr")
    rand = random.randint(1,1000)
    file = "ses" + str(rand) + ".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

# Konuşmadan -> Metine
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



speak("merhaba")
girdi = record()
print(girdi)