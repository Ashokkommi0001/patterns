def l():
    for row in range(7):
        for col in range(5):
            if (col==0) or (row==6 and col<3):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
