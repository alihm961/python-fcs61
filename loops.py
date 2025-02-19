# For loop

#for i in range(1,11):
   # print("The square of i is: " + str(i**2))
    
    
# formatted string (fstring)

#for i in range(1, 11):
 #   print(f"The square of {i} is {i**2}")

# while loop, be aware of infinite loop
word = ""
while "stop":
    word = input("Enter a word: ")
  
# length
word = input("Enter a word: ")
length = len(word)

if length < 5:
    print("Word is short")
    
else:
    print("Word is long")