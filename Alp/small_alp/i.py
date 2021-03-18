def for_i():
    for row in range(9):
        for col in range(7):
            if (col==3 or row==8) and row>1 or (row>2 and row+col==3) or row==0 and col==3 :
                print("*",end="")
            else:
                print(end=" ")
        print()

def while_i():
    row=0
    while row<9:
        col=0
        while col<7:
            if (col==3 or row==8) and row>1 or (row>2 and row+col==3) or row==0 and col==3 :
                print("*",end="")
            else:
                print(end=" ")
            col+=1
        row+=1
        print()
