#Get input from the user.

X = str(input("Provide a string: "))

#Define the length of the string.

y = len(X)

if X.isprintable():
    print("Reverse of the given string is: ",X[y::-1])
else:
    print("Dear User, The input given by you is not a string type! Please recheck it.")
