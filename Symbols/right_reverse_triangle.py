def right_reverse_triangle(): 
    for row in range(6):
        for col in range(6):
            if (col==5 or row==0) or row-col==0:
                print("*",end=" ")
            else:
                print(end="  ")
        print()
    
