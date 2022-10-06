import random
import sys

def tot_streaks(maxs, iterations):
    tot=0
    for j in range(iterations):
        ex=[]
        for i in range(100):
            ex.append(random.randint(0,1))
        counter=0
        for j in range(99):
            if ex[j+1] == ex[j]:
                counter+=1
            else:
                counter=0
            if counter == maxs:
                tot+=1
                counter=0
    return tot
maxs = 10
iterations = 10000
try:
    tot = tot_streaks(maxs, iterations)
except KeyboardInterrupt:
    print('exiting...')
    sys.exit(0)
print(str(tot) + ' out of ' + str(iterations))
