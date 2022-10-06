import concurrent.futures
import threading
import time

tmp = input("Enter limit: ")
# Force = input("Force multiprocessing (True/False): ")
start = time.perf_counter()
n = int(tmp)
prime = [2, 3]
list = 'prime-list.txt'
i_primer, i_odd = 4, 5
# initialize json file
with open(list, 'w') as f:
    f.write("--- List Of Prime Numbers In Order ---\n\t2\n\t")


# functions for odd and even numbers
def primer(prime, list, i_primer):
    p = len(prime)
    x = 0
    check = True
    while x < p:
        if i_primer % prime[x] == 0:
            check = False
            break
        x += 1
    if check:
        with open(list, 'a') as p1:
            prime.append(i_primer)
            p1.write(str(i_primer))
            p1.write("\n\t")
            print(i_primer)
            return [True, i_primer + 2, i_primer]
    else:
        return [False, i_primer + 2, None]


def odd(prime, list, i_odd):
    p = len(prime)
    x = 0
    check = True
    while x < p:
        if i_odd % prime[x] == 0:
            check = False
            break
        x += 1
    if check:
        with open(list, 'a') as p2:
            prime.append(i_odd)
            p2.write(str(i_odd))
            p2.write("\n\t")
            print(i_odd)
            return [True, i_odd + 2, i_odd]
    else:
        return [False, i_odd + 2, None]


# sharing calculus with multiprocessing
with concurrent.futures.ProcessPoolExecutor() as executor:
    print("1\n2\n3")
    while i_odd <= n:
        f1 = executor.submit(primer, prime, list, i_primer)
        f2 = executor.submit(odd, prime, list, i_odd)
        c1, i_primer, temp1 = f1.result()
        if c1:
            prime.append(temp1)
        c2, i_odd, temp2 = f2.result()
        if c2:
            prime.append(temp2)
    finish = time.perf_counter()
    print(f'Terminated in {round(finish - start, 2)} second(s)')
