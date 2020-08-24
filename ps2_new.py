import random
import string



def load_words():   # taken from the question(source:MIT-OCW)
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open("words.txt", 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):	#also taken from the question(source:MIT-OCW)   
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)







def dash():

	print("\n-----------------------\n\n")


'''def letter_in(letter,sequence):

	for i in sequence:		# we can use the membership test instead
					#The function checks if the letter is present in the sequence  
		if i==letter:
			return True

	return False	'''



def change_guess(letter,string,secret_word):
	''' This is a function to add a right letter to the blanks in partially guessed word
     	letter is the right letter 
	string is the partially guessed word  ''' 



	new_guess=""   					     

	secret_list=list(secret_word)

	for i in range (0,len(secret_word)):
		if letter==secret_list[i]:
			new_guess=new_guess+letter

		else:
			new_guess=new_guess+string[i]
			
	return new_guess




def show_matches(guess_word,wordlist):

	matches=[]

	for i in wordlist:
		check=''
		if len(i)==len(guess_word):
			k=0
			for j in guess_word:

				if j=='-':
					check=check+i[k]

				else:
					check=check+guess_word[k]

				k=k+1
		if i==check :
			matches.append(i)


	er=0
	a=''

	while er==0:

		print("There are",len(matches),"words matching ,do you want to see them ? , please enter y/n ")
		a=input()
		if a=='y' or a=='n':
			er=1
		if er==0:
			print("please enter only lowercase y or n") 

		

	if a=='y':
		print(matches)
		return True

	else:
		print("you\'ve saved your lifeline") 







#THE GAME STARTS FROM HERE

print("WELCOME TO THE GAME HANGMAN\n")

wordlist=load_words()

u=input("Do you want me to tell you the rules of the game? type \'y\' if YES \'n\' if NO")

if u=='y' or u=='Y':

	print("\t\tRULES OF THE GAME")

	print("\nI will first think of a word and will tell you only the size of it")

	print("You will have six guesses")

	print("If you guess a letter that is present in the secret word you will not lose a guess, the position/s of those letters in secret word will also be unveiled\n\n")

	print("if you guess the wrong letter(which is consonant) you will lose a guess")

	print("if you guess the wrong letter(which is vowel) you will lose two guesses\n\n")

	print("please do not enter characters other than the alphabets")

	print("Also do not repeat the guesses")

	print("In the above two cases you will be issued a warning")

	print("Only a maximum of three warnings will be issued after which one guess will be deducted\n\n")

	print("The game ends either when you guess all the letters in the word or when you run out of your guesses\n\n\n")

	print("\t\t LIFELINE\n")
	
	print("You even have a lifeline i.e. if you enter '*' as your guess letter")
	
	print("you can avail it only if you have already guessed atleast one right letter")

	print("when you avail the lifeline i will show you the number of matching words that are available  ")

	print("And again ask you if you want me to display all the matching words")

	print("if you type 'y' i will display all the words and your only lifeline will be cut")

	print("whereas if you type 'n' i shall not display them and your lifeline is also saved\n\n\n") 
	

	 

elif u=='n' or u=='N':

	print("\nhope you know the rules then let us start the game\n\n\n")

else:

	print("please enter only \'y\' or \'n\'")	




vowels="aeiou"
					#just for later use
alphabets="abcdefghijklmnopqrstuvwxyz"





secret_word=choose_word(wordlist)
					#choosing the word and also converting it into a set
secret_set=set(secret_word)





available_letters=list("abcdefghijklmnopqrstuvwxyz")

guess_no=6							#These three variables may be subsequently changed in the loop

warn_no=3

lifeline=1




guess_word=""

for i in range(0,len(secret_word)):	
	guess_word=guess_word+'-'


iguess_word=guess_word




print("I have a",len(secret_word),"lettered word in my mind.\n")

dash()





while guess_no>0 and guess_word!=secret_word:

	print("you have",guess_no,"guesses\n")

	print("Remaining letters are ",''.join(available_letters),"\n")

	guess=(input("please enter your guess:")).lower()





	if guess in available_letters :

		available_letters.remove(guess)



		if guess in secret_set:	
						
			guess_word=change_guess(guess,guess_word,secret_word)				

			print("Great Guess:",guess_word)
						



		else :
			print("sorry it is not there in the secret word\n")

			if guess in vowels:
		
				guess_no=guess_no-2

			else:
				guess_no=guess_no-1

			print(guess_word)





		dash()






	elif guess in alphabets:

		if warn_no>0:

			warn_no=warn_no-1

		else:

			guess_no=guess_no-1			

		print("wrong you've already guessed this letter")

		print("you have",warn_no,"warnings left")

		print(guess_word)

		dash()



			


	


	else:

		if guess=='*':
		
			if lifeline>0 and guess_word!=iguess_word:
				print("The possible matches are:")
				if show_matches(guess_word,wordlist):
					lifeline=lifeline-1

			elif guess_word==iguess_word:
				print("sorry you cannot use the lifeline now since you haven't even guessed one right letter")
			
			
			else:
				print("sorry your lifelines are over")

			dash()


		else:
			if warn_no>0:

				warn_no=warn_no-1

			else:

				guess_no=guess_no-1			

			print("wrong you've entered invalid character")

			print("you have",warn_no,"warnings left")

			print(guess_word)

			dash()






if(guess_no<=0):
	print("sorry you ran out of your guesses.The word is:",secret_word)
else:

	print("congrats you have successfully cracked the word. your score is:",guess_no*len(secret_set))






