from random import randint
file_reader = open("words.txt", "r")

#Get number of lines
def getLines():
    
    num_lines = sum(1 for line in open('words.txt'))
    return num_lines

def gameInfo(number_of_lines):
    #Name of the game
    print("\nWelcome to a game of Hangman!\n")

    #Displays number of words
    print("There are", getLines(), "different words")
    
    #Choose a difficulty
    difficulty = input("Choose your difficulty: \n 1 = Easy (4-6 characters)\n 2 = Medium (6-8 characters)\n 3 = Hard (8+ characters)\n")

    return int(difficulty)

#Gets random word
def random_Word(number_of_lines,difficulty):
    index = randint(0, number_of_lines)
    words = file_reader.readlines()
    word = words[index]
    wordLength = len(word)

    if(difficulty == 1):
        if(wordLength > 6):
            print ("Index : ", index)
            print ("Failed length: ", wordLength)
            random_Word(number_of_lines,difficulty)

    if(difficulty == 2):
        if(wordLength < 6 or wordLength > 8):
            print ("Index : ", index)
            print ("Failed length: ", wordLength)
            random_Word(number_of_lines,difficulty)

    if(difficulty == 3):
         if(wordLength < 8):
            print ("Index : ", index)
            print ("Failed length: ", wordLength)
            random_Word(number_of_lines,difficulty)

    print ("Index : ", index)
    return word

#Creates empty word the same length of secrect word 
def createEmptyWord(word):
    guessProgress = ""
    while (len(guessProgress) < ((len(word)-1)*2)):
        guessProgress += "_ "
    
    print ("Length of word: ", (len(word)-1))
    print ("Length of guessProgress: ", (len(guessProgress)))
    print (guessProgress)
    return guessProgress

#Checks of your guess has any matches in the secrect word
def matchCheck(emptyWord, guess, word):
    index = 0
    for letter in word:
        if(guess == letter):
            string_list = list(emptyWord)
            string_list[index] = guess
            emptyWord = "".join(string_list)
        index += 2
    print (emptyWord)
    return emptyWord        

#Prompts user for guesses and compares it to the secrect word
def playerGuesses(word, emptyWord):
    attempts = 8
    return guessPrompt(attempts,word,emptyWord)

    
   

def guessPrompt(attempts,word,emptyWord):

    newEmptyWord = emptyWord
    status = False

    while(attempts > 0):
        print("", attempts, " number of attempts left")
        guess = input("Make a guess, enter a letter: ")
    
        if(len(guess) > 1):
            print("Invalid input, limited to one letter")
            playerGuesses(word, newEmptyWord)
        else:
            newEmptyWord = matchCheck(newEmptyWord, guess, word)
            attempts -= 1
            guessPrompt(attempts,word,newEmptyWord)

        for letter in newEmptyWord:
            if(letter == "_"):
                status = False
            else:
                status = True
    return status

def gameStatus(status):
    playerStatus = ""
    if(status == True):
        playerStatus = "Congrats! You WON!!!"
    else:
        playerStatus = "Sorry... You lost try agin"

    return playerStatus 

#Function for the entire program
def startGame():
    #Gets number of lines
    number_of_lines = getLines()
    #Displays game info
    difficulty = gameInfo(number_of_lines)
    #Stores the random word in a variable
    word = random_Word(number_of_lines,difficulty)

    print("The secrect word is : ",word)
    #Creates an string that displays the un-guessed word
    emptyWord = createEmptyWord(word)
    #Returns true of false depending on if the player won the game
    status = playerGuesses(word, emptyWord)
    #Displays player game status
    gameStatus(status)

startGame()

