def _3():
    for row in range(7):
        for col in range(6):
            if (row%3==0 and col<5) or (col==5 and row%3!=0):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
