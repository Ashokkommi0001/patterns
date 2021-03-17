def left_reverse_triangle():
    for row in range(6):
        for col in range(6):
            if (col==0 or row==0) or row+col==5:
                print("*",end=" ")
            else:
                print(end="  ")
        print()
