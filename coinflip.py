import random
import sys

def s0(flips, ht):
    while True:
        flips += 1
        if flip() == 1:
            continue
        break
    return s1(flips, ht)

def s1(flips, ht):
    while True:
        flips += 1
        if ht and flip() == 0:
            s0(flips, ht)
        if not ht and flip() == 1:
            continue
        break
    return terminal(flips)

def terminal(flips):
    return flips

# heads: 0
# tails: 1
def flip():
    return random.randint(0, 1)

loops = 1
if len(sys.argv) == 2:
    loops = int(sys.argv[1])

total = 0
for _ in range(loops):
    total += s0(0, False)

print(total / loops)
