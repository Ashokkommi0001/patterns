def for_n():
    for row in range(5):
        for col in range(4):
            if row==col==0 or (col%3==0 and row>0) or (row==0 and col%3!=0):
                print("*",end=" ")
            else:
                print(end="  ")
        print()

def while_n():
    row=0
    while row<5:
        col=0
        while col<4:
            if row==col==0 or (col%3==0 and row>0) or (row==0 and col%3!=0):
                print("*",end=" ")
            else:
                print(end="  ")
            col+=1
        row+=1
        print()
