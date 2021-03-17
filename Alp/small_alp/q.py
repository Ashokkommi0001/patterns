def q():
    for row in range(7):
        for col in range(6):
            if col==4 or (col==0 and (row==1 or row==2)) or ((row==0 or row==3) and (col>0 and col<4)) or (row==5 and col==5):
                print("*",end=" ")
            else:
                    print(end="  ")
        print()
