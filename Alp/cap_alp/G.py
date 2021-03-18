def for_G():
    for row in range(7):
        for col in range(5):
            if (col==0 and (row!=0 and row!=6))  or ((row==0 or row==6) and (col>0)) or (row==3 and col>1) or (row>3 and col==4):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_G():
    i=0
    while i<7:
        j=0
        while j<5:
            if (j==0 and (i!=0 and i!=6))  or ((i==0 or i==6) and (j>0)) or (i==3 and j>1) or (i>3 and j==4):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
