"""
#here we are playing with the parameters of the print function
name = input("what is your name: ")
print('hello', name, end="")
print("hello", end="\n ")
print(name)
"""
'''
#print(""freind"")="freind" problem we will use single quotation mark '
print('"freind"')
print("'freind'")
#"special string" python feature  to activat it we add 'f'
print(f"hello, {name}")
#how to remove the accidential white space from the string
#strip() its a method
name2 = input("what is your name: ")
name2 = name2.strip()
#capitalize first letter of thename methode
name2 = name2.capitalize()
print('hello', name2)
# capitalize all the letters 
name2 = name2.title()
print('hello', name2)
#remove white space and title case the name
name2 = name2.strip().title()
print('hello', name2)
'''
'''
#how to optimaze this code
name2 = input("what is your name: ").strip().title()
print(name2)
#how to split a the name into last and first name
first, last =name2. split(" ")#where do u want it to be separate from
print(f"hello, {last}")


#def: to define your own function
def hello(to_name="World"):   #so we used this parametre "to_name" as like the variabe of the function
    print("Hello",to_name)

hello()
'''
def hello(to):
    print("Hello Wolrd",end='\n')
    print(f"hello,{to}")
name = input("what is your name: ").strip().title()
first, last1 = name.split(" ")
hello(name)
print(f"Your first name is {first}")
print(f"Your first name is {last}")

first_name, last_name= input("what is your name: ").split(" ")



