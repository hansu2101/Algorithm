while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    elif (b>=a) and (b % a == 0):
        print('factor')
    elif (b<=a) and (a % b ==0):
        print('multiple')
    else:
        print('neither')
