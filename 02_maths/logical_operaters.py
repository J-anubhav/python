temp =45
is_raining = False
if temp>35 or temp<0 or is_raining:
    print("we cannot play")
else: 
    print("we can play")


is_sunny =False

if temp>35 and is_sunny:
    print('it is hot and sunny')

if not is_sunny:
    print('it is cloudy')

#  conditional expressions 
# also know as ternary operation

x= 5

print("postive" if x>0 else "negative")