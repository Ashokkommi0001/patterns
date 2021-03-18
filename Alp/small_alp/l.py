def for_l():
    for row in range(7):
        for col in range(5):
            if (col==0) or (row==6 and col<3):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_l():
    row=0
    while row<7:
        col=0
        while col<5:
            if (col==0) or (row==6 and col<3):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
