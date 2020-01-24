import time
from multiprocessing import Process
from operations import ask_user, complex_calculation

if __name__ == '__main__': #because on windows main module is executed at start of the new process
    process = Process(target=complex_calculation)
    process.start()
    start = time.time()
    ask_user()
    process.join()

    print(f'Two process took {time.time() - start}')

    process1 = Process(target=complex_calculation)
    process2 = Process(target=complex_calculation)
    start = time.time()
    process1.start()
    process2.start()

    process1.join()
    process2.join()
    print(f'Two process calculating took {time.time() - start}')