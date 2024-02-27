# Voice Recorde in python
# pip install sounddevice

import sounddevice
from scipy.io.wavfile import write

fs=44100
#Ask to enter the recording time
second = int(input("Enter the recording time in second:"))
print("Recording...\n")
record_voice = sounddevice.rec(int(second * fs), samplerate=fs,channels=2)
sounddevice.wait()
write("Myrecording.wav",fs,record_voice)
print("Recording is done Please chek you folderrr to listen recording.")