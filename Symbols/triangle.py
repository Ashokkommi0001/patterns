def triangle():
    for row in range(6):
        for col in range(11):
            if (row==5) or (col-row==5 or row+col==5):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
