# Author: Quintin Nguyen
# Date: 04.03.19
# E-mail: quintintnguyen@gmail.com
# Description: Hawaiian Project, show the pronunciation of Hawaiian words

# Global Characters
CONSONANTS = ["h", "k", "l", "m", "n", "p", "w", "'", "H", "K", "L", "M", "N", "P", "W"]
VOWELS = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
COMPLEX_VOWELS = ["ai", "ae", "ao", "au", "ei", "eu", "iu", "oi", "ou", "ui"]

# Global vowel sounds
VOWEL_SOUNDS = ["ah", "eh", "ee", "oh", "oo"]
VOWEL_PAIR_SOUNDS = ["eye", "eye", "ow", "ow", "ay", "eh-oo", "ew", "oy", "ow", "ooey"]

# Global Choices
ANSWERS = ["y", "yes", "n", "no"]
CONTINUE = "Do you want to enter another word?"

def getHawaiianPhrase():

    global phrase
    VALID_VOWEL = False
    VALID_LETTER = False
    # Determine if phrase is valid
    while not VALID_VOWEL and not VALID_LETTER:
        phrase = input("Enter a Hawaiian phrase to pronounciate: ")
        VOWEL_END_CHECK = phrase.split(" ")
        INVALID_VOWEL = []
        INVALID_CHAR = []
        SANITY_CHECK = 0 # SANITY_CHECK makes sure that booleans that are flagged as false do not turn t\
                         # rue when code is re-iterated.

# This segment of code checks if words end in a vowel

        i = 0
        # Determine if the phrase ends in a vowel
        while i < len(VOWEL_END_CHECK):

            word = VOWEL_END_CHECK[i]

            index = 0

            # Iterates through each individual word in string
            while index < len(word):
                char = word[index]
                lastIndex = len(word) - 1

                if index == lastIndex:

                    # Compares the last character in each word
                    if char not in VOWELS:
                        INVALID_VOWEL.append(word)
                        VALID_VOWEL = False
                        SANITY_CHECK += 1
                    else:
                        VALID_VOWEL = True

                index += 1

            i += 1

        # Print invalid words that don't end in a vowel
        i = 0
        while i < len(INVALID_VOWEL):
            word = INVALID_VOWEL[i]
            print("The word ", word, " does not end in a vowel")
            i += 1

# This segment of code checks for invalid letters in phrase

        charCheck = phrase.strip()
        charCheck = phrase.split(" ")
        i = 0
        # Checks for invalid characters || iterates through each word in phrase
        while i < len(charCheck):

            word = charCheck[i]

            index = 0
            # Check for valid char in each word of phrase
            while index < len(word):

                char = word[index]

                if char not in VOWELS and char not in CONSONANTS:
                    INVALID_CHAR.append(char)
                    VALID_LETTER = False
                    SANITY_CHECK += 1
                else:
                    VALID_LETTER = True

                index += 1

            i += 1

        # Print invalid characters

        i = 0
        while i < len(INVALID_CHAR):
            char = INVALID_CHAR[i]
            print("The letter ", char, " is not valid")
            i += 1

        # Final check if phrase is still valid
        if VALID_LETTER == False or VALID_VOWEL == False or SANITY_CHECK > 0:
            VALID_LETTER = False
            VALID_VOWEL = False

    phrase = phrase.split(" ")
    return phrase

# Function finds a word that "w" exists in
def getWordW(string):

    # SANITY_CHECK ensures that there are no "w's" in the word
    SANITY_CHECK = 0

    i = 1
    # Iterate through string to find a W
    while i < len(string):

        char = string[i]
        if char == "w" or char == "W":
            SANITY_CHECK = 1
            return True

        i += 1

    if SANITY_CHECK == 0:
        return False

# Function finds the index of the word that "w" exists in
def getIndexW(string):

    i = 1
    # Iterate through string to find a W
    while i < len(string):
        char = string[i]
        if char == "w" or char == "W":
            return i
        i += 1

def pronounceW(word, index):

    VLetters = ["a", "e", "i", "A", "E", "I"]
    indexV = index - 1
    VChar = word[indexV]

    if VChar in VLetters:
        return "v"

    if VChar not in VLetters:
        return "w"

# Function splits strings into lists
def turnStringIntoList(string):

    splitWord = []

    i = 0
    # Iterates through each char of string and index's it to a list
    while i < len(string):
        char = string[i]
        splitWord.append(char)
        i += 1

    return splitWord

def simpleVowel(letter):

    string = ""

    if letter == "a":
        string = "ah-"

    if letter == "e":
        string = "eh-"

    if letter == "i":
        string = "ee-"

    if letter == "o":
        string = "oh-"

    if letter == "u":
        string = "oo-"

    return string

