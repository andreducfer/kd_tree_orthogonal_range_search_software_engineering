from enum import Enum


class NodeType(Enum):
    INTERNAL = 0
    LEAF = 1


class Node:
    def __init__(self):
        self.type = NodeType.INTERNAL
        self.level = 0
        self.cut = None
        self.point = None
        self.left_child = None
        self.right_child = None
