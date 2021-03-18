def for_u():
    for row in range(7):
        for col in range(6):
            if ((col==0 or col==4) and row<5) or (row==5 and col>0 and col<4) or  (row+col==10) and row!=6:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_u():
    row=0
    while row<7:
        col=0
        while col<6:
            if ((col==0 or col==4) and row<5) or (row==5 and col>0 and col<4) or  (row+col==10) and row!=6:
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
