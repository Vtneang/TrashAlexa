# importing the pyttsx library 
import pyttsx3 
import speech_recognition as sr

# initialisation 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
	if voice.gender == 'VoiceGenderFemale' and voice.name == "Karen":
		engine.setProperty('voice', voice.id)
r = sr.Recognizer()
  
# testing
def commands(audio):
	if 'what time' in audio or 'current time' in audio:
		engine.say("The current time is right now you bitch")
	else:
		engine.say("Hello what's the next thing you wanna say")
	engine.runAndWait()

engine.say("Hello")
while True:
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		stuff = r.recognize_google(audio)
		print(stuff)
		commands(stuff)
	except:
		engine.say("Whoops what was that?")
		engine.runAndWait()

