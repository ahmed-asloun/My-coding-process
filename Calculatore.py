"""x = input("what your x ?")
y = input("whats your Y ?")#so if we typed out numbers over here, input() will take it as a string
print(x+y)

x= 14 
y = 24
z = int(x)+int(y)#int() it convert a string that represents a valid integer value into an integer
print(z)"""
"""#we could do this to optimize the code
x=int(input("x? :"))
y=int(input("Y?:"))
print(x+y)"""
"""
#for float values like 1.2 8.6 pi we need to use the float() function
x=float(input("x? :"))
y=float(input("Y? :"))
print(round(x+y, 3))
#format the number adding commas as thousands separators
print(f"{x+y:,}")
#division x/y
print(f"{x/y:.2f}") #.2f format the number with two decimal places.
"""
'''
def calculator():
    x=float(input("what is your x: "))
    y=float(input("what is your y: "))
    z = x+y
    print(f"{z:,}")
calculator()
'''
def squaremain():
    x= int(input("what is your x? "))
    print(f"x squar is {squareseconde(x)}")
def squareseconde(n):
    return n*n
squaremain()
#to understand more the mechanics of "return"
'''
def square(x):
    x = x * x

value = 5
square(value)
print(value)  # This will print 5, not the squared value
                assigning a new value to it doesn't affect the variable value outside the function
                
thats why we use"return"

def square(x):
    return x * x

value = 5
value = square(value)  # Update value with the squared value
print(value)  # Now, it will print the squared value, which is 25
'''
'''
2**4=16   2 to the power of 4
'''
'''
pow(2,4)= 16
'''


