#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr






#Look through string, find first string that looks like int and returns as int
def fetchFirstInt(string):
	dlist = string.split()
	for stre in dlist:
		if stre.isdigit():
			return int(stre)
	return False



#return string from audio recording (MUST HAVE WI-FI OR ELSE)
def getListen(recognizer):
	with sr.Microphone() as source:
		audio = recognizer.listen(source)
	try:
		return recognizer.recognize_google(audio)
	except sr.UnknownValueError:
		return ":("
	except sr.RequestError:
		return ">:("

#fill list with specific value num times
def fill(arr, num, val):
	for i in range(num):
		arr.append(val)


#OR check, stringMatch("and", ["and", "two"]) -> true 
def stringMatch(string, list2):
	for stre in list2:
		if stre in string:
			return True
	return False


#AND CHECK, stringMatch("and", ["and, "two"]) -> false
def stringMatchAll(string, list2):
	DECISIONOFALIFETIMEPLEASEHELPME = False
	for stre in list2:
		if stre in string:
			DECISIONOFALIFETIMEPLEASEHELPME = True
		else:
			DECISIONOFALIFETIMEPLEASEHELPME = False		

	return DECISIONOFALIFETIMEPLEASEHELPME
 
	
		


#util check for multiple yes/no 
def yesNoVerify(recognizer):
	result = getListen(recognizer)
	if stringMatch(result, ["yes", "yeah", "definitely", "totally"]):
		return True
	elif stringMatch(result, ["no", "nah", "nope"]):
		return False
	else:
		print("Invalid voice input, please try again!")
		yesNoVerify(recognizer)
	
	

#please.. im sorry.. this is a monster
def resultCheckOR(recognizer, keys, funcs, params):
	fill(params, len(funcs) - len(params), [])
	result = getListen(recognizer)
	for i, keylist in enumerate(keys):
		for key in keylist:
			if stringMatch(result, key):
				return funcs[i](*params[i])	
	print("Invalid voice input, please retry.")
	resultCheck(recognizer, keys, funcs, params)
	
#ALL OF THIS IS A MONSTER
def resultCheckAND(recognizer, keys, funcs, params):
	fill(params, len(funcs) - len(params), [])
	result = getListen(recognizer)
	for i, keylist in enumerate(keys):
		for key in keylist:
			if stringMatchAll(result, key):
				return funcs[i](*params[i])	
	print("Invalid voice input, please retry.")
	resultCheck(recognizer, keys, funcs, params)
#ASHWIN MADE ME MAKE THIS MONSTER
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
