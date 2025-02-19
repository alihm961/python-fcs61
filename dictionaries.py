numbers = [45, 80, 32, 9]

sum = 0
average = 0
for num in numbers:
    sum = sum + num
    
average = sum / len(numbers)

print("sum:", sum)
print("Avg:", average)
