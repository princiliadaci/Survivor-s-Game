# The Survivor's Number, Group 6
# Author: Princilia DACI

from collections import deque

def J_0(n):
    if n <= 0:
        return "Please enter a positive integer for n"
    else:
        people = [i for i in range(1, n + 1)]
        print(people)
        while len(people) > 1:
            if len(people) % 2 == 0:  # Even case
                for i in range(len(people)//2):
                    h = people.pop(i + 1)
                    print(people, "\t", h, "is eliminated")
            else:  # Odd case
                for i in range(len(people)//2):
                    h = people.pop(i + 1)
                    print(people, "\t", h, "is eliminated")
                people.insert(0, people.pop(len(people) - 1))
                print(people)
        return f"So {people[0]} is the only survivor"


def J_1(n):
    m = 0
    if n == 1:
        return 1
    elif n <= 0:
        return "Please enter a positive integer for n"
    else:
        # Find the greatest m and the corresponding
        # remainder l such that n = 2^m + l
        for j in reversed(range(n)):
            for i in range(n):
                if n == pow(2, i) + j:
                    m, l = i, j
        return 1 + 2*l



def J_2(n):
    # I look for the largest power of 2 that is not bigger than n,
    # by doubling p as long as I stay below n
    p = 1
    while 2 * p <= n:
        p = 2 * p
    l = n - p
    return 2 * l + 1


def J_binary(n):
    b = bin(n)[2:]               # for example 10 gives '1010'
    return int(b[1:] + b[0], 2)  # I move the first digit to the end


def J_start(n, s):
    # survivor when the game starts with person s (Section 4.2)
    p = 1
    while 2 * p <= n:
        p = 2 * p
    l = n - p
    if s + 2 * l <= n:
        return s + 2 * l
    return s + 2 * l - n


def play(n, s=1):
    # I play the game without printing anything, to check the formulas
    circle = deque(range(1, n + 1))
    circle.rotate(-(s - 1))      # person s is now the first of the list
    while len(circle) > 1:
        circle.rotate(-1)        # the first person is skipped and goes to the back
        circle.popleft()         # the next one is eliminated
    return circle[0]


def check(N):
    for n in range(1, N + 1):
        assert play(n) == J_2(n) == J_binary(n)
        for s in range(1, n + 1):
            assert play(n, s) == J_start(n, s)
    return "all the checks passed for n = 1, ..., " + str(N)


if __name__ == "__main__":
    print(J_0(10))
    print(J_1(10), J_2(10), J_binary(10), J_start(10, 4))
    print(check(200))
