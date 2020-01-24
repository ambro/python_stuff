import time
from concurrent.futures import ProcessPoolExecutor
from operations import complex_calculation

if __name__ == '__main__': #because on windows main module is executed at start of the new process
    start = time.time()
    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)

    print(f'Two process calculating took {time.time() - start}')