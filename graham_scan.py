'''
Implements graham scan, a rotational sweep algo for creating the smallest
bounding polygon from a set of input points.
 from intro to algorithms (CLRS ch. 33)
'''
from operator import itemgetter
from matplotlib import pyplot

def find_min_y(input_q):
    '''returns smallest y in set. if tie, goes by smallest x.'''
    return input_q.index(min(input_q, key=itemgetter(1, 0)))

def cross_product(vector1, vector2):
    '''returns cross product of two vectors (x1 * y2) - (x2 * y1)'''

    #if this is positive, v1 is clockwise from p2; if negative, counterclockwise
    #if this is zero, the vectors are equivalent or collinear, or one is len 0
    return (vector1[0] * vector2[1]) - (vector2[0] * vector1[1])

    # so in sorted order a,b, a is clockwise from b cross product
    # meaning would be like a x b > 0

def polar_sort(input_q, orig_pt):
    #TODO: testing for assumptions == verifying cross product and sort order
    '''sorts list by polar angle counterclockwise around p0 (the orig_pt)'''
    #TODO implement polar_sorted. can this be parallelized
    if orig_pt is None:
        print "this shouldn't happen"

    normalized = map(lambda x: (x[0] - orig_pt[0], x[1] - orig_pt[1]), input_q)


    def qsort(L):
        '''a cross product quicksort. if thing x pt >0, counterclockwise,
            if thing x point > 0, clockwise. and i thiIink it discards colinear?
        '''
        if len(L) <= 1: return L
        return qsort([i for i in L[1:] if cross_product(i,L[0])>0]) + L[0:1] + \
               qsort([i for i in L[1:] if cross_product(i,L[0])<0])

    return map(lambda x: (x[0] + orig_pt[0], x[1] + orig_pt[1]), qsort(normalized))

def angle(top, next_top, min_y):
    """
        non-left angles wtf
    """
    if top is None or next_top is None or min_y is None:
        print "this shouldn't happen"

    #TODO implement this! should be the last piece

def graham_scan(input_set):
    '''
        Takes a set of points of size >= 3 and returns smallest bounding polygon.
        Size assumption is tested for.
    '''

    assert len(input_set) >= 3 # q
    # assert unique
    # assert non-collinear

    polar_sorted = [] # p
    vertices = [] # s

    mindex = find_min_y(input_set)
    polar_sorted.append(input_set[mindex])
    input_set = input_set[:mindex] + input_set[mindex+1:] # why does this keyword feel gross

    polar_sorted.extend(polar_sort(input_set, polar_sorted[0]))
    # so far so good....

    print "sorted: ", polar_sorted

    vertices.append(polar_sorted[0])
    vertices.append(polar_sorted[1])
    vertices.append(polar_sorted[2])

    print "vertices: ", vertices

    for candidate_point in polar_sorted[3:]:
        while angle(vertices[-1], vertices[-2], candidate_point) > 90: # degrees
            vertices.pop()
        vertices.append(candidate_point)

    return vertices



def plot(dset, bound):
    '''plot the list of tuples dset and create a bounding polygon from bound'''

    last = bound[0]
    bound.append(last)

    for cur in bound[1:]:
        pyplot.plot(last[0], last[1], cur[0], cur[1])
        last = cur

    pyplot.scatter(*zip(*dset))
    pyplot.show()

def generate_coordinates(length):
    '''input number of tuples. return that many rand tuples.'''
    import random
    rsamp = random.sample(range(1, 100), length * 2)
    return zip(rsamp[:length], rsamp[length:])

if __name__ == '__main__':

    data = generate_coordinates(4)
    print "data =", data
    boundaries = graham_scan(data)
    print "bounds ",boundaries
    plot(data, boundaries)
