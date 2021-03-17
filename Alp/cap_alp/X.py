def X():
    for row in range(7):
        for col in range(7):
            if (row-col==0 or row+col==6):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
