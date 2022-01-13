#Every item has a starting price , we denote it as base_price
base_price = int(input("The starting price of the item:"))
#lets add all the values to the list 
coustmer_price = []
#we are supposed to give the number of participants participating in the auction
Participants = int(input("Enter the number of participants:"))
#we will use for loop to get input of every participant name
for i in range(Participants):
    customer_value = int(input("Enter the value if only greater than " + str(base_price) + ": "))
    coustmer_price.append(customer_value )
    coustmer_price.sort()
#Lets also see the list of all values entered 
print(coustmer_price)
# now lets see the maximum price that is given for the auction
print("The price at which the item sold is:", coustmer_price[-1])
#it gives a output as a note of thanks to the participants.
print("Thank you for using our "AUCTO" services")
