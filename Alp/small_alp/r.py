def r():
    for row in range(7):
        for col in range(6):
            if (col==2 and row>0) or (row<1 and col>2) or row==col==0:
                print("*",end=" ")
            else:
                print(end="  ")
        print()
