import json
from styles.style import Style

class RectangleStyle(Style):
    def display(self, data, icon_family):
        icon = icon_family.get_icon()
        print_rectangle(data, icon)

class NodeBuilder:
    def set_name(self, name):
        raise NotImplementedError

    def set_syntax(self, syntax):
        raise NotImplementedError

    def add_child(self, child):
        raise NotImplementedError

    def build(self):
        raise NotImplementedError

class RectNodeBuilder(NodeBuilder):
    def __init__(self):
        self.name = None
        self.syntax = "null"
        self.children = []

    def set_name(self, name):
        self.name = name
        return self

    def set_syntax(self, syntax):
        self.syntax = syntax
        return self

    def add_child(self, child):
        self.children.append(child)
        return self

    def build(self):
        return Rect_Node(self.name, self.syntax, self.children)

class Rect_Node:
    def __init__(self, name, syntax="null", children=None):
        self.name = name
        self.syntax = syntax
        self.children = children if children is not None else []

    def display_node(self, prefix="", is_last=False, is_bottom=False, count=0, icon=""):
        if is_bottom:
            connector = "└──┴──" + icon
        else:
            connector = "└─" + icon if is_last else "├─" + icon
        line = prefix + connector + self.name
        if self.syntax != "null":
            line += ": " + self.syntax

        if is_bottom:
            if count == 1:
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
    builder = RectNodeBuilder().set_name(name)
    if isinstance(data, dict):
        for k, v in data.items():
            child_node = json_to_nodes(k, v)
            builder.add_child(child_node)
        return builder.build()
    else:
        return builder.set_syntax(data if data is not None else "null").build()

def print_rectangle(data, icon_family):
    icon = icon_family

    nodes = [json_to_nodes(k, v) for k, v in data.items()]

    if nodes:
        top_node = nodes[0]
        print("┌──" + icon + top_node.name + " " + "─" * (44 - len(top_node.name) - 3) + "┐")
        for child in top_node.children:
            child.display_node("│  ", False, False, 0, icon)

        for node in nodes[1:-1]:
            print("├──" + icon + node.name + " " + "─" * (44 - len(node.name) - 3) + "┤")
            for child in node.children:
                child.display_node("│  ", False, 0, icon)

        bottom_node = nodes[-1]
        print("├──" + icon + bottom_node.name + " " + "─" * (44 - len(bottom_node.name) - 3) + "┤")
        for i, child in enumerate(bottom_node.children):
            is_last_child = (i == len(bottom_node.children) - 1)
            child.display_node("", is_last_child, True, 1 if is_last_child else 0, icon)

if __name__ == "__main__":
    with open("test2.json", "r") as file:
        data = json.load(file)
    print_rectangle(data, '*+')
