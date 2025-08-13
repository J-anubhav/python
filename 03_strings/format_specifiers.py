# format specifiers :  { value : flags} format a valuse based on what flags are inserted 

price1 = 32.235
price2 = -900.34
price3 = 143.3


# is used for the decimicial precision after 2 decimal points
print(f"price 1 is {price1: .2f}")
print(f"price 2 is {price2:.2f}")
print(f"price 3 is {price3:.2f}")


# thi is used for the formaing tha alingment where you can use > for - right alignment  < for the left alignemt  and ^ for the center aligment 
print(f"price 1 is {price1:>10}")
print(f"price 2 is {price2:>10}")
print(f"price 3 is {price3:>10}")


# can also show cxase if it is postive and i want ot show it if it is postive 
print(f"price 1 is {price1:+}")
print(f"price 2 is {price2:+}")
print(f"price 3 is {price3:+}")



#  and can use two flages at the same time 
print(f"price 1 is {price1:>10,.2f}")
print(f"price 2 is {price2:>10.2f}")
print(f"price 3 is {price3:>10,.2f}")