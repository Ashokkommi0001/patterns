def f():
    for row in range(8):
        for col in range(7):
            if (col==3 and row>0) or (row==5 and col>0 and col<6) or (row==0 and col>3 and col<6) or (col==6 and row==1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
