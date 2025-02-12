# Right angle triangle ///

#rows = int(input("Enter the number of rows: "))

#for i in range(1, rows + 1):
#    print("*" * i)
    

# Inverted right angle triangle ///

#rows = int(input("Enter the number of rows: "))

#for i in range(rows, 0, -1):
 #   print("*" * i)
 
 
# Pyramid pattern ///

#rows = int(input("Enter the number of rows: "))

#for i in range(1, rows, +1):
 #   spaces = " " * (rows - i)
  #  stars = "*" * (2 * i -1)
   # print(spaces + stars)
   
   
# Diamond pattern ///

#rows = int(input("Enter the number of rows: "))

#Upper part
#for i in range(1, rows +1):
 #   spaces = " " * (rows - i)
  #  stars = "*" * (2 * i - 1)
   # print(spaces + stars)
    
#Lower part
#for i in range(rows - 1, 0, -1):
 #   spaces = " " * (rows - i)
  #  stars = "*" * (2 * i - 1)
   # print(spaces + stars)
   
# Star framing around the name  ///

name = input("Enter your name: ")

border = "*" * (len(name) + 4)
print(border)
print(f"* {name} * ")
print(border)
    