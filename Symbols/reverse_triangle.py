def reverse_triangle():
    for row in range(6):
        for col in range(11):
            if (row==0) or (row-col==0 or row+col==10):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
