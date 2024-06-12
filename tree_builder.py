from node import Node


class TreeBuilder:
    def __init__(self):
        self.root = None

    def build_tree(self, json_obj):
        self.root = Node("root")  # 创建一个虚拟的根节点
        for k, v in json_obj.items():
            self.root.add_child(self._build_node(k, v))
        return self

    def _build_node(self, name, value):
        node = Node(name, None if isinstance(value, dict) else value)
        if isinstance(value, dict):
            for k, v in value.items():
                node.add_child(self._build_node(k, v))
        return node

    def get_tree(self):
        return self.root
