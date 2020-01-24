from concurrent.futures import ThreadPoolExecutor
import time

from operations import ask_user, complex_calculation

start = time.time()
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f'Single thread took {time.time() - start}')