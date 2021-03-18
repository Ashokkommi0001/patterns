def for_W():
    for row in range(6):
        for col in range(5):
            if (col==0 or col==4) or ( row>2 and (row+col==5 or row-col==1)):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_W():
    i=0
    while i<6:
        j=0
        while j<5:
            if (j==0 or j==4) or (i>2 and (i+j==5 or i-j==1)):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
