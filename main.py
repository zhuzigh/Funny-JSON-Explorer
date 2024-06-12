import json
from style_factory import TreeStyleFactory, RectangleStyleFactory
from icon_family import IconFamily


def main():
    json_data = """
    {
        "oranges": {
            "mandarin": {
                "clementine": null,
                "tangerine": "cheap & juicy!"
            }
        },
        "apples": {
            "gala": null,
            "pink lady": null
        }
    }
    """

    json_obj = json.loads(json_data)
    style = "tree"  # 'tree' or 'rectangle'
    icon_family_name = "poker-face-icon-family"

    # 创建风格工厂
    if style == "tree":
        factory = TreeStyleFactory()
    elif style == "rectangle":
        factory = RectangleStyleFactory()
    else:
        factory = TreeStyleFactory()

    # 创建图标族
    if icon_family_name == "poker-face-icon-family":
        icon_family = IconFamily(middle_icon="♢", leaf_icon="♤")
    if icon_family_name == "emoji":
        icon_family = IconFamily(middle_icon="😀", leaf_icon="😁")
    else:
        icon_family = IconFamily(middle_icon="-", leaf_icon=">")

    # 构建树
    tree = factory.create_tree(json_obj)

    # 展示树
    if style == "tree":
        for i, child in enumerate(tree.children):
            child.display(
                indent=0, icon_family=icon_family, is_last=(i == len(tree.children) - 1)
            )

    elif style == "rectangle":
        tree.display_rectangle(icon_family=icon_family)


if __name__ == "__main__":
    main()
