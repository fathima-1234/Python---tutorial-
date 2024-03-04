# Python3 program introducing f-string
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")
 
 
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")


# Prints today's date with help
# of datetime library
import datetime
 
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")


# integer literal
 
# Binary Literals
a = 0b10100
 
# Decimal Literal
b = 50
 
# Octal Literal
c = 0o320
 
# Hexadecimal Literal
d = 0x12b
 
print(a, b, c)