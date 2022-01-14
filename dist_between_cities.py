#Distance between two cities
#lets plot world map on the 2D plane
#Get x , y co-ordinates of the cities
#city1 details 1st
city1 = str(input("Enter the 1st city name: "))
x1 = float(input("Enter" + city1 + "X co-ordinartes: "))
y1 = float(input("Enter" + city1 + "Y co-ordinartes: "))
#collect city2 details now
city2 =  str(input("Enter the 2nd city name: "))
x2 = float(input("Enter" + city2 + "X co-ordinartes: "))
y2 = float(input("Enter" + city2 + "Y co-ordinartes: "))
#calculate distance by simple maths
#here 1unit is 1 m
# scale is in Km
d1 = (x1-x2)^2
d2 = (y1-y2)^2
Distanse = (d1 + d2)^(1/2)
#after we processed the simple city distance equation now give output to the user.
print("The distance between" + city1 + "and" + city2 + "is: ", Distanse )
print("Thank you for using our services, HOW DHUUR IS IT?")
