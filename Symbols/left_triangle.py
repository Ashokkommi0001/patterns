def for_left_triangle():
    for row in range(6):
        for col in range(6):
            if (col==0 or row==5) or row-col==0:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_left_triangle():
    row=0
    while row<6:
        col=0
        while col<6:
            if (col==0 or row==5) or row-col==0:
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
