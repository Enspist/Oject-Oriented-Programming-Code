#This is a script that will take a user input as an int from 0 to 999 and return the value as a string version of the int
#this script will also print the number time the numbers 1-10 show up in a random 100 number field.

#importing necessary modules
import random


#Set Assignment Exercise
random.seed(1)

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0

list_of_numbers=[random.randint(1,10) for i in range(100)]

for nums in range(list_of_numbers[99]):
    if list_of_numbers[nums] == 1:
        count1 += 1
    elif list_of_numbers[nums] == 2:
        count2 += 1
    elif list_of_numbers[nums] == 3:
        count3 += 1
    elif list_of_numbers[nums] == 4:
        count4 += 1
    elif list_of_numbers[nums] == 5:
        count5 += 1
    elif list_of_numbers[nums] == 6:
        count6 += 1
    elif list_of_numbers[nums] == 7:
        count7 += 1
    elif list_of_numbers[nums] == 8:
        count8 += 1
    elif list_of_numbers[nums] == 9:
        count9 += 1
    elif list_of_numbers[nums] == 10:
        count10 += 1
    
print(f"1 shows up {count1} times")
print(f"2 shows up {count2} times")
print(f"3 shows up {count3} times")
print(f"4 shows up {count4} times")
print(f"5 shows up {count5} times")
print(f"6 shows up {count6} times")
print(f"7 shows up {count7} times")
print(f"8 shows up {count8} times")
print(f"9 shows up {count9} times")
print(f"10 shows up {count10} times")