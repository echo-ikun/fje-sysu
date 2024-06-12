import json
from styles.style import Style


class RectangleStyle(Style):
    def display( self, data, icon_family:str):
        icon = icon_family.get_icon()
        print_rectangle(data, icon)


class Rect_Node:
    def __init__(self, name, syntax="null", children=None):
        self.name = name
        self.syntax = syntax
        self.children = children if children is not None else []

    def display_node(self, prefix="", is_last=False, is_bottom=False, count=0, icon=""): # count表示是顶部还是底部，底部为 1
        if is_bottom:
            connector = "└──┴──" + icon
        else:
            connector = "└─"+icon if is_last else "├─"+icon
        line = prefix + connector + self.name
        if self.syntax != "null":
            line += ": " + self.syntax

        if is_bottom:
            if count == 1: # 如果此时画的是底部 并且还是最后一个（is_bottom=1 ）
                line += " " + "─" * (45 - len(prefix) - len(connector) - len(self.name) - (len(self.syntax) + 2 if self.syntax != "null" else 0)) + "┘"
            else:
                line += " " + "─" * (45 - len(prefix) - len(connector) - len(self.name) - (len(self.syntax) + 2 if self.syntax != "null" else 0)) + "┤"
        else:
            line += " " + "─" * (45 - len(prefix) - len(connector) - len(self.name) - (len(self.syntax) + 2 if self.syntax != "null" else 0)) + "┤"
        print(line)

        if self.children:
            new_prefix = prefix + ("   " if is_last else "│  ")
            for i, child in enumerate(self.children):
                is_child_last = i == len(self.children) - 1
                child.display_node(new_prefix, is_child_last, is_bottom, 0, icon)


def json_to_nodes(name, data):
    if isinstance(data, dict):
        children = [json_to_nodes(k, v) for k, v in data.items()]
        return Rect_Node(name, children=children)
    elif data is None:
        return Rect_Node(name)
    else:
        return Rect_Node(name, syntax=data)


def print_rectangle(data, icon_family):

    # icon = icon_family.get_icon(value)
    icon = icon_family

    nodes = [json_to_nodes(k, v) for k, v in data.items()]

    if nodes:
        # 上边框
        top_node = nodes[0]
        print("┌──" + icon + top_node.name + " " + "─" * (44 - len(top_node.name) - 3) + "┐")
        for child in top_node.children:
            child.display_node("│  ", False, False, 0, icon)

        # # 打印中间的节点
        for node in nodes[1:-1]:
            print("├──"+ icon + node.name + " " + "─" * (44 - len(node.name) - 3) + "┤")
            for child in node.children:
                child.display_node("│  ", False, 0, icon)

        # 下边框
        bottom_node = nodes[-1]
        print("├──" + icon + bottom_node.name + " " + "─" * (44 - len(bottom_node.name) - 3) + "┤")
        for i, child in enumerate(bottom_node.children):
            is_last_child = (i == len(bottom_node.children) - 1)
            if is_last_child == 0:
                child.display_node("", is_last_child, True, 0, icon )
            else:
                child.display_node("", is_last_child, True, 1, icon)



if __name__ == "__main__":
   # main()
    with open("test2.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    display(data, "*")
