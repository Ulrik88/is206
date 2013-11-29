# This is the first room you can enter

import os
 
def start():
	os.system('cls') 
	print "\n\n Hmm so you pick this room. This room is rich of love."
	print "Wow, it seems that there is a beautiful lady here which really likes you."
	print "You have to make a move towards this beauty"
	print "\nType '1' if you want to kiss her"
	print "\nType '2' if you want to perform a robbery of the potential love of your life\n\n"
	answer = raw_input(">> ")
	if "1" in answer:
		os.system('cls')
		print "\n\nThe beautiful lady falls in love with you and offer you to spend a happy life with her for the rest of your life. YOU WIN!\n\n\n"
	elif "2" in answer:
		os.system('cls')
		print "\n\nYou continue to live an empty life with no passion which will torture your brain to the very bitter end. YOU LOOSE!\n\n\n"
	else:
		os.system('cls')
		print "\n\nOMG! That option didn't even exist. You loose your life. GAME OVER!\n\n\n"

start() 