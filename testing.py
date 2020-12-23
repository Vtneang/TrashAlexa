# importing the pyttsx library 
import pyttsx3 
import speech_recognition as sr
import time

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
		checktime()
	else:
		engine.say("Sorry I don't know what to do...")
	engine.runAndWait()

#Commands
def checktime():
	saying = "The current time is "
	t = time.localtime()
	current = time.strftime("%H, %M", t)
	saying += current[0:2]
	saying += current[3:6]
	if int(current[0:2]) < 12 or int(current[0:2]) == 24:
		saying += " am"
	else:
		saying += " pm"
	engine.say(saying)

while True:
	with sr.Microphone() as source:
		audio = r.listen(source)
		print("got it")
	try:
		stuff = r.recognize_google(audio)
		print(stuff)
		commands(stuff)
	except:
		engine.say("Whoops what was that?")
		engine.runAndWait()