def complexVowel(vowels):
    string = ""

    if vowels == "ai" or vowels == "ae":
        string = "eye-"

    if vowels == "ao" or vowels == "au":
        string = "ow-"

    if vowels == "ei":
        string = "ay-"

    if vowels == "eu":
        string = "eh-oo-"

    if vowels == "iu":
        string = "ew-"

    if vowels == "oi":
        string = "oy-"

    if vowels == "ou":
        string = "ow-"

    if vowels == "ui":
        string = "ooey-"

    return string

def pronounceWord(word):

    word = word.lower()
    wordIndex = len(word)
    word += "   "  # Increase index size of word so that the program can evaluate each char without causing an error
    pronounce = ""

    i = 0
    #Pronounce the word!!! Find the proper vowel sounds
    while i < wordIndex:

        a = i + 1
        b = i + 3
        c = i + 2
        SANITY_CHECK = 0  # Make sure to not pronounce the same vowels

        char = word[i]
        complexVowelCheck = word[a:b]  # The first 2 characters ahead of index
        simpleVowelCheck = word[a]  # The first character ahead of index
        vowelCheck = word[i:c]  # This is the char at index and char after it

        if char in CONSONANTS:
            pronounce += char  # Appends a consonant to the pronounciation

            if complexVowelCheck in COMPLEX_VOWELS:  # Checks if there is a complex vowel to pronounce
                doubleVowelSound = complexVowel(complexVowelCheck)  # Finds proper pronounciation for complex vowel
                pronounce += doubleVowelSound
                SANITY_CHECK = 1
                i += 3

            if simpleVowelCheck in VOWELS and SANITY_CHECK == 0:
                singleVowelSound = simpleVowel(simpleVowelCheck)  # Finds a simple vowel to pronounce
                pronounce += singleVowelSound  # Adds the pronounciation to string

                i += 2

        SANITY_CHECK = 0

        if char in VOWELS:

            if vowelCheck in COMPLEX_VOWELS:
                doubleVowelSound = complexVowel(vowelCheck) # Checks if there is a complex vowel to pronounce
                pronounce += doubleVowelSound
                SANITY_CHECK = 1
                i += 2

            if char in VOWELS and SANITY_CHECK == 0:
                singleVowelSound = simpleVowel(char) # Checks if there is a single vowel to pronounce
                pronounce += singleVowelSound
                i += 1
    i = 0
    # Iterate through the pronounciation to correct for the Okina
    while i < len(pronounce):
        char = pronounce[i]
        okinaIndex = i - 1

        if char == "'":
            part1 = pronounce[:okinaIndex]
            part2 = pronounce[i:]
            pronounce = part1 + part2

        i += 1

    pronounce = "".join(pronounce)
    pronounce = pronounce.strip()
    splitStringIndex = len(pronounce) - 1
    pronounce = pronounce[0:splitStringIndex] + " "
    return pronounce

def pronounce(phrase):

    phrase = phrase.split(" ")
    pronouncedString = ""

    # Loop through each word in phrase
    i = 0
    while i < len(phrase):
        word = phrase[i]
        word = word.strip()
        word = pronounceWord(word)
        pronouncedString += word + " "

        i += 1

    return pronouncedString

def getChoice(question, options):

    proceed = True

    optionString = "("
    i = 0
    # Completes string for options by adding backslashes
    while i < len(options):

        optionWord = options[i]
        optionString += optionWord + "/"

        i += 1

    optionLength = len(optionString) - 1
    optionString = optionString[0:optionLength]
    optionString += ")"

    while proceed:

        choice = input(question + " " + optionString + ": ")

        choice = choice.lower()

        if choice == "yes" or choice == "y":
            proceed = False
            choice = "yes"
            return choice

        if choice == "no" or choice == "n":
            proceed = False
            choice = "no"
            return choice

        if choice != "yes" and choice != "no" and choice != "y" and choice != "n":
            print("Enter ", optionString)

def main():

    choice = True
    while choice:

        validString = getHawaiianPhrase()
        finalString = []

        i = 0
        # Iterate through my valid string to find proper pronounciation of "w"
        while i < len(validString):
            word = validString[i] # individual word
            isThereAW = getWordW(word) # Find if there is a W in word

            if isThereAW == True:
                indexW = getIndexW(word) # get index of w
                char = pronounceW(word, indexW) # find proper char using the pronounceW function
                newWord = turnStringIntoList(word)
                newWord[indexW] = char
                newWord = "".join(newWord)
                finalString.append(newWord)

            if isThereAW == False:
                finalString.append(word)

            i += 1

        finalPhrase = " ".join(finalString)
        finalPhrase = finalPhrase.upper()
        print("The phrase", finalPhrase, "is pronounced:")
        finalPhrase = finalPhrase.lower()
        print("\t", pronounce(finalPhrase))

        choice = getChoice(CONTINUE,ANSWERS)

        if choice == "no":
            choice = False

main()



