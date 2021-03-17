def M():
    for row in range(6):
        for col in range(5):
            if (col==0 or col==4) or (row<3 and (row-col==0 or row+col==4)):
                print("*",end="  ")
            else:
                print(end="   ")
        print()
