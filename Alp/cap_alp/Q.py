def for_Q():
    for row in range(7):
        for col in range(6):
            if ((col==0 or col==4) and (row!=0 and row!=6)) or (col>0 and col<4) and (row==0 or row==6) or (row>2 and row-col==1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_Q():
    i=0
    while i<7:
        j=0
        while j<6:
            if ((j==0 or j==4) and (i!=0 and i!=6)) or (j>0 and j<4) and (i==0 or i==6) or (i>2 and i-j==1):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
