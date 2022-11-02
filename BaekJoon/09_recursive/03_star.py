n = int(input())

array = ['***', '* *', '***']

def print_star(n):

    if n == 3:
        print('*', end='')
    else:
        for i in range(n):
            for j in range(n):
                if n//3 <= j and j < n*2//3 and n//3 <= i and i < n*2//3:
                    print(' ', end='')
                else:
                    print_star(n//3)
            print('')



print_star(n)



        # if (n/3) < i <(n*2/3):
        #     print(' ')
        # print('*', end='')