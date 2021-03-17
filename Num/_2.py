def _2():
    for row in range(5):
        for col in range(4):
            if (row==4 or row+col==4)  or (row==0 and col!=0) or (row==1 and col<1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
