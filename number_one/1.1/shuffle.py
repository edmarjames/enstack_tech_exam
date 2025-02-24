import random

'''
The first loop (for x in range(14)) runs outer, meaning x changes slower.
The second loop (for y in range(4)) runs inner, meaning y changes faster.
This naturally results in (x, y) order

sorting the list of tuple by y then x in ascending order using sort and lambda functions.

used a built-in shuffle function from a standard library (random.shuffle()) to shuffle it.
'''

def shuffle_list():
    A = [(x, y) for x in range(14) for y in range(4)]
    A.sort(key = lambda t: (t[1], t[0]))
    random.shuffle(A)
    return A

shuffled_one = shuffle_list()
print(shuffled_one)