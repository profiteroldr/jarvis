import gtts
import speech_recognition as sr
from playsound import playsound

ses = gtts.gTTS("Merhaba", lang="tr")

ses.save("hello.mp3")

playsound("hello.mp3")