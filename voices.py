import pyttsx3
import time
engine = pyttsx3.init()
voices = engine.getProperty('voices')
ppl = ["Karen", "Daniel", "Fiona"]
for voice in voices:
	if voice.name in ppl:
		voice.rate = 175
		engine.setProperty('voice', voice.id)
		print(voice)
		engine.say("Hello world my name is " + voice.name)
		engine.say("The weather ouside is pretty warm compared to Berkeley")
		engine.say("Ohhh so it wasn't a good day today was it...")
		engine.runAndWait()

#Daniel - GB
#Fiona - Scotland
#Karen - Aussie
#Kyoko - jap
#Melina - el_Gr
#Tessa - en_Za
#Ting=ting = zh
#Veena - en_in
#yuna - korean
#Yuri - russian