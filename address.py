#these questions ask for the user input for their address
first_name = input('Enter your first name: ')
last_name = input('Enter your first name: ')
street_number = input('enter your street number: ')
street_name = input('enter your street name: ')
po_box = input("enter your PO Box or enter if not applicable: ")
city = input("enter your city: ")
state = input("enter your state: ")
zip_code = input("enter your zip code: ")

#this is the tuple that is storing all of the address information
address = first_name,last_name,street_number,street_name,po_box,city,state,zip_code

#here is the print statements that access the tuple to get each bit of information that is needed
print(f"{address[1]}, {address[0]}")
print(f"{address[2]} {address[3]}")

#if there is a PO BOX then the line for PO BOX will be print, otherwise it will be skipped. 
if address[4]:
    print(f"PO BOX {address[4]}")
    
#this is the final line printing the town, city and zip code.
print(f"{address[5]}, {address[6]} {address[7]}")
