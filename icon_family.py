class IconFamily:
    def __init__(self, middle_icon, leaf_icon):
        self.middle_icon = middle_icon
        self.leaf_icon = leaf_icon

    def get_icon(self, node):
        return self.middle_icon if node.children else self.leaf_icon
