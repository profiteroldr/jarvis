import gtts
import speech_recognition as sr
from playsound import playsound

ses = gtts.gTTS("Merhaba patron!", lang="tr")

ses.save("giris.mp3")

playsound("giris.mp3")