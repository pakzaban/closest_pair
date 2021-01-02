"""
Merge sort algorithm modified to sort points by x or y coordinate
"""
def merge(list1, list2, x):
    """
    merges 2 ordered list of points by x or y coordinate
    :param list1, list2: list of point objects
    :param x: Boolean: if true, sorts by x; else, by y.
    :return: merged ordered list of points by x or y coordinate
    """
    result = []
    while len(list1) > 0 and len(list2) > 0:
        if x:
            if list1[0].x <= list2[0].x:
                result.append(list1.pop(0))
            elif list2[0].x <= list1[0].x:
                result.append(list2.pop(0))
            else:
                result.append(list1.pop(0))
                result.append(list2.pop(0))
        else:
            if list1[0].y <= list2[0].y:
                result.append(list1.pop(0))
            elif list2[0].y <= list1[0].y:
                result.append(list2.pop(0))
            else:
                result.append(list1.pop(0))
                result.append(list2.pop(0))
    result = result + list1 + list2
    return result

def merge_sort_points_by(unordered_list, x=True):
    """
    Recursive divide and conquer algorithm
    :param unordered_list: [Point(x,y)]
    :param x: Boolean: if true, sorts by x; else, by y.
    :return: ordered_list
    """
    #base_case:
    if len(unordered_list) <= 1:
        return unordered_list
    #recursive step
    half_n = len(unordered_list)//2
    left_half = unordered_list[:half_n]
    right_half = unordered_list[half_n:]
    sorted_left = merge_sort_points_by(left_half, x)
    sorted_right = merge_sort_points_by(right_half, x)
    return merge(sorted_left,sorted_right, x)