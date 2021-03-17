def m():
    for row in range(5):
        for col in range(7):
            if row==col==0 or (col%3==0 and row>0) or (row==0 and col%3!=0):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
