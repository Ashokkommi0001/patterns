def for_eight():
    for row in range(7):
        for col in range(5):
            if ((col==0 and row%3!=0) or (col==4 and row%3!=0)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_eight():
    row=0
    while row<7:
        col=0
        while col<5:
            if ((col==0 and row%3!=0) or (col==4 and row%3!=0)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
