def k():
    for row in range(7):
        for col in range(5):
            if (col==0) or (row>1 and (row+col==5  or row-col==3)):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
