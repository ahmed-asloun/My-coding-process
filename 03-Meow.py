def main():
    n = int(input("How much Meow's you want lol: "))
    check(n)
    Meow(n)
def Meow(a):
    check(a)
    print("Meow\n"*a, end='')
def check(s):
    while True:
        if s<0:
            s = int(input("How much Meow's you want lol: "))
        else:
            return s
main()
            
