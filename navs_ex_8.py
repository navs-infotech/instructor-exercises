mynumber = input("Enter a number between 1 to 10: ")
mynumber = int(mynumber)
print("You entered " + str(mynumber) + ".")

if 1 <= mynumber and mynumber <= 10:
    print(str(mynumber) + " is between 1 and 10.")
else:
    print(str(mynumber) + " is not between 1 and 10.")
