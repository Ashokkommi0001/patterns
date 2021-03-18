def for_1():
    for row in range(7):
        for col in range(7):
            if (col==3 or row==6) or (row<3 and row+col==2):
                print("*",end="")
            else:
                print(end=" ")
        print()


def while_1():
    row=0
    while row<7:
        col=0
        while col<7:
            if (col==3 or row==6) or (row<3 and row+col==2):
                print("*",end="")
            else:
                print(end=" ")
            col+=1
        row+=1
        print()
