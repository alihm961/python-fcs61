# Exercise 1 // Movie ticket price calculator

age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 5
elif age <=18:
    price = 8
else:
    price = 10
print(f"The ticket price is {price} $")


# Exercise 2 // Even or Odd checker

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
 
 
 # Exercise 3 // username and password

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")
    
