def for_2():
    for row in range(5):
        for col in range(4):
            if (row==4 or row+col==4)  or (row==0 and col!=0) or (row==1 and col<1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_2():
    row=0
    while row<5:
        col=0
        while col<4:
            if (row==4 or row+col==4)  or (row==0 and col!=0) or (row==1 and col<1):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
