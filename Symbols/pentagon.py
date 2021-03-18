def for_pentagon():
    for row in range(10):
        for col in range(9):
            if (row==9) or (row>4 and (col==0 or col==8)) or (row+col==4 or col-row==4):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_pentagon():
    row=0
    while row<10:
        col=0
        while col<9:
            if (row==9) or (row>4 and (col==0 or col==8)) or (row+col==4 or col-row==4):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
