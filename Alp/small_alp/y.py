def y():
    for row in range(7):
        for col in range(5):
            if (row%3==0 and row!=0) and (col>0 and col<4) or (col==0 and (row>0 and row<3)) or (col==4 and (row>0 and row<6)) or (row==5 and col==0):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
