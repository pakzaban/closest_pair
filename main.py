from Point import Point
from MergeSort import merge_sort_points_by
import math

def find_closest_pair(P):
    """
    Pre-processes the list of points and returns to sorted lists
    :returns (Px: points sorted by x, Py: poits sorted by y)
    """
    Px = merge_sort_points_by(points, x=True)
    Py = merge_sort_points_by(points, x=False)
    # print_list(Px)
    # print(closest_split_pair(Px,Py,10)[0])
    # print_list(closest_split_pair(Px,Py,10)[1])
    return closest_pair_recursion(Px, Py)

def closest_pair_recursion(Px, Py):
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
    (p1, q1) = closest_pair_recursion(Qx, Qy)
    (p2, q2) = closest_pair_recursion(Rx, Ry)
    delta = min(get_distance((p1,q1)), get_distance((p2,q2)))
    (p3, q3) = closest_split_pair(Px, Py, delta)
    # (p3, q3) = (p2, q2)


    # Combine: select pair with minimum distance
    closest_pair = (p1, q1)
    for pair in [(p2, q2), (p3, q3)]:
        if get_distance(pair) < get_distance(closest_pair):
            closest_pair = pair

    return(closest_pair)

def closest_split_pair(Px, Py, delta):
    median_x = Px[len(Px)//2 -1].x
    left_x_limit = median_x - delta/2
    right_x_limit = median_x + delta/2
    S = [point for point in Px if point.x > left_x_limit and point.x < right_x_limit]
    Sy = [point for point in Py if point in S]
    print("Sy")
    print_list(Sy)

    min_distance = delta
    closest_pair = None
    for i in range(len(Sy) - 2):
        for j in range(min(7,len(Sy)-2)):
            pair = (Sy[i], Sy[i+j])
            if get_distance(pair) < min_distance:
                closest_pair = pair
    print(f"closest pair: {closest_pair}")
    return closest_pair

def get_distance(pair):
    p1 = pair[0]
    p2 = pair[1]
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force_closest_pair(P):
    closest_pair = (P[0], P[1])
    min_distance = get_distance(closest_pair)
    for i in range(len(P) - 1):
        for j in range(i + 1, len(P)):
            if get_distance((P[i], P[j]))  < min_distance:
                closest_pair = (P[i], P[j])
    return closest_pair

def print_list(l):
    for p in l:
        print(p, end=", ")
    print()

points = Point.make_random_points(10)
print_list(points)
print_list (find_closest_pair(points))
print_list(brute_force_closest_pair(points))

