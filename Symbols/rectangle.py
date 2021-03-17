def rectangle():
    for row in range(5):
        for col in range(10):
            if row==0 or row==4 or col==0 or col==9:
                print("*",end=" ")
            else:
                print(end="  ")
        print()
