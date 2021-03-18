def for_right_triangle():
    for row in range(6):
        for col in range(6):
            if (col==5 or row==5) or row+col==5:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_right_triangle():
    row=0
    while row<6:
        col=0
        while col<6:
            if (col==5 or row==5) or row+col==5:
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
