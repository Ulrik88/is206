# This is the second room you can enter

import os


def start():
	os.system('cls') 
	print "\n\nYou are now in the secret of chambers"
	print "The master of secret of chambers ask you a question."
	print "Are you an evil pirate?\n\n" 
	
	answer = raw_input("Type your answer here> ")
	if "no" in answer:
		os.system('cls')
		print "\n\nThat is correct! You will live a happy life with the secret of chambers bless. \n\n\n Game over!\n\n\n"
	else:
		os.system('cls')
		print "\n\nWrong answer.. You will never be a candidate to join the secret of chambers ... \n\n\n Game over! \n\n\n"

start() 