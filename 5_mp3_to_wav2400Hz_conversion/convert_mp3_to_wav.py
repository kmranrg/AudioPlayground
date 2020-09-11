# pip install pydub
# sudo apt-get install ffmpeg


from os import path
from pydub import AudioSegment

# files                                                                         
src = "welcome.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
