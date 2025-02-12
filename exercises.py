# Exercise 1  $print numbers from 1 to 10

#for i in range(1, 11):
   # print(f"Number: {i}")
    
    
# Exercise 2  $keep asking the user for a number until they enter 0

#while True:
 #   num = int(input("Enter a number (0 to stop): "))
  #  if num == 0:
   #     print("Loop stopped")
    #    break
   # print(f"You entered: {num}")
    
    
# Exercise 3  $Print only even numbers from 1 to 20

#for i in range(2, 20, 2):
   # print(f"Even number: {i}")
    
    
# Exercise 4  $  $reverse the users word

word = input("Enter a word: ")
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word
print(f"Reversed word: {reversed_word}")
