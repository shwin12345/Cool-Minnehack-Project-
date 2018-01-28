#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr






def getListen(recognizer):
	with sr.Microphone() as source:
		audio = recognizer.listen(source)
	try:
		return recognizer.recognize_google(audio)
	except sr.UnknownValueError:
		return ":("
	except sr.RequestError:
		return ">:("
   
def stringMatch(string, list2):
	for stre in list2:
		if stre in string:
			return True
	return False 

def yesNoVerify(recognizer):
	result = getListen(recognizer)
	if stringMatch(result, ["yes", "yeah", "definitely", "totally"]):
		return 1
	elif stringMatch(result, ["no", "nah", "nope"]):
		return 0
	else:
		return 2
	

def resultCheck(recognizer, keys, funcs, params):
	result = getListen(recognizer)
	for i, keylist in enumerate(keys):
		for key in keylist:
			if stringMatch(result, key):
				funcs[i](*params[i])
				return	






def noHeadache():
	print("You have no headache? Great!")


def headache():
	print("Oh! You have a headache :(")



r = sr.Recognizer()



print("Do you have a headache?")
resultCheck(r, [
	["yeah", "yes"],
	["no", "nah", "nope"]
], [headache, noHeadache], [
[], 
[]
])



	
	
