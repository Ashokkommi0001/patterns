def for_four():
    for i in range(7):
        for j in range(5):
            if (j==3 or i==4 or i+j==3):
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
        print()

def while_four():
    row=0
    while row<7:
        col=0
        while col<5:
            if (col==3 or row==4 or row+col==3):
                print('*',end =" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
