import random
from kdtree import KdTree


def generate_points(number_of_points):

    """In this function, we build the points list to be used to construct the Kd-Tree"""

    x = list(range(number_of_points))
    y = list(range(number_of_points))

    random.shuffle(x)
    random.shuffle(y)

    points = [list(a) for a in zip(x, y)]

    return points


def main():
    number_of_points = 1000
    points = generate_points(number_of_points)
    kd_tree = KdTree(points)

    # Query to search points
    query_x = [400, 500]
    query_y = [300, 400]
    region_x = [None, None]
    region_y = [None, None]

    search_result = kd_tree.search(query_x, query_y, region_x, region_y)
    print("The query:")
    print("X = [%d, %d]" % (query_x[0], query_x[1]))
    print("Y = [%d, %d]" % (query_y[0], query_y[1]))
    print("Returns:")
    print(search_result)
    print("######################################################################################################\n")

    # kd_tree.print()


main()
