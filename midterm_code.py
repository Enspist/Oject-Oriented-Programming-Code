#This Code will read a test html file and change the title of the document
#It will also read if each letter in the header is a Vowel, Consonant or Space
#any blank print statements are so that the entire file is easier to read when read
from bs4 import BeautifulSoup

#This section of code is reading the html file and giving the name doc so that is can be manipulated
with open("text.html", "r") as file:
    doc = BeautifulSoup(file, "html.parser")
    
#This line is printing out the html file in a way that makes it more readable
print(doc.prettify())


print()
print()
print()

#Here the code is finding the Title tag and changing the string that is inside of the tag.
#It will then print out the changed title and the html file again to show the change in both sections
title = doc.title
print(title)
print()
print(title.string)
print()
title.string = "Changed Title"
print(title.string)
print()
print(title)
print()
print(doc.prettify())


print()
print()
print()


#This section of code will analyze the first header of the html file

#This is finding the first header and giving it a name to make it easier to read
#It also prints out the header and the string inside of the header
h1 = doc.h1
print(h1)
print()
print(h1.string)


print()
print()
print()

#This line is a list of vowels so that the if statement can reference them 
vowels = "aeiou"

#This for loop is going to find each letter in the header string and will see if it is a vowel, consonant, or space
#It will print out what it is for each letter
for letter in h1.string:
    if letter in vowels:
        print("Vowel")
    if letter == " ":
        print("space")
    else:
        print("consonant")