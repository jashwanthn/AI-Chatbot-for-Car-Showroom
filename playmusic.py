from playsound import playsound
from gtts import gTTs

def playautio(audio):
    playsound(audio)

def convert_to_audio(mp3):
    audio = gTTs(mp3)
    audio.save("myaudio.mp3")
    playaudio("myaudio.mp3")

mp3=("hello my name is charan")
