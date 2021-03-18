def for_N():
    for row in range(7):
        for col in range(7):
            if (col==0 or col==6) or row-col==0:
                print("*",end="  ")
            else:
                print(end="   ")
        print()

def while_N():
    i=0
    while i<7:
        j=0
        while j<7:
            if (j==0 or j==6) or i-j==0:
                print("*",end="  ")
            else:
                print(end="   ")
            j+=1
        i+=1        
        print()
