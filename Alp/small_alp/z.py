def z():
    for row in range(5):
        for col in range(5):
            if row==0 or row==4 or row+col==4 :
                print("*",end=" ")
            else:
                print(end="  ")
        print()
