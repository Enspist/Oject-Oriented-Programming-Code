#starting values for both the count and total values
total = 0
count_numbers = 0

#starting the indefinite while loop
while True:
    #asking for input from the user
    numbers = input("Enter number or q to quit: ")
    #If the user enters the quit command the program will break
    if numbers == 'q':
        break
    #otherwise it will run the loop again while counted up one for both the total and count
    total += int(numbers)
    count_numbers += 1

#taking the average is just the total sum divided by the count
average = total / count_numbers

#here is the print statement for both the total and count
print(f"The sum of the numbers entered is {total}.")
print(f"The count of the numbers entered is {count_numbers}.")
print(f"The average of the numbers entered is {average}.")