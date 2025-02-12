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