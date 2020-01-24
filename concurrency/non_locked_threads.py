import time
import random
from threading import Thread

counter = 0


def increment_counter():
    global counter
    counter += 1
    time.sleep(random.random()) #fuzzing
    print(f'New counter value: {counter}')
    time.sleep(random.random())
    print('----------------')


#for x in range(10):
#    increment_counter()

for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()

