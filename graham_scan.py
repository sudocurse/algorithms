'''
Implements graham scan, a rotational sweep algo for creating the smallest
bounding polygon from a set of input points.
 from intro to algorithms (CLRS ch. 33)
'''
from operator import itemgetter
from matplotlib import pyplot

def min_y(input_q):
    '''returns smallest y in set. if tie, goes by smallest x.'''
    return input_q.index(min(input_q, key=itemgetter(1, 0)))

def polar_sorted(input_q, min_y):
    '''sorts list by polar angle counterclockwise around p0 (the min_y)'''
    #TODO implement polar_sorted. can this be parallelized
    return input_q

def angle(top, next_top, p0):
    """
        non-left angles wtf
    """
    #TODO angle. can this be parallelized
    pass

def graham_scan(input_set):
    '''
        Takes a set of points of size >= 3. This is tested for.

        Assumes points are unique, and not collinear. TODO: test for these

        Algorithm description:
            (q) input_set = input_set
            (result_stack) s = []
            (candidates) p[0] = min_y(input_set) # min y
    '''
    assert len(input_set) >= 3 # q
    # assert unique
    # assert non-collinear

    candidates = [] # p
    results = [] # s

    mindex = min_y(input_set)
    candidates.append(input_set[mindex])
    del input_set[mindex] # why does this keyword feel gross

    candidates.extend(polar_sorted(input_set, candidates[0]))

    results.append(candidates[0])
    results.append(candidates[1])
    results.append(candidates[2])

    for item in range(3, len(candidates)):
        # enumerate for index?? may need to pass that info onto angle()
        while angle(results[-1],results[-2],candidates[0]) > 90: # that's 90 degrees
            results.pop()

        results.append(candidates[1])

    return results

def generate_coordinates(length):
    '''input number of tuples. return that many rand tuples.'''
    import random
    rsamp = random.sample(range(1, 100), length * 2)
    return zip(rsamp[:length], rsamp[length:])

def plot(set, bound):
    pyplot.scatter(*zip(*set))
    pyplot.show()

if __name__ == '__main__':
    #
    #TODO: write some unit tests to make sure graham_scan(data) fails on bad length, non-unique, or collinear input data
    #

    data = generate_coordinates(5)
    boundaries = graham_scan(data)
    plot(data, boundaries)
