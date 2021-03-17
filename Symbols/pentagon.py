def pentagon():
    for row in range(10):
        for col in range(9):
            if (row==9) or (row>4 and (col==0 or col==8)) or (row+col==4 or col-row==4):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
