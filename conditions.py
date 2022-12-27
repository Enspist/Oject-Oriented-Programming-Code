#The three variables
letter1 = "m"
letter2 = "u"
letter3 = "y"

#The test
#comments are only of the first iteration of the if statements to save space and sanity and to make the code look prettier
#if the test letter is in the group of vowels, it will be printed out as a vowel
if letter1 in "aeiou":
    print(f"{letter1} is a vowel.")
#if the test letter fails the first test but is a y, it will be printed out as a y here
elif letter1 == "y":
    print(f"{letter1} is a y.")
#if the test letter fails both of the above tests, it must be a consonant, so it will be printed as one
else:
   print(f"{letter1} is a consonant")

if letter2 in "aeiou":
     print(f"{letter2} is a vowel.")
elif letter2 == "y":
    print(f"{letter2} is a y.")
else:
    print(f"{letter2} is a consonant")

if letter3 in "aeiou":
    print(f"{letter3} is a vowel.")
elif letter3 in "y":
    print(f"{letter3} is a y.")
else:
    print(f"{letter3} is a consonant")