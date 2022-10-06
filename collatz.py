import sys
def collatz(num):
    if (num % 2) == 1:
        print(3*num+1)
        return 3*num+1
    else:
        print(num//2)
        return num//2

num=0
print('enter an integer value:', end=' ')
try:
    while num == 0: 
        try:
            num=int(input())
            if num <= 0:
                print('enter an integer greater than 0:', end=' ')
                continue
        except ValueError:
            print('enter a valid integer:', end=' ')
    while num != 1:
        num=collatz(num)
except KeyboardInterrupt:
    print('exiting...')
    sys.exit(0)

