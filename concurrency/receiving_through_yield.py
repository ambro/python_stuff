from collections import deque

# def greet():
#     friend = yield
#     print(f'Hello {friend}')
#
#
# g = greet()
# g.send(None)  # priming the generator
# g.send('Adam')

friends = deque(('Rolf', 'Joe', 'Anna', 'Jen', 'Dan'))


# called coroutine instead of generator cause it's not returning
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    g.send(None)
    while True:
        greening = yield
        g.send(greening)

# or
# def greet(g):
#     yield from g


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Multitasking here')
greeter.send('How are you,')
