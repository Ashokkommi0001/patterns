def for_seven():
    for row in range(6):
        for col in range(6):
            if (row==0 or row+col==5):
                print("*",end="")
            else:
                print(end="  ")
        print()

def while_seven():
    row=0
    while row<6:
        col=0
        while col<6:
            if (row==0 or row+col==5):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
