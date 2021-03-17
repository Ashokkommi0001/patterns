def right_triangle():
    for row in range(6):
        for col in range(6):
            if (col==5 or row==5) or row+col==5:
                print("*",end=" ")
            else:
                print(end="  ")
        print()
