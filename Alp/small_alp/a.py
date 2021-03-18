def for_a():
    for row in range(8):
        for col in range(7):
            if (row%3==0 and (col>0 and col<5)) or (col==5 and (row>0 and row<7)) or ((row==1 or row==4 or row==5) and col==0) or (row+col==13):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def while_a():
    row=0
    while row<8:
        col=0
        while col<7:
   
            if (row%3==0 and (col>0 and col<5)) or (col==5 and (row>0 and row<7)) or ((row==1 or row==4 or row==5) and col==0) or (row+col==13):
                print("*", end=" ")
            else:
                print(" ", end=" ")
            col+=1
        row+=1
        print()
