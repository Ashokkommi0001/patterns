def hexagon():
    for row in range(5):
        for col in range(15):
            if ((row==0 or row==4) and col>3 and col<13) or (((row<=2) and row+col==4) or (row>2 and col-row==0)) or  (row<=2 and col-row==12) or (row>2 and row+col==16):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
