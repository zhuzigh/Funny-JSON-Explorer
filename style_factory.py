from abc import ABC, abstractmethod
from tree_builder import TreeBuilder


class TreeFactory(ABC):
    @abstractmethod
    def create_tree(self, json_obj):
        pass


class TreeStyleFactory(TreeFactory):
    def create_tree(self, json_obj):
        builder = TreeBuilder()
        builder.build_tree(json_obj)
        return builder.get_tree()


class RectangleStyleFactory(TreeFactory):
    def create_tree(self, json_obj):
        builder = TreeBuilder()
        builder.build_tree(json_obj)
        return builder.get_tree()
