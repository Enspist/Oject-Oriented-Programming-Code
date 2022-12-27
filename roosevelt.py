#original string
string_phrase = "The only thing we have to fear is fear itself"

#splitting the phrase into a list so that the words can be manipulated
phrase_list = string_phrase.split(' ')

#a list of vowels to make checking them easier and neater in the for loop
vowels = 'aeiou'

#the blank list that changed words will be added to
new_list = []

#for each word in the list the word will be looked at
for word in phrase_list:
    #if the word starts with a vowel it will be affected
    if word[0] in  vowels:
        #print the word with "way" on the end of it and add it to the new list
        new_list.append(word + "way")
    #if the word does not start with a vowel then it will be affected here
    else:
        #this is to get the first letter of the word so that it can be moved to the end
        drop_let = word[0]
        #when adding the word to the new list, by starting with the second place value the first letter gets chopped off
        #and then added to the end of the word along with "ay"
        new_list.append(word[1:] + drop_let +'ay')
        
#the new list is then converted back into a string with all of the parameters changed        
final_string = ' '.join(new_list)

#here the string is printed out with the first letter of the sentence capitalized.
print(final_string.capitalize())
