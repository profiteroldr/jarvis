import os
import random
from turtle import back
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr

# Metinden -> Konuşmaya
def speak(string):
    tts = gTTS(string, lang="tr") # Sese dönüştürülecek metin eklendi.
    rand = random.randint(1,1000) # Sese dönüştürülecek metinin mp3 dosya adı oluşturuldu.
    file = "ses" + str(rand) + ".mp3" # Sese dönüştürülecek metinin mp3 dosya adı tanımlandı.
    tts.save(file) # Ses dsoyası kaydedildi.
    playsound(file) # Ses dosyası oynatıldı.
    os.remove(file) # Ses dosyası silindi.

# Konuşmadan -> Metine
def record():
    r = sr.Recognizer() # "r" adlı bir tanımlayıcı oluşturuldu.
    with sr.Microphone() as source: # "source" adlı kaynak mikrofon olarak tanımlandı.
        voice = r.listen(source) # sourceden yani mikrofondan gelen sesin tanımlayıcı ile dinlenmesi sağlandı. "voice" üzerine atandı.
        try:
            audio = r.recognize_google(voice, language="tr-TR") # Metine döünüştürülecek ses dosyası (voice) ve sesin dili "audio" üzerine tanımlandı. 
        
        # Karşılaşabilinecek Hatalar
        except sr.UnknownValueError: # Ses dosyasında söylenenlerin anlaşılamadığı zaman verilen hata.
            speak("Üzgünüm anlayamadım. Lütfen tekrar söyler misin?") # Hata sonucu kullanıcıya bildirim.
            return record() # Yeniden kullanıcının dinlenmesi amacı ile yazılan kod.
        
        except sr.WaitTimeoutError: # Kullanıcının asistanı fazla bekletmesi ya da konuşmamasından kaynaklanan hata.
            speak("Üzgünüm seni duyamadım. Lütfen tekrar söyler misin?") # Hata sonucu kullanıcıya bildirim.
            return record() # Yeniden kullanıcının dinlenmesi amacı ile yazılan kod.
        
        except sr.RequestError: # Tanımlanmayan olası hatalar.
            speak("Üzgünüm sistem çalışmıyor.") # Hata sonucu kullanıcıya bildirim.

        return audio # Herhangi bir hata ile karşılaşılmadığında "audio" ile elde edilen metin dışarı çıkartılır.

a=1
while a:
    b=1
    while b:
        girdi_1 = record()
        if girdi_1 == "Jarvis":
            b=0
        else:
            b=1

    speak("Merhaba Patron seni dinliyorum.")
    girdi = record()
    speak(girdi)
    a = 0