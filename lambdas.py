#This script is going to sort the names of employees by their last name
#It will give them employee ID numbers based on their names
#This is to be done using Lambda functions.

#List of names
names_list = ['Frank Harrelson', 'Bob Sharles', 'Bob Tranklin', 'Bob Grody', 'Hank Charles', 'Bob Rarrelson', 
            'Mack Slobson', 'John Jonones', 'Rob Wranklin', 'Tom Simpsonian', 'Rob Rearrelson', 'John Moodys', 
            'Frank Shones', 'John Harrelson','Frank Quhorles', 'Tom Pharles', 'Frank Fwanklin', 'Frank Charleston', 
            'John Arles', 'John Georanklin', 'Frank Dobsonsoson', 'Diane Johnston', 'Dob Scone', 'Michael Scarn', 
            'Goldie Hawn', 'Billie Holliday', 'Woody Harrelson', 'Arthur Rubinstein', 'Thomas Edison', 'Robert Goulet']

#Printing out the list by sorted last name
print(sorted(names_list, key= lambda name: name.split()[-1]))

#adding some space between the two functions
print()
print()

#Using a Lambda Function to get the first five and last two
user_name = list(map(lambda name: name.split()[-1][0:5].lower()+name.split()[0][0:2].lower(), names_list))

print(user_name)

