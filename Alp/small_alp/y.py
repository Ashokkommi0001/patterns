def for_y():
    for row in range(7):
        for col in range(5):
            if (row%3==0 and row!=0) and (col>0 and col<4) or (col==0 and (row>0 and row<3)) or (col==4 and (row>0 and row<6)) or (row==5 and col==0):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_y():
    row=0
    while row<7:
        col=0
        while col<5:
            if (row%3==0 and row!=0) and (col>0 and col<4) or (col==0 and (row>0 and row<3)) or (col==4 and (row>0 and row<6)) or (row==5 and col==0):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
