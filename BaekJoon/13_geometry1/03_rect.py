while True:
    array = list(map(int, input().split()))
    if array[0]==0 and array[1]==0 and array[2]==0:
        break
    array.sort()
    if round(array[0]**2) + round(array[1]**2) == round(array[2]**2):
        print('right')
    else:
        print('wrong')


