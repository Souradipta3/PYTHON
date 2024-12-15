n = int(input("Enter the no of numbers:"))
sum = 0
for num in range(1, n+1, 1):
    sum += num
print("The sum is", sum)
avg = sum/n
print("The average is", avg)
