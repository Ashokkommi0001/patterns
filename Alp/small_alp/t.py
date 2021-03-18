def for_t():
    for row in range(7):
        for col in range(4):
            if (row==2 and col<4) or (col==1 and row<6) or (row==6 and col>1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_t():
    row=0
    while row<7:
        col=0
        while col<4:
            if (row==2 and col<4) or (col==1 and row<6) or (row==6 and col>1):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
