# age logic
#age = int(input("please enter your age: "))

#check = age > 12

#if check:
 #   print("You are eligible to run this code")
#else:
#    print("Not eligible")
    
# Grades logic 

#grade = int(input("Please enter your grade: "))

#if grade > 90:
  #  print("A")
#elif grade > 80:
 #   print("B")
#elif grade > 70:
   # print("C")
#elif grade > 70:
 #   print("D")
#else:
 #   Print("F")
    
# Give the user the choice between kg and lbs, then calculate the mass according to the choice.


# Ask the user to choose kg or lbs
unit = input("Enter 'kg' to input weight in kilograms or 'lbs' for pounds: ")


if unit == "kg":
    weight = float(input("Enter your weight in kilograms: "))
    converted_weight = weight * 2.20462 
    print("Your weight in pounds is:", converted_weight, "lbs")

elif unit == "lbs":
    weight = float(input("Enter your weight in pounds: "))
    converted_weight = weight * 0.454  
    print("Your weight in kilograms is:", converted_weight, "kg")
else:
    print("Invalid choice. Please enter 'kg' or 'lbs'.")