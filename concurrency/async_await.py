from collections import deque
from types import coroutine

# def greet():
#     friend = yield
#     print(f'Hello {friend}')
#
#
# g = greet()
# g.send(None)  # priming the generator
# g.send('Adam')

friends = deque(('Rolf', 'Joe', 'Anna', 'Jen', 'Dan'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('starting')
    await g
    print('ending')

# the old ways
# def greet(g):
#     g.send(None)
#     while True:
#         greening = yield
#         g.send(greening)

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Multitasking here')
greeter.send('How are you,')
greeter.send('How are you,')
greeter.send('How are you,')
greeter.send('How are you,')
greeter.send('How are you,')
greeter.send('How are you,')


# async def test():
#     await friend_upper()
#
#
# test_gen = test()
# test_gen.send(None)
# test_gen.send('A')
# test_gen.send('B')
# test_gen.send('C')

