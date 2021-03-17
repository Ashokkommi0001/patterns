def a():
    for row in range(8):
        for col in range(7):
            if (row%3==0 and (col>0 and col<5)) or (col==5 and (row>0 and row<7)) or ((row==1 or row==4 or row==5) and col==0) or (row+col==13):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
