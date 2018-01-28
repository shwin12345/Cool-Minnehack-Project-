#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from util import *







	
def noHeadache():
	print("You have no headache? Great!")
	return False


def headache():
	print("Oh! You have a headache :(")
	return True



r = sr.Recognizer()


#print(stringMatchAll("yeah yes", ["yeah", "yes"]))


#print("Do you have a headache?")
#boo = resultCheckAND(r, [
#	["yeah", "yes"],
#	["no", "nah", "nope"]
#], [headache, noHeadache], [[], []])



#if boo:
	#print("Headache check!")

I_AM_GOD = resultCheckANDOR(r, 
	[["head", "hurts"]],
        [["headache"]],
	[headache],
	[[]],
	[[]]
)

print(I_AM_GOD)



print("I AM GOD")
print(getListen(r))






	
	
