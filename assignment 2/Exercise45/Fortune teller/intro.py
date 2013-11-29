# Start of the game

import os # so that I can use the clear screen function later

		
 
def intro():
	print "\n\nHi and welcome to Fortune teller. This game is compatible only with the windows OS" 
	print "This is a game where you play a treasure hunter."
	print "You have been searching for a life changing treasure on the seven seas for years"
	print "You are now getting tired and feels lonely for some reason \n \n"
	name = raw_input("Choose a name and press ENTER. >> ")
	os.system('cls') # clears the screen
	
	print "\n\nHi", name, "I've been following your grief for some time now."
	print "I may have a couple of solutions for your empty life which can help you in achieving the life of your dreams."
	print "Well since this is a text based reality it can be a little hard for you to understand."
	print "As a special one I will be able to tell you that the outcome of the solution depends of a choice you make between the two doors in front of you"
	print "You will only be able to choose one of the two doors. Now, make your choice."
	print "\nType 1 or 2 in order to make a choice. Then push ENTER."
	
	choice = raw_input(">> ")
	if choice == "1":
		import roomonefile # imports Room 1 in which is in a separate file
	elif choice == "2":
		import roomtwofile # imports Room 2
	else:
		os.system('cls') 
		print "\n\n Your incompetence lead to your death \n\n\n Game over! \n\n\n"
		
		

	
intro()

 

 

