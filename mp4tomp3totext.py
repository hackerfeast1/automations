import speech_recognition as sr
from pydub import AudioSegment

#Conversion of video to audio
AudioSegment.from_file("path_to_video").export("output.mp3", format="mp3")

# Getting the audio from output.mp3
sound = AudioSegment.from_mp3("output.mp3")

# Converting the audio file to wav format
audio_file = "transcript.wav"
sound.export(audio_file, format="wav")

# Setting up the recognizer
r = sr.Recognizer()

# Recognize text from source with help of google
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
    
text = r.recognize_google(audio)
print(text)

with open("transcript.txt", "w") as F:
    F.write(text)
F.close()
