import sys

num1 = input('Enter first number:')
num2 = input('Enter second number:')

#Add two number by programmer1
sum = int(num1) + int(num2)
print('The sum of '+ num1 +' + '+ num2 + ' is ' + str(sum)) 

#Find the square root of first number by programmer2
num_sqrt = int(num1) ** 0.5
print('The square root of ' + num1 + ' is ' + str(num_sqrt))

# Check if the 2nd number is even or odd by programmer3
if (int(num2) % 2) == 0: 
    print(num2 + ' is an Even number.') 
else: 
    print(num2 + ' is an Odd number.' ) 
