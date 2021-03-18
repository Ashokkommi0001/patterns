def for_M():
    for row in range(6):
        for col in range(5):
            if (col==0 or col==4) or (row<3 and (row-col==0 or row+col==4)):
                print("*",end="  ")
            else:
                print(end="   ")
        print()

def while_M():
    i=0
    while i<6:
        j=0
        while j<5:
            if (j==0 or j==4) or (i<3 and (i-j==0 or i+j==4)):
                print("*",end="  ")
            else:
                print(end="   ")
            j+=1
        i+=1
        print()
