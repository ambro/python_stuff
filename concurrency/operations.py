import time


def ask_user():
    start = time.time()
    user_input = input("Name please: ")
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user took {time.time() - start}')


def complex_calculation():
    start = time.time()
    print('Starting calculations')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation took {time.time() - start}')