def _4():
    for i in range(7):
        for j in range(5):
            if (j==3 or i==4 or i+j==3):
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
        print()
