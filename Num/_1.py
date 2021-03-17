def _1():
    for row in range(7):
        for col in range(7):
            if (col==3 or row==6) or (row<3 and row+col==2):
                print("*",end="")
            else:
                print(end=" ")
        print()

