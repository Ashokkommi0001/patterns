def for_parlalogram():
    for row in range(7):
        for col in range(21):
            if ((row==0  and col>5) or (row==6 and col<14) or (row+col==6)) or row+col==20:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_parlalogram():
    row=0
    while row<7:
        col=0
        while col<21:
            if ((row==0  and col>5) or (row==6 and col<14) or (row+col==6)) or row+col==20:
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
