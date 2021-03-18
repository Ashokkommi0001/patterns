def for_Y():
    for row in range(7):
        for col in range(7):
            if (row-col==0 and row<3) or (row+col==6 and row<3) or (row>2 and col==3):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_Y():
    i=0
    while i<7:
        j=0
        while j<7:
            if (i-j==0 and i<3) or (i+j==6 and i<3) or (i>2 and j==3):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
