# indexing in the python start from 0 and go upto n-1 length 
#  we can pass vale in index line[ start : end : step]

number = "1234-5678-9012"


# print(number[0])
# print(number[ 0: 4])
# print(number[: 4])
# print(number[-1])
# print(number[ : : 2])
# print(number[ : : ])

# last_four_digit = number[-4:]
# print(last_four_digit)

reverse = number[:: -1]# it will make the string reversed (setting the step to -1)
print(reverse)