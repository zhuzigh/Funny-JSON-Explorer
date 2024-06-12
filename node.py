class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, indent=0, icon_family=None, is_last=True):
        icon = icon_family.get_icon(self) if icon_family else ""
        prefix = "│  " * indent + ("└─ " if is_last else "├─ ")
        print(prefix + icon + self.name + (": " + self.value if self.value else ""))
        for i, child in enumerate(self.children):
            child.display(
                indent + 1, icon_family, is_last=(i == len(self.children) - 1)
            )

    def display_rectangle(self, icon_family=None, level=0, is_last=False):
        icon = icon_family.get_icon(self) if icon_family else ""
        if level == 0:
            prefix = "┌─ " if len(self.children) > 0 else "└─ "
        else:
            prefix = "│  " * (level - 1) + ("└─ " if is_last else "├─ ")
        suffix = " ───────────────────────────" if len(self.children) > 0 else ""
        print(
            prefix
            + icon
            + self.name
            + (": " + self.value if self.value else "")
            + suffix
        )
        for i, child in enumerate(self.children):
            child.display_rectangle(
                icon_family, level + 1, is_last=(i == len(self.children) - 1)
            )
