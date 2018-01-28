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

def fill(arr, num, val):
	for i in range(num):
		params.append(val)



def stringMatch(string, list2):
	for stre in list2:
		if stre in string:
			return True
	return False


   
def stringMatchAll(string, list2):
	DECISIONOFALIFETIMEPLEASEHELPME = False
	for stre in list2:
		if stre in string:
			DECISIONOFALIFETIMEPLEASEHELPME = True
		else:
			DECISIONOFALIFETIMEPLEASEHELPME = False		

	return DECISIONOFALIFETIMEPLEASEHELPME
 
	
		



def yesNoVerify(recognizer):
	result = getListen(recognizer)
	if stringMatch(result, ["yes", "yeah", "definitely", "totally"]):
		return True
	elif stringMatch(result, ["no", "nah", "nope"]):
		return False
	else:
		print("Invalid voice input, please try again!")
		yesNoVerify(recognizer)
	
	


def resultCheckOR(recognizer, keys, funcs, params):
	fill(params, len(funcs) - len(params), [])
	result = getListen(recognizer)
	for i, keylist in enumerate(keys):
		for key in keylist:
			if stringMatch(result, key):
				return funcs[i](*params[i])	
	print("Invalid voice input, please retry.")
	resultCheck(recognizer, keys, funcs, params)
	

def resultCheckAND(recognizer, keys, funcs, params):
	fill(params, len(funcs) - len(params), [])
	result = getListen(recognizer)
	for i, keylist in enumerate(keys):
		for key in keylist:
			if stringMatchAll(result, key):
				return funcs[i](*params[i])	
	print("Invalid voice input, please retry.")
	resultCheck(recognizer, keys, funcs, params)

def resultCheckANDOR(recognizer, keyANDList, keyOR, funcs, ANDParamList, ORParamaList):
	result = getListen(recognizer)
	for i, keylist in enumerate(keyANDList):
		for key in keylist:
			if stringMatchAll(result, keylist):
				return funcs[i](*ANDParamList[i])
			elif stringMatch(result, keyOR[i]):
				return funcs[i](*ORParamaList[i])
	print("Invalid voice input, please retry.")
	resultCheckANDOR(recognizer, keyANDList, keyOR, funcs, ANDParamList, ORParamaList)
	


	


def noHeadache():
	print("You have no headache? Great!")
	return False


def headache():
	print("Oh! You have a headache :(")
	return True



r = sr.Recognizer()



print("Do you have a headache?")
boo = resultCheckOR(r, [
	["yeah", "yes"],
	["no", "nah", "nope"]
], [headache, noHeadache], [])

if boo:
	print("Headache check!")








	
	
