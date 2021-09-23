import sys

str1 = input('Enter first string:')
str2 = input('Enter second string:')

#Add two strings by programmer1
print(str1 + str2) 

#Count the number of word of first string by programmer2
print(str1 + ' has ' + str(len(str1.split())) + ' of words.')

# Compare if the two strings are the same by programmer3
if str1 == str2: 
    print('These two strings are identical.') 
else: 
    print('These two strings are not identical.' ) 
