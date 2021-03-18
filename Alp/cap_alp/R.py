def for_R():
    for row in range(7):
        for col in range(5):
            if col==0 or (col==4 and (row==1 or row==2)) or ((row==0 or row==3) and (col>0 and col<4)) or (row>2 and row-col==2):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_R():
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 or (j==4 and (i==1 or i==2)) or ((i==0 or i==3) and (j>0 and j<4)) or (i>2 and i-j==2):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1
        print()
