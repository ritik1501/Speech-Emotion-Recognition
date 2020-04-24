import speech_recognition as sr
import pyttsx3

filename="test.wav"
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    
    audio_data = r.record(source)
    
    text = r.recognize_google(audio_data)
    # print(text)

stext=text.split(" ")
print(stext)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

user_input=input("Enter the word to be searched: ")
user_range=input("Enter the word till you want to listen: ")

for ind,x in enumerate(stext):
    if x==user_range:
        z=ind


l=[]
for index,i in enumerate(stext):
    if i==user_input:
        l=stext[index:(z+1)]
print(l)
        
user_str= ""
for x in l:
    user_str+=x
speak(user_str)        

