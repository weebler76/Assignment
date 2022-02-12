# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Jonathan Devlin   
# Creation Date: 2/11/2002
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
#To many 's
	print("You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendlycand willshare his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.")
	print()

def chooseCave():
    cave = ''
#unnecessary while loop
#Corrected tabs/spaces
    
    print('Which cave will you go into? (1 or 2)')
    cave = input()
    

#caves in following line should be cave
    return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
    #sleep is set for 3 seconds
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
    #Missing parentheses
		print ('Gobbles you down in one bite!')

playAgain = 'yes'
#= in following line should be ==
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
#choosecave should be chooseCave
	caveNumber = chooseCave()
	checkCave(caveNumber)
#combined print and input lines
	playAgain =input('Do you want to play again? (yes or no)')
	
	if playAgain == "no":
    #planing should be playing
		print("Thanks for planing")
