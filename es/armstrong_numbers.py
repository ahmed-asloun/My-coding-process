for i in range(100,10**6):
    Nmbr = i
    Q=Nmbr
    S=0
    while Q!=0:
        R=Q%10 
        Q=Q//10
        S=R**3+S
    if S == Nmbr:
        print(Nmbr)