def t():
    for row in range(7):
        for col in range(4):
            if (row==2 and col<4) or (col==1 and row<6) or (row==6 and col>1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
