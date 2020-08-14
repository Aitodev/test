from gtts import gTTS
from playsound import playsound

play = 'audio.mp3'
language = 'ru'

audio =  gTTS(text = "Привет Кирилл,Талаай, Умут, Данияр,Турат", lang = 'ru',slow = False)

audio.save(play)
playsound(audio)