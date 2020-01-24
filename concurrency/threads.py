import time
from threading import Thread

from operations import ask_user, complex_calculation


start = time.time()
ask_user()
complex_calculation()
print(f'Single thread took {time.time() - start}')

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Two threads took {time.time() - start}')