Nmbr = int(input("Ur number here: "))
Q=Nmbr
S=0
while Q!=0:
    R=Q%10 #I changed the line 5 with 6 and i got diff result so bewar next time!
    Q=Q//10
    S=R**3+S
if S == Nmbr:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

