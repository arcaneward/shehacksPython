def hangmanGame():
	print("Let's play a game of\nH   A   N   G   M   A   N")
	randomWord = input("Please choose a random word, player 1: ")
	beginGame(randomWord)

def beginGame(randomWord):
	numberLives = 5
	guessedLetters =[]
	
	print(numberLives)
	
	while numberLives == numberLives:
		currentGuess = input("Player 2, please guess a letter: ")
		
        # removes player life for incorrect guess
		numberLives -= 1
		print(numberLives)
		 if currentGuess not in guessedLetters and currentGuess in randomWord:
			print(numberLives)
			if currentGuess not in guessedLetters:
				guessedLetters.append(str(currentGuess))
			else:
				pass

            elif currentGuess not in randomWord:
			    numberLives -= 1
			print(numberLives)
			if currentGuess not in guessedLetters:
				currentGuess.append(str(currentGuess))
			else:
				pass

            elif currentGuess in guessedLetters:
			numberLives -= 1
			print(numberLives)
			if currentGuess not in guessedLetters:
				guessedLetters.append(str(currentGuess))
			else:
				pass

            # game over
            if numberLives == 0:
			gameOver(numberLives,randomWord)
