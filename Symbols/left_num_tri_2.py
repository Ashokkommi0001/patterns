a=8
def left_num_tri_2():
    for i in range(0, a):
        for j in range(i+1,0,-1):
            print(j, end=" ")
        print()
