from random import randint
from time import sleep
from threading import Thread
from time import time

start_time = time()
my_list = []
def generating_mylist():
    for i in range(1,1001):
        a = randint(1,100000)
        sleep(0.000000000000000000000000000001)
        print(f'{i} --->> current number')
        my_list.append(a)

def calculatesum():
    print(f'sum of all numbers: {sum(my_list)}')
def calc_sum():
    print(f'everage sum of random numbers: {sum(my_list) / len(my_list)}')

def main():
    t1 = Thread(target=generating_mylist)
    t2 = Thread(target=calculatesum)
    t3 = Thread(target=calc_sum)
    t1.start()
    t1.join()
    t2.start()
    t3.start()
    t3.join()
    print(f'total spend time: {time() - start_time}')

if __name__ == "__main__":
    main()
