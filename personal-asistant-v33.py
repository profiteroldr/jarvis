import os
import random
from turtle import back
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
from selenium import webdriver
import webbrowser
import subprocess as sp
import datetime
import locale
import sys
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

speak("Merhaba Patron seni dinliyorum.") # Sistemin başladığını ve çalıştığına dair ön komut.

def jarvis():
    # Döngü 2
    b=1
    while b: # b=1 olduğu sürece çalışacaktır.
        girdi_1 = startJarvis() # Kullanıcıdan ses alıyoruz.
        if girdi_1 == "Jarvis": # Kullanıcı eğer "Jarvis" derse b=0 olacak, "Döngü 2" kırılacak sonraki "Döngü 1" içindeki fonksiyon olan speak() çalışacak.
            b=0
        else: # Kullanıcı eğer "Jarvis" demez ise b=1 olarak atanacak ve döngü b=0 olana kadar yani "Jarvis" kelimesi söylenene kadar tekrarlanacak.
            b=1
    # Döngü 2 Bitti

def run():
    # Döngü 1
    a=1
    while a: # a=1 olduğu sürece kod çalışcaktır.
        
        jarvis() # "Döngü 2"in çalıştırılmasını sağlıyor

        speak("Patron") # "Döngü 2"nin kırıldığını ve sistemin kullanıcıyı dinlediğine dair ön bildirim. "Döngü 2" kırıldığında çalışacak bir komuttur.

        girdi = record() # Kullanıcı komut söyleyecek.
        girdi.lower()
        speak(girdi) # Kullanıcının söylediği komut metine çevrilip tekrar asistan tarafından söyletilecek.
        
        if girdi == "Google": # Uygulama Açma Yönetm: 1
            url = "www.google.com"
            brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" # Brave tarayıcının yolu.
            webbrowser.register("brave", None, webbrowser.BackgroundBrowser(brave_path)) # brave_path'in Brave adlı bir tarayıcı olduğunu, "brave" kavramı ile Brave taryıcısını kullaanacağımzı ve yolunun bu olduğunu belirttik.
            webbrowser.get("brave").open_new(url) # Belirtilen linki brave_path'te bulunan "brave" kavramını kullanarak, Brave taryıcısına açtırdık.
        
        elif girdi == "YouTube": # Uygulama Açma Yönetm: 1
            url = "www.youtube.com"
            brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" # Brave tarayıcının yolu.
            webbrowser.register("brave", None, webbrowser.BackgroundBrowser(brave_path)) # brave_path'in Brave adlı bir tarayıcı olduğunu, "brave" kavramı ile Brave taryıcısını kullaanacağımzı ve yolunun bu olduğunu belirttik.
            webbrowser.get("brave").open_new(url) # Belirtilen linki brave_path'te bulunan "brave" kavramını kullanarak, Brave taryıcısına açtırdık.
        
        elif girdi == "Facebook": # Uygulama Açma Yönetm: 2
            # Çözümü: https://www.geeksforgeeks.org/python-script-to-open-a-web-browser/?ref=rp
            url = "www.facebook.com"
            brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" # Brave tarayıcının yolu.
            webbrowser.register("brave", None, webbrowser.BackgroundBrowser(brave_path)) # brave_path'in Brave adlı bir tarayıcı olduğunu, "brave" kavramı ile Brave taryıcısını kullaanacağımzı ve yolunun bu olduğunu belirttik.
            webbrowser.get("brave").open_new(url) # Belirtilen linki brave_path'te bulunan "brave" kavramını kullanarak, Brave taryıcısına açtırdık.
        
        elif girdi == "saat":
            locale.setlocale(locale.LC_ALL, '')
            saat = datetime.datetime.now()
            tarih = datetime.datetime.strftime(saat, "%X") # tam saat bilgisi
            speak(tarih)
        
        elif girdi == "hafta":
            locale.setlocale(locale.LC_ALL, '')
            hafta_gun = datetime.datetime.now()
            tarih = datetime.datetime.strftime(hafta_gun, "%A") # hafta gününün tam adı
            speak(tarih)
        
        elif girdi == "ay":
            locale.setlocale(locale.LC_ALL, '')
            ay = datetime.datetime.now()
            tarih = datetime.datetime.strftime(ay, "%B") # ayın tam adı
            speak(tarih)
        
        elif girdi == "tarih":
            locale.setlocale(locale.LC_ALL, '')
            tam1_tarih = datetime.datetime.now()
            tarih = datetime.datetime.strftime(tam1_tarih, "%x") # tarih bilgisi
            speak(tarih)
        
        elif girdi == "tam tarih":
            locale.setlocale(locale.LC_ALL, '')
            tam2_tarih = datetime.datetime.now()
            tarih = datetime.datetime.strftime(tam2_tarih, "%c") # tam tarih bilgisi (yani saat bilgisi eklenmiş hali)
            speak(tarih)
        
        elif "orada mısın" in girdi or "Orada mısın" in girdi: # Komutun içinde belirtilen kelime(ler) geçerse çalışacak bir komut.
            speak("Buradayım patron.")
        
        elif girdi == "çıkış": # Sesli asistanı kapatmaya yarıyor.
            sys.exit()
            # sys.exit() yerine break kullanılabilir.
        a = 1 # "Döngü 1" kırılmayacak ve devam edecek.

    # "Döngü 1" devam edecek ve baştan başlayacak yani "Döngü 2"ye gelecek. "Döngü 2" kırılmadığı sürece sistem devam etmeyecektir. "Döngü 2" kırıldığında işlem tekrarlanacak.
    # Döngü 1 Bitti

run() # "Döngü 1"in çalıştırılmasını sağlıyor