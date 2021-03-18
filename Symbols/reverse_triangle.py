def for_reverse_triangle():
    for row in range(6):
        for col in range(11):
            if (row==0) or (row-col==0 or row+col==10):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_reverse_triangle():
    row=0
    while row<6:
        col=0
        while col<11:
            if (row==0) or (row-col==0 or row+col==10):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
