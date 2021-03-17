def N():
    for row in range(7):
        for col in range(7):
            if (col==0 or col==6) or row-col==0:
                print("*",end="  ")
            else:
                print(end="   ")
        print()
