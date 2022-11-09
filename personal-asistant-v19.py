import os
import random
from turtle import back
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
from selenium import webdriver
import webbrowser
import subprocess as sp
# playsound hatası düzeltmek için --> pip install playsound==1.2.2


# Metinden -> Konuşmaya
def speak(string):
    tts = gTTS(string, lang="tr") # Sese dönüştürülecek metin eklendi.
    rand = random.randint(1,1000) # Sese dönüştürülecek metinin mp3 dosya adı oluşturuldu.
    file = "ses" + str(rand) + ".mp3" # Sese dönüştürülecek metinin mp3 dosya adı tanımlandı.
    tts.save(file) # Ses dsoyası kaydedildi.
    playsound(file) # Ses dosyası oynatıldı.
    os.remove(file) # Ses dosyası silindi.
    return file

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

# Konuşmadan -> Metine (Jarvis Başlatmak için)
def startJarvis():
    r = sr.Recognizer() # "r" adlı bir tanımlayıcı oluşturuldu.
    with sr.Microphone() as source: # "source" adlı kaynak mikrofon olarak tanımlandı.
        voice = r.listen(source) # sourceden yani mikrofondan gelen sesin tanımlayıcı ile dinlenmesi sağlandı. "voice" üzerine atandı.
        try:
            audio = r.recognize_google(voice, language="tr-TR") # Metine döünüştürülecek ses dosyası (voice) ve sesin dili "audio" üzerine tanımlandı. 
        
        # Karşılaşabilinecek Hatalar
        except sr.UnknownValueError: # Ses dosyasında söylenenlerin anlaşılamadığı zaman verilen hata.
            print("Patron bana mı seslendin?") # Hata sonucu kullanıcıya bildirim.
            return startJarvis() # Yeniden kullanıcının dinlenmesi amacı ile yazılan kod.
        
        except sr.WaitTimeoutError: # Kullanıcının asistanı fazla bekletmesi ya da konuşmamasından kaynaklanan hata.
            print("Senin için burada bekliyorum.") # Hata sonucu kullanıcıya bildirim.
            return startJarvis() # Yeniden kullanıcının dinlenmesi amacı ile yazılan kod.
        
        except sr.RequestError: # Tanımlanmayan olası hatalar.
            print("Üzgünüm sistem çalışmıyor.") # Hata sonucu kullanıcıya bildirim.

        return audio # Herhangi bir hata ile karşılaşılmadığında "audio" ile elde edilen metin dışarı çıkartılır.

# Döngü 1
a=1
while a: # a=1 olduğu sürece kod çalışcaktır.
    
    # Döngü 2
    b=1
    while b: # b=1 olduğu sürece çalışacaktır.
        girdi_1 = startJarvis() # Kullanıcıdan ses alıyoruz.
        if girdi_1 == "Jarvis": # Kullanıcı eğer "Jarvis" derse b=0 olacak, "Döngü 2" kırılacak sonraki "Döngü 1" içindeki fonksiyon olan speak() çalışacak.
            b=0
        else: # Kullanıcı eğer "Jarvis" demez ise b=1 olarak atanacak ve döngü b=0 olana kadar yani "Jarvis" kelimesi söylenene kadar tekrarlanacak.
            b=1

    speak("Merhaba Patron seni dinliyorum.") # "Döngü 2" kırıldığında çalışacak kod.
    girdi = record() # Kullanıcı komut söyleyecek.
    speak(girdi) # Kullanıcının söylediği komut metine çevrilip tekrar asistan tarafından söyletilecek.
    if girdi == "Google":
        chrome_path_driver = "D:\Python Projeler\Drivers\chromedriver"
        website = webdriver.Chrome(executable_path=chrome_path_driver)
        website.get("https://www.google.com/")
        # Üste bulunan ksımın yanlamasına yazılışı: webdriver.Chrome("D:\Python Projeler\Drivers\chromedriver").get("https://www.google.com/")
    elif girdi == "YouTube":
        chrome_path_driver = "D:\Python Projeler\Drivers\chromedriver"
        website = webdriver.Chrome(executable_path=chrome_path_driver)
        website.get("https://www.youtube.com/")
    elif girdi == "Facebook":
        url = "www.facebook.com"
        chrome_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        webbrowser.get(chrome_path).open_new(url)
    a = 1 # "Döngü 1" kırılmayacak ve devam edecek.
