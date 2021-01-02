"""
Finds closest of two points from a set P of points.
Compares recursive O(nlgn) and brute force algorithms O(n^2).

Functions:
def find_closest_pair(P), pre-processes P and calls closest_pair_recursion(Px, Py)
def closest_pair_recursion(Px, Py), tha main function. Calls closest_split_pair(Px, Py, delta)
def closest_split_pair(Px, Py, delta), needed to calculate closest pairs that cross midline of P
def brute_force_closest_pair(P), used to compute base case in closest_pair_recursion(Px, Py)

def get_distance(pair): helper function to compute Euclidean distance
def print_list(l): helper function to print string representation of a list of point objects
"""
import math
import Point
from MergeSort import merge_sort_points_by

def find_closest_pair(P):
    """
    Pre-processes the list of points P and calls the recursive method
    :param P: list of points
    :return: the output of the recursive method:i.e. the pair of closest points
    """
    Px = merge_sort_points_by(P, x=True)
    Py = merge_sort_points_by(P, x=False)
    return closest_pair_recursion(Px, Py)

def closest_pair_recursion(Px, Py):
    """
    Recursive function. Calls on closest_split_pai and brute_force functions
    :param Px: P sorted by x
    :param Py: P sorted by y
    :return: closest_pair
    """
    # Base case - brute force for short list of points
    if len(Px) < 4:
        return brute_force_closest_pair(Px)
    # Recursive steps
    # Divide
    half_n = len(Px)//2
    Qx = Px[:half_n] #left half of Px (sorted by x)
    Rx = Px[half_n:] #right half of Px (sorted by y)
    Qy = [point for point in Py if point in Qx] #left half of Px sorted by y
    Ry = [point for point in Py if point in Rx] #right half of Px sorted by y

    #Conquer
    p1q1 = closest_pair_recursion(Qx, Qy)
    p2q2 = closest_pair_recursion(Rx, Ry)
    delta = min(get_distance(p1q1), get_distance(p2q2))
    p3q3 = closest_split_pair(Px, Py, delta)
    # p3q3 = None

    # Combine: select pair with minimum distance
    closest_pair = None
    for pair in [p1q1, p2q2, p3q3]:
        if get_distance(pair) < get_distance(closest_pair):
            closest_pair = pair
    return closest_pair

def closest_split_pair(Px, Py, delta):
    """
    computes closest pair that straddle the Px median (split pair)
    :param Px: P sorted by x
    :param Py: P sorted by y
    :param delta: min distance of the closest pairs in the left and right
    halves of Px that don't straddle the median (non-split pairs)
    :return: closest_split_pair only if it's distance smaller than the non_split pairs
    """
    median_x = Px[len(Px)//2 -1].x
    left_x_limit = median_x - delta
    right_x_limit = median_x + delta
    S = [point for point in Px if point.x > left_x_limit and point.x < right_x_limit]
    Sy = [point for point in Py if point in S]

    min_distance = delta
    closest_pair = None
    for i in range(1, len(Sy) - 1):
        for j in range(1, min(7, len(Sy) - i)):
            pair = (Sy[i], Sy[i+j])
    # for i in range(len(Sy) -1):
    #     for j in range(i + 1,len(Sy)):
    #         pair = (Sy[i], Sy[j])
            if get_distance(pair) < min_distance:
                closest_pair = pair
    # print(f"closest pair: {closest_pair}")
    return closest_pair

def get_distance(pair):
    """ computes Eucliden distance"""
    if pair is None:
        return math.inf
    p1 = pair[0]
    p2 = pair[1]
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force_closest_pair(P):
    """brute force algorithm for closest_pair O(n^2)"""
    closest_pair = (P[0], P[1])
    min_distance = get_distance(closest_pair)
    for i in range(len(P) - 1):
        for j in range(i + 1, len(P)):
            if get_distance((P[i], P[j]))  < min_distance:
                closest_pair = (P[i], P[j])
                min_distance = get_distance((P[i], P[j]))
    return closest_pair

def print_list(l):
    """Prints string representation of a list of point objects"""
    for p in l:
        print(p, end=", ")
    print()

# _______________________________________________________
# Tests
points = list(set(Point.make_random_points(100)))
print_list(points)
print('________________________________________________')
print_list (find_closest_pair(points))
print(f'recursive distance: {get_distance(find_closest_pair(points))}')
print('________________________________________________')
print_list(brute_force_closest_pair(points))
print(f'brute force distance: {get_distance(brute_force_closest_pair(points))}')
