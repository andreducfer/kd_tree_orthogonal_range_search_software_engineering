from node import Node, NodeType


class KdTree:

    """This class builds a Kd-Tree and enables orthogonal search in this tree"""

    def __init__(self, points):
        points_sorted_x, points_sorted_y = self._sort_points(points)
        self.root_node = self._build(points_sorted_x, points_sorted_y, depth=0)

    def _sort_points(self, points):

        """Return two lists, one sorted by x and other sorted by y"""

        points_sorted_x = sorted(points, key=lambda x: (x[0], x[1]))
        points_sorted_y = sorted(points, key=lambda x: (x[1], x[0]))

        return points_sorted_x, points_sorted_y

    def _get_index_median(self, points):

        """Return the index of the median of the given list"""

        if len(points) % 2 == 0:
            return len(points) / 2
        else:
            return (len(points) + 1) / 2

    def _split_points(self, points, median, depth):

        """Return two lists, splitted by the median"""

        left_points = []
        right_points = []

        if depth % 2 == 0:
            index_column = 0
        else:
            index_column = 1

        for point in points:
            if point[index_column] < median[index_column]:
                left_points.append(point)
            elif point[index_column] == median[index_column]:
                if point[index_column - 1] <= median[index_column - 1]:
                    left_points.append(point)
                else:
                    right_points.append(point)
            else:
                right_points.append(point)

        return left_points, right_points

    def _build(self, points_sorted_x, points_sorted_y, depth):

        """Build the Kd-Tree"""

        node = Node()

        # Select witch set of sorted points to use
        if depth % 2 == 0:
            points = points_sorted_x
        else:
            points = points_sorted_y

        if len(points) == 1:
            node.level = depth
            node.point = points[0]
            node.type = NodeType.LEAF
            node.cut = None

            return node
        elif depth % 2 == 0:
            index_median = int(self._get_index_median(points))

            p1_x = points[:index_median]
            p2_x = points[index_median:]

            p1_y, p2_y = self._split_points(points_sorted_y, p1_x[-1], depth)
        else:
            index_median = int(self._get_index_median(points))

            p1_y = points[:index_median]
            p2_y = points[index_median:]

            p1_x, p2_x = self._split_points(points_sorted_x, p1_y[-1], depth)

        node_left = self._build(p1_x, p1_y, depth + 1)
        node_right = self._build(p2_x, p2_y, depth + 1)

        node.type = NodeType.INTERNAL
        node.level = depth

        index_point = index_median - 1

        if depth % 2 == 0:
            node.cut = points[index_point][0]
        else:
            node.cut = points[index_point][1]

        node.left_child = node_left
        node.right_child = node_right

        return node

    def _is_valid_leaf(self, node, query_x, query_y):

        """Verify if a leaf is inside a search query"""

        is_valid_leaf = False

        if node.point[0] >= query_x[0] and node.point[0] <= query_x[1] and node.point[1] >= query_y[0] and node.point[
                1] <= query_y[1]:
            is_valid_leaf = True

        return is_valid_leaf

    def _is_fully_contained(self, region_x, region_y, query_x, query_y):

        """Verify if a region is inside the search query"""

        is_fully_contained = False

        if None in region_x + region_y:
            return is_fully_contained

        if region_x[0] >= query_x[0] and region_x[1] <= query_x[1] and region_y[0] >= query_y[0] and region_y[1] <= \
                query_y[1]:
            is_fully_contained = True

        return is_fully_contained

    def _has_intersection(self, point, query):

        """Verify if a point has intersection with a query"""

        has_intersection = False

        if point == query[1]:
            has_intersection = False
        elif point >= query[0] and point < query[1]:
            has_intersection = True

        return has_intersection

    def _report_sub_tree(self, node):

        """Return all the points that are on the leafs bellow this node"""

        elements = []

        if node.type == NodeType.LEAF:
            elements.append(node.point)
            return elements

        left_element = self._report_sub_tree(node.left_child)
        elements += left_element
        right_element = self._report_sub_tree(node.right_child)
        elements += right_element

        return elements

    def search(self, query_x, query_y, region_x, region_y, node='first_entry'):

        """Return all the points that are inside the query search"""

        if node == 'first_entry':
            node = self.root_node

        elements_to_return = []

        if node.type == NodeType.LEAF:
            if self._is_valid_leaf(node, query_x, query_y):
                elements_to_return.append(node.point)
        else:
            if node.level % 2 == 0:
                region_x_lc = [region_x[0], node.cut]
                region_y_lc = region_y
                region_x_rc = [node.cut, region_x[1]]
                region_y_rc = region_y
                query_intersection = query_x
            else:
                region_x_lc = region_x
                region_y_lc = [region_y[0], node.cut]
                region_x_rc = region_x
                region_y_rc = [node.cut, region_y[1]]
                query_intersection = query_y

            # LEFT CHILD SEARCH
            if self._is_fully_contained(region_x_lc, region_y_lc, query_x, query_y):
                elements = self._report_sub_tree(node.left_child)
                elements_to_return.extend(elements)
            elif self._has_intersection(node.cut, query_intersection) or node.cut >= query_intersection[1]:
                elements = self.search(query_x, query_y, region_x_lc, region_y_lc, node.left_child)
                elements_to_return.extend(elements)

            # RIGHT CHILD SEARCH
            if self._is_fully_contained(region_x_rc, region_y_rc, query_x, query_y):
                elements = self._report_sub_tree(node.right_child)
                elements_to_return.extend(elements)
            elif self._has_intersection(node.cut, query_intersection) or node.cut < query_intersection[0]:
                elements = self.search(query_x, query_y, region_x_rc, region_y_rc, node.right_child)
                elements_to_return.extend(elements)

        return elements_to_return

    def print(self, node='first_entry'):

        """Print the Kd-Tree"""

        if node == 'first_entry':
            node = self.root_node

        tab_char = '\t'

        if node is None:
            return

        print('%sLevel: %d' % (tab_char * node.level, node.level))
        if node.type == NodeType.LEAF:
            print('%sPoint: %s' % (
                tab_char * node.level, ', '.join([str(point_element) for point_element in node.point])))
        elif node.type == NodeType.INTERNAL:
            print('%sCut: %d' % (tab_char * node.level, node.cut))
        print('%s----> Left child' % (tab_char * node.level))
        self.print(node.left_child)
        print('%s----> Right child' % (tab_char * node.level))
        self.print(node.right_child)
