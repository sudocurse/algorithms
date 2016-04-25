'''
Implements graham scan, a rotational sweep algo for creating the smallest
bounding polygon from a set of input points.
 from intro to algorithms (CLRS ch. 33)
'''
from operator import itemgetter
from matplotlib import pyplot
from matplotlib.path import Path
import matplotlib.patches as patches

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
    '''sorts list by polar angle counterclockwise around p0 (the orig_pt)'''
    #TODO: testing for assumptions == verifying cross product and sort order

    if orig_pt is None:
        print "this shouldn't happen"

    normalized = map(lambda x: (x[0] - orig_pt[0], x[1] - orig_pt[1]), input_q)
    #TODO: yeah pylint is going to complain about these map functions

    def qsort(L):
        '''
         a cross product quicksort. if thing x pt >0, counterclockwise,
         if thing x point > 0, clockwise. and i thiIink it discards colinear?
        '''
        if len(L) <= 1:
            return L
        return qsort([i for i in L[1:] if cross_product(i, L[0]) > 0]) + L[0:1] + \
               qsort([i for i in L[1:] if cross_product(i, L[0]) < 0])

    return map(lambda x: (x[0] + orig_pt[0], x[1] + orig_pt[1]), qsort(normalized))

def left_turn(p0, p1, p2):
    '''
     also uses vectors to determine clockwise-ness.
     if cross product of (p2-p0) x (p1 - p0) is negative, left turn at p1
    '''

    v1 = (p2[0]-p0[0], p2[1]-p0[1])
    v2 = (p1[0]-p0[0], p1[1]-p0[1])

    return cross_product(v1, v2) < 0

def graham_scan(input_set):
    '''
        Takes a set of points of size >= 3 and returns smallest bounding polygon.
        Size assumption is tested for.
    '''

    assert len(input_set) >= 3 # q

    # get input with y that is lowest first, then leftmost if tied, and make that p[0]
    mindex = find_min_y(input_set)
    polar_sorted = [input_set[mindex]]

    # p1...n = array of the rest of the coordinates, sorted by polar angle to p[0]
    input_set = input_set[:mindex] + input_set[mindex+1:]
    polar_sorted.extend(polar_sort(input_set, polar_sorted[0]))

    vertices = polar_sorted[0:3]

    #for each candidate point check
    for candidate_point in polar_sorted[3:]:
        # s1 -> s2 -> candidate_point needs to make a left turn
        while left_turn(vertices[-2], vertices[-1], candidate_point) is False: # degrees
            vertices.pop()

        vertices.append(candidate_point)

    return vertices

def plot(dset, bound):
    '''plot the list of tuples dset and create a bounding polygon from bound'''

    codes = [Path.MOVETO]

    for _ in bound[1:]:
        codes.append(Path.LINETO)

    bound.append(bound[0])
    codes.append(Path.CLOSEPOLY)

    path = Path(bound, codes)
    patch = patches.PathPatch(path, facecolor='orange', lw=2, alpha=0.3)
    pyplot.gca().add_patch(patch)

    pyplot.scatter(*zip(*dset))

    pyplot.show()

def generate_coordinates(length):
    '''input number of tuples. return that many rand tuples.'''
    import random
    rsamp = random.sample(range(1, 100), length * 2)
    return zip(rsamp[:length], rsamp[length:])

if __name__ == '__main__':

    data = generate_coordinates(40)
    boundaries = graham_scan(data)
    plot(data, boundaries)
