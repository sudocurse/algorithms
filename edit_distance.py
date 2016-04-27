"""
Edit distance implementation

blost = {} # if we called 'meow' on this we would get a key error.
another way to handle this would be to add an exception handler
print cost['meow']
cost[frozenset(['meow','matter'])] = 3
cost[frozenset(['matter','meow'])] = 4
print cost[frozenset(['meow','matter'])]

try:
    blost['meow']
except KeyError:
    blost['meow']= "derp"
"""

import unittest
from collections import defaultdict
#from time import sleep

def edit(word, alt):
    '''
        word = initial, alt = target, returns levenstein distance.
    '''
    #has debugging prints littered throughout
    #TODO: make this more readable

    if word == alt:
        return 0
    #misses = 0
    cost = defaultdict(int) # sets it up so i don't have to zero init

    for index, x in enumerate(word):
        i = index + 1 # because slices!
        cost[frozenset(['', word[:i]])] = i

        for jindex, y in enumerate(alt):

            j = jindex+1
            cost[frozenset(['', alt[:j]])] = j

            if frozenset([alt[:j], word[:i]]) not in cost:
                print(cost)
                print(frozenset([word[:i], alt[:j]]))
                inserts = cost[frozenset([word[:i-1], alt[:j]])] + 1
                deletes = cost[frozenset([word[:i], alt[:j-1]])] + 1
                subs = cost[frozenset([word[:i-1], alt[:j-1]])] + (x != y)
                print(inserts, deletes, subs, word[:i], alt[:i])
                minimum = min(inserts, deletes, subs)
                #sleep(2)
                cost[frozenset([word[:i], alt[:j]])] = minimum

    #print misses
    print(cost[frozenset([word, alt])])
    print(cost)

    return cost[frozenset([word, alt])]


def compute_cost(word, alt):

    if word == alt:
        return 0, 0
    cost = defaultdict(int)
    misses = 0
    if frozenset([word, alt]) not in cost:
        #distance = -1
        for index, c in enumerate(word):
            i = index+1
            cost[frozenset(['', word[:i]])] = i
            for jindex, d in enumerate(alt):
                j = jindex+1
                cost[frozenset(['', alt[:j]])] = j
                if frozenset([alt[:j], word[:i]]) not in cost:
                    inserts = cost[frozenset([word[:i-1], alt[:j]])] + 1
                    deletes = cost[frozenset([word[:i], alt[:j-1]])] + 1
                    subs = cost[frozenset([word[:i-1], alt[:j-1]])] + (c != d)
                    minimum = min(inserts, deletes, subs)
#                    print "miss",alt[:j],word[:i],"\t\t","calculating mins:" , \
#                     inserts, deletes, subs, "\tcost:", minimum
                    cost[frozenset([word[:i], alt[:j]])] = minimum

    return cost[frozenset([word, alt])]

class testEdit(unittest.TestCase):
    '''checks that cat > cot edit distance is 1'''
    def testEdit(self):
        self.assertEqual(edit('cat', 'cot'), 1)

if __name__ == '__main__':
    edit('cat', 'cot')
