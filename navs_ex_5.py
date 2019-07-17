print("Hello NAVS students!")

name = input("What is your name? ")
print("Hello, " + name + ".")

print("Do you like ice cream?")
likes = input("(Enter 1 for yes or 2 for no): ")

if likes == "1":
    print(name + " likes ice cream.")
elif likes == "2":
    print(name + " does not like ice cream.")
else:
    print("I did not understand what you entered.")
    
