def for_A():
    for i in range(7):
        for j in range(5):
            if ((j==0 or j==4) and i!=0) or (j>0 and j<4) and (i==0 or i==3):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_A():
    i=0
    while i<7:
        j=0
        while j<5:
            if ((j==0 or j==4) and i!=0) or (j>0 and j<4) and (i==0 or i==3):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1 
        print()
