import unittest
from kdtree import KdTree
from node import Node, NodeType


class TestKdTree(unittest.TestCase):

    def setUp(self):

        """This is called immediately before calling every test method"""

        # ODD CASE
        self.points_odd = [[2, 4], [-1, 5], [3, -3], [6, 1], [1, 2]]
        self.points_odd_sorted_x = [[-1, 5], [1, 2], [2, 4], [3, -3], [6, 1]]
        self.points_odd_sorted_y = [[3, -3], [6, 1], [1, 2], [2, 4], [-1, 5]]
        self.kd_tree_odd = KdTree(self.points_odd)

        # EVEN CASE
        self.points_even = [[2, 4], [-1, 5], [3, -3], [1, 2]]
        self.points_even_sorted_x = [[-1, 5], [1, 2], [2, 4], [3, -3]]
        self.points_even_sorted_y = [[3, -3], [1, 2], [2, 4], [-1, 5]]
        self.kd_tree_even = KdTree(self.points_even)

        # QUERY TO SEARCH IN THE KD-TREE
        self.query_x = [1, 3]
        self.query_y = [2, 4]

        # BUILDING A KD-TREE
        # LEVEL 4 KD_TREE
        self.node_level_4_1 = Node()
        self.node_level_4_1.type = NodeType.LEAF
        self.node_level_4_1.level = 4
        self.node_level_4_1.cut = None
        self.node_level_4_1.point = [3, 1]
        self.node_level_4_1.left_child = None
        self.node_level_4_1.right_child = None

        self.node_level_4_2 = Node()
        self.node_level_4_2.type = NodeType.LEAF
        self.node_level_4_2.level = 4
        self.node_level_4_2.cut = None
        self.node_level_4_2.point = [1, 2]
        self.node_level_4_2.left_child = None
        self.node_level_4_2.right_child = None

        # LEVEL 3 KD_TREE
        self.node_level_3_1 = Node()
        self.node_level_3_1.type = NodeType.INTERNAL
        self.node_level_3_1.level = 3
        self.node_level_3_1.cut = 1
        self.node_level_3_1.point = None
        self.node_level_3_1.left_child = self.node_level_4_1
        self.node_level_3_1.right_child = self.node_level_4_2

        self.node_level_3_2 = Node()
        self.node_level_3_2.type = NodeType.LEAF
        self.node_level_3_2.level = 3
        self.node_level_3_2.cut = None
        self.node_level_3_2.point = [4, 5]
        self.node_level_3_2.left_child = None
        self.node_level_3_2.right_child = None

        self.node_level_3_3 = Node()
        self.node_level_3_3.type = NodeType.LEAF
        self.node_level_3_3.level = 3
        self.node_level_3_3.cut = None
        self.node_level_3_3.point = [2, 6]
        self.node_level_3_3.left_child = None
        self.node_level_3_3.right_child = None

        self.node_level_3_4 = Node()
        self.node_level_3_4.type = NodeType.LEAF
        self.node_level_3_4.level = 3
        self.node_level_3_4.cut = None
        self.node_level_3_4.point = [5, 7]
        self.node_level_3_4.left_child = None
        self.node_level_3_4.right_child = None

        self.node_level_3_5 = Node()
        self.node_level_3_5.type = NodeType.LEAF
        self.node_level_3_5.level = 3
        self.node_level_3_5.cut = None
        self.node_level_3_5.point = [6, 3]
        self.node_level_3_5.left_child = None
        self.node_level_3_5.right_child = None

        self.node_level_3_6 = Node()
        self.node_level_3_6.type = NodeType.LEAF
        self.node_level_3_6.level = 3
        self.node_level_3_6.cut = None
        self.node_level_3_6.point = [8, 4]
        self.node_level_3_6.left_child = None
        self.node_level_3_6.right_child = None

        self.node_level_3_7 = Node()
        self.node_level_3_7.type = NodeType.LEAF
        self.node_level_3_7.level = 3
        self.node_level_3_7.cut = None
        self.node_level_3_7.point = [7, 8]
        self.node_level_3_7.left_child = None
        self.node_level_3_7.right_child = None

        self.node_level_3_8 = Node()
        self.node_level_3_8.type = NodeType.LEAF
        self.node_level_3_8.level = 3
        self.node_level_3_8.cut = None
        self.node_level_3_8.point = [9, 9]
        self.node_level_3_8.left_child = None
        self.node_level_3_8.right_child = None

        # LEVEL 2 KD_TREE
        self.node_level_2_1 = Node()
        self.node_level_2_1.type = NodeType.INTERNAL
        self.node_level_2_1.level = 2
        self.node_level_2_1.cut = 3
        self.node_level_2_1.point = None
        self.node_level_2_1.left_child = self.node_level_3_1
        self.node_level_2_1.right_child = self.node_level_3_2

        self.node_level_2_2 = Node()
        self.node_level_2_2.type = NodeType.INTERNAL
        self.node_level_2_2.level = 2
        self.node_level_2_2.cut = 2
        self.node_level_2_2.point = None
        self.node_level_2_2.left_child = self.node_level_3_3
        self.node_level_2_2.right_child = self.node_level_3_4

        self.node_level_2_3 = Node()
        self.node_level_2_3.type = NodeType.INTERNAL
        self.node_level_2_3.level = 2
        self.node_level_2_3.cut = 6
        self.node_level_2_3.point = None
        self.node_level_2_3.left_child = self.node_level_3_5
        self.node_level_2_3.right_child = self.node_level_3_6

        self.node_level_2_4 = Node()
        self.node_level_2_4.type = NodeType.INTERNAL
        self.node_level_2_4.level = 2
        self.node_level_2_4.cut = 7
        self.node_level_2_4.point = None
        self.node_level_2_4.left_child = self.node_level_3_7
        self.node_level_2_4.right_child = self.node_level_3_8

        # LEVEL 1 KD_TREE
        self.node_level_1_1 = Node()
        self.node_level_1_1.type = NodeType.INTERNAL
        self.node_level_1_1.level = 1
        self.node_level_1_1.cut = 5
        self.node_level_1_1.point = None
        self.node_level_1_1.left_child = self.node_level_2_1
        self.node_level_1_1.right_child = self.node_level_2_2

        self.node_level_1_2 = Node()
        self.node_level_1_2.type = NodeType.INTERNAL
        self.node_level_1_2.level = 1
        self.node_level_1_2.cut = 4
        self.node_level_1_2.point = None
        self.node_level_1_2.left_child = self.node_level_2_3
        self.node_level_1_2.right_child = self.node_level_2_4

        # LEVEL 0 KD_TREE
        self.root_node = Node()
        self.root_node.type = NodeType.INTERNAL
        self.root_node.level = 0
        self.root_node.cut = 5
        self.root_node.point = None
        self.root_node.left_child = self.node_level_1_1
        self.root_node.right_child = self.node_level_1_2

        self.points = [[1, 2], [2, 6], [3, 1], [4, 5], [5, 7], [6, 3], [7, 8], [8, 4], [9, 9]]
        self.kd_tree = KdTree(self.points)
        self.kd_tree.root_node = self.root_node

    def test_sort_points(self):

        """Test if the sorted list is like expected"""

        # ODD CASE
        result_odd_x, result_odd_y = KdTree._sort_points(self.kd_tree_odd, self.points_odd)
        self.assertListEqual(self.points_odd_sorted_x, result_odd_x)
        self.assertListEqual(self.points_odd_sorted_y, result_odd_y)

        # EVEN CASE
        result_even_sorted_x, result_even_sorted_y = KdTree._sort_points(self.kd_tree_even, self.points_even)
        self.assertListEqual(self.points_even_sorted_x, result_even_sorted_x)
        self.assertListEqual(self.points_even_sorted_y, result_even_sorted_y)

    def test_get_index_median(self):

        """Test if the median returned is correct"""

        # ODD CASE
        self.assertEqual(KdTree._get_index_median(self.kd_tree_odd, self.points_odd), 3)

        # EVEN CASE
        self.assertEqual(KdTree._get_index_median(self.kd_tree_even, self.points_even), 2)

    def test_split_points(self):

        """Test if the splitted list is like expected"""

        # ODD CASE CUT BY X ON THE SORTED Y LIST
        left_points_1 = [[3, -3], [1, 2], [2, 4], [-1, 5]]
        right_points_1 = [[6, 1]]
        result_left_points_odd_1, result_right_points_odd_1 = \
            KdTree._split_points(self.kd_tree_odd, self.points_odd_sorted_y, [3, -3], 0)

        self.assertListEqual(result_left_points_odd_1, left_points_1)
        self.assertListEqual(result_right_points_odd_1, right_points_1)

        # EVEN CASE CUT BY X ON THE SORTED Y LIST
        left_points_2 = [[1, 2], [2, 4], [-1, 5]]
        right_points_2 = [[3, -3]]
        result_left_points_even_1, result_right_points_even_1 = \
            KdTree._split_points(self.kd_tree_even, self.points_even_sorted_y, [2, 4], 0)

        self.assertListEqual(result_left_points_even_1, left_points_2)
        self.assertListEqual(result_right_points_even_1, right_points_2)

        # ODD CASE CUT BY Y ON THE SORTED X LIST
        left_points_3 = [[1, 2], [2, 4], [3, -3], [6, 1]]
        right_points_3 = [[-1, 5]]
        result_left_points_odd_2, result_right_points_odd_2 = \
            KdTree._split_points(self.kd_tree_odd, self.points_odd_sorted_x, [2, 4], 1)

        self.assertListEqual(result_left_points_odd_2, left_points_3)
        self.assertListEqual(result_right_points_odd_2, right_points_3)

        # EVEN CASE CUT BY Y ON THE SORTED X LIST
        left_points_4 = [[1, 2], [2, 4], [3, -3]]
        right_points_4 = [[-1, 5]]
        result_left_points_even_2, result_right_points_even_2 = \
            KdTree._split_points(self.kd_tree_even, self.points_even_sorted_x, [2, 4], 1)

        self.assertListEqual(result_left_points_even_2, left_points_4)
        self.assertListEqual(result_right_points_even_2, right_points_4)

    def test_is_valid_leaf(self):

        """Test if a node is a valid leaf"""

        node_1 = Node()
        node_1.point = [2, 4]
        node_2 = Node()
        node_2.point = [3, -3]
        node_3 = Node()
        node_3.point = [3, 4]
        node_4 = Node()
        node_4.point = [-1, 6]

        self.assertTrue(KdTree._is_valid_leaf(self.kd_tree_even, node_1, self.query_x, self.query_y))
        self.assertFalse(KdTree._is_valid_leaf(self.kd_tree_even, node_2, self.query_x, self.query_y))
        self.assertTrue(KdTree._is_valid_leaf(self.kd_tree_even, node_3, self.query_x, self.query_y))
        self.assertFalse(KdTree._is_valid_leaf(self.kd_tree_even, node_4, self.query_x, self.query_y))

    def test_is_fully_contained(self):

        """Test if all the leafs of a region is being returned"""

        region_x_1 = [None, None]
        region_y_1 = [None, None]
        self.assertFalse(KdTree._is_fully_contained(self.kd_tree_even, region_x_1, region_y_1,
                                                    self.query_x, self.query_y))

        region_x_2 = [2, 3]
        region_y_2 = [2, None]
        self.assertFalse(KdTree._is_fully_contained(self.kd_tree_even, region_x_2, region_y_2,
                                                    self.query_x, self.query_y))

        region_x_3 = [2, 3]
        region_y_3 = [2, 5]
        self.assertFalse(KdTree._is_fully_contained(self.kd_tree_even, region_x_3, region_y_3,
                                                    self.query_x, self.query_y))

        region_x_4 = [2, 3]
        region_y_4 = [2, 3]
        self.assertTrue(KdTree._is_fully_contained(self.kd_tree_even, region_x_4, region_y_4,
                                                   self.query_x, self.query_y))

    def test_has_intersection(self):

        """Test if a point has intersection with a query"""

        point_1 = 3
        query = [1, 3]
        self.assertFalse(KdTree._has_intersection(self.kd_tree_even, point_1, query))

        point_2 = 2
        query = [1, 3]
        self.assertTrue(KdTree._has_intersection(self.kd_tree_even, point_2, query))

        point_3 = 1
        query = [1, 3]
        self.assertTrue(KdTree._has_intersection(self.kd_tree_even, point_3, query))

        point_4 = 0
        query = [1, 3]
        self.assertFalse(KdTree._has_intersection(self.kd_tree_even, point_4, query))

    def test_report_sub_tree(self):

        """Test if the points returned from a region are correct"""

        expected_tree = [[3, 1], [1, 2], [4, 5], [2, 6], [5, 7]]
        result = KdTree._report_sub_tree(self.kd_tree_even, self.node_level_1_1)

        self.assertListEqual(result, expected_tree)

    def test_build(self):

        """Test if we are building correctly the Kd-Tree"""

        kd_tree_generated_by_function = KdTree(self.points)
        kd_tree_generated_by_hand = self.kd_tree

        self.validate_node(kd_tree_generated_by_function.root_node, kd_tree_generated_by_hand.root_node)

    def validate_node(self, function_node, hand_node):
        self.assertEqual(function_node.type, hand_node.type)

        if function_node.type == NodeType.INTERNAL:
            self.assertEqual(function_node.level, hand_node.level)

            self.assertEqual(function_node.cut, hand_node.cut)

            self.assertIsNone(function_node.point)
            self.assertIsNone(hand_node.point)

            self.assertIsNotNone(function_node.left_child)
            self.assertIsNotNone(hand_node.left_child)

            self.assertIsNotNone(function_node.right_child)
            self.assertIsNotNone(hand_node.right_child)

            self.validate_node(function_node.left_child, hand_node.left_child)
            self.validate_node(function_node.right_child, hand_node.right_child)
        elif function_node.type == NodeType.LEAF:
            self.assertEqual(function_node.level, hand_node.level)

            self.assertIsNone(function_node.cut)
            self.assertIsNone(hand_node.cut)

            self.assertListEqual(function_node.point, hand_node.point)

            self.assertIsNone(function_node.left_child)
            self.assertIsNone(hand_node.left_child)

            self.assertIsNone(function_node.right_child)
            self.assertIsNone(hand_node.right_child)
        else:
            raise Exception("NodeType has wrong value.")

    def test_search(self):

        """Test if the search result is correct"""

        region_x_1 = [None, None]
        region_y_1 = [None, None]
        query_x_1 = [1, 6]
        query_y_1 = [1, 4]
        expected_result_1 = [[3, 1], [1, 2], [6, 3]]
        result_1 = KdTree.search(self.kd_tree, query_x_1, query_y_1, region_x_1, region_y_1)
        self.assertListEqual(result_1, expected_result_1)

        region_x_2 = [None, None]
        region_y_2 = [None, None]
        query_x_2 = [2, 8]
        query_y_2 = [4, 8]
        expected_result_2 = [[4, 5], [2, 6], [5, 7], [8, 4], [7, 8]]
        result_2 = KdTree.search(self.kd_tree, query_x_2, query_y_2, region_x_2, region_y_2)
        self.assertListEqual(result_2, expected_result_2)


if __name__ == '__main__':
    unittest.main()
