from collections import deque

friends = deque(('Rolf', 'Joe', 'Anna', 'Jen', 'Dan'))


def get_friend():
    yield from friends


def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'HELLO {friend}'
        except StopIteration:
            break  #pass


friends_generator = get_friend()
g = greet(friends_generator)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
