def for_U():
    for row in range(7):
        for col in range(5):
            if ((col==0 or col==4) and row<6) or (row==6 and col>0 and col<4):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_U():
    i=0
    while i<7:
        j=0
        while j<5:
            if ((j==0 or j==4) and i<6) or (i==6 and j>0 and j<4):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
