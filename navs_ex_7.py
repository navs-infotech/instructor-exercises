mynumber = input("Enter a number between 1 to 10: ")
mynumber = int(mynumber)
print("You entered " + str(mynumber) + ".")

if 1 <= mynumber:
    print(str(mynumber) + " is greater than or equal to 1.")
if mynumber <= 10:
    print(str(mynumber) + " is less than or equal to 10.")
