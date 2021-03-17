def T():
    for row in range(6):
        for col in range(5):
            if (row==0 or col==2):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
