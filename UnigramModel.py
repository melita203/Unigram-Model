# Project : Unigram Model

# Large Language Models (like the ones used in Google Search, Bard, & ChatGPT) use word probabilities to model the way words are used in text. 
# In this project, I will be building a very simple language model called a “unigram” model! 
# I’ll pick a text to “train” it on and make a program that reports the probability that sentences appear in the text someone picked. 

# This function creates and returns a list of the specified length containing only 0s.
# Arguments: length (integer): the desired length of the list
# Return: returns a list of the specified length, containing only 0s
def createEmptyList(length):
    return [0] * length

# This function returns the index of “word” inside of the list “allWords”
# Arguments: 
#   allWords - a list of strings to search inside of;
#   word - a string to search for
# Return: returns an integer representing the index of word inside of allWords or -1 if the word is not present
def getIndexOfWord(wordList, word):
    try: 
        return wordList.index(word)
    except:
        return -1

# This function opens the requested file and returns the origText in it as a list of individual words.
# Arguments: fileName (string) - the name of the file you want to open and read the origText from.
# Return: returns a list of strings. Each string is one word.
def readWordsFromText(fileName):
    file = open(fileName, "r")
    fileContents = file.read()
    file.close()
    return fileContents.split()

# This function returns a list containing all of the unique words inside of the list “words” (i.e., removes all repeats in “words”).
# Arguments: words (list) - a list containing all of the words in a text.
# Return: returns a list of strings. Each string is one word.
def makeWordList(words):
    # Create an empty list
    wordList = []
    # For each word: 
    for word in words:
        #  if it's NOT in the list, add it
        if word not in wordList:
            wordList.append(word)
        #  else, skip it
        else:
            pass
    # return list
    return wordList

# ---------- ADD YOUR FUNCTIONS BELOW THIS LINE - DON'T MODIFY THE ONES ABOVE ------------- #
# origtext is list with all words
# wordlist is origtext list but without duplicates
# define the function computeDistribution
def computeDistribution(origText, wordList):
    # create an empty list
    ProbList = []
    # for each unique word , I have to calculate the parcentage of unique words present in the word list
    for uniqueWord in wordList:
    # This function computes probability distribution
        distribution = origText.count (uniqueWord) /len(origText)
    # New distribution will be added by the end of the problist
        ProbList.append(distribution) 
    # return problist
    return ProbList


# define the function computeProbability
def computeProbability(wordList, dist, sentence):
# after adding all the probability distribution the total is equal to 1
    probability = 1
    # split the sentence into individual word
    wordSplite = sentence.split(" ")
    # for each word in the list, get the index
    for word in wordSplite:
        wordIndex = getIndexOfWord(wordList,word)
    # If the word entered by the user doesn’t appear in wordList, 
    # we should assign it a probability of 1/(length of wordList). 

        if wordIndex == -1:
            probability= probability * (1/len(wordList))
    #  keep updatong probability 
        else:
            probability = probability * (dist[wordIndex])
# return probability
    return probability
    
    
    

def main():
    # assign the title tp origText
    #origText = "Texts/Frankenstein.txt"
    # textWordList will store all the text from Frankenstein text file
    textWordList = readWordsFromText("Texts/Frankenstein.txt")
    # uniqueWords is the list of all unique words from the text wordlist
    uniqueWords = makeWordList(textWordList)
    # create a distribution of each uniqueWord present in the textWordList
    dist = computeDistribution(textWordList, uniqueWords)
    # input a sentence
    inputSentence = input("Input a sentence or input quit. ")
    # quit = False
    # No one has calculate probability till now, calculate probability
    
    # if the input sentence is not quite
    while inputSentence != "quit":
     # keep asking for inputs until user quits  
        probability = computeProbability(uniqueWords, dist, inputSentence)
        print("Your sentence has a probabiity of ", probability)
        inputSentence = input ("input a sentence or input 'quit'. ")
    print(" Thank you! ")
    
    
    
    # Fill in the main function!
    # print("Start of main") #This is a placeholder - you can delete it when you're ready.
    # readWordsFromText("Frankenstein.text")
    # filecontents = readWordsFromText()
    # with open("frankenstein.text", "r") as file:
    #   wordList = [line.strip() for line in file]
if __name__ == "__main__":
    main()