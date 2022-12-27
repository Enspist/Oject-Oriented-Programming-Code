#This program is going to take user input as letters and will calculate the value of the word
#this program uses Lists and For Loops and If/Else Statements

#this is the dictionary for each letter with its point value.
scrabble_dict = {1: ['A','E','I','O','U','L','N','R','S','T'],
                2: ['D','G'], 
                3: ['B','C','M','P'],
                4: ['F','H','V','W','Y'],
                5: ['K'],
                8: ['J','X'], 
                10: ['Q','Z']}


#this is count value that will be the total points value at the end
count = 0

#The code will ask for a word input and then make every letter uppercase so it can be read in the dictionary
word = input("Please enter a word: ").upper()

#This is going to check each letter in the dictionary and then will count the key value for each letter
for letter in word:
    for key, value in scrabble_dict.items():
        if letter in value:
            count += key


#this prints out the final count along with the word made back lowercase as the user input it
print(f"The points awarded for {word.lower()} is {count}")