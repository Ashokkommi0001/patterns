def v():
    for row in range(8):
        for col in range(16):
            if (row-col==0 or row+col==14):
                print("*",end="")
            else:
                print(end=" ")
        print()
