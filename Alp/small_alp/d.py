def d():
    for row in range(7):
        for col in range(6):
            if (col==5 ) or ((row==3 or row==6) and col>0) or (col==0 and (row>3 and row<6)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
