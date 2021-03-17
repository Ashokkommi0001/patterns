n=9
def right_num_tri():
    for i in range(1, n+1):
        for j in range(1, n-i+1):
            print(" ",end=" ")
        for k in range(i, 0, -1):
            print(k, end=" ")
        print()
