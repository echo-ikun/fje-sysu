import json
from styles.style import Style

class TreeStyle(Style):
    def display( self, data, icon_family):
        icon = icon_family.get_icon()
        print_tree(data, icon)


class Component:
    def display_node(self, icon, prefix="", is_last=True):
        raise NotImplementedError("You should implement this method")


class Composite_Node(Component):
    def __init__(self, name, syntax="null", children=None):
        self.name = name
        self.syntax = syntax
        self.children = children if children is not None else []

    def display_node(self, icon, prefix="", is_last=True):
        connector = "└─" if is_last else "├─"
        line = prefix + connector + icon + self.name
        if self.syntax != "null":
            line += ": " + self.syntax
        print(line)

        if self.children:
            new_prefix = prefix + ("    " if is_last else "│   ") # 只有最后一个不用加 横杠， 其他都需要，并且基础prefix是不断类加的
            for i, child in enumerate(self.children):
                is_child_last = i == len(self.children) - 1
                child.display_node(icon, new_prefix, is_child_last)


class Leaf_Node(Component):
    def __init__(self, name, syntax="null"):
        self.name = name
        self.syntax = syntax

    def display_node(self, icon, prefix="", is_last=True):
        connector = "└─" if is_last else "├─"
        line = prefix + connector + icon + self.name
        if self.syntax != "null":
            line += ": " + self.syntax
        print(line)




def json_to_nodes(name, data):
    # 叶子节点
    if not isinstance(data, dict):
        return Leaf_Node(name, data if data  else "null")
    # 复合节点
    else:
        children = []
        for key, value in data.items():
            child_node = json_to_nodes(key, value)
            children.append(child_node)  # children列表存的是 “结点”，eg：composite->composite->leaf
        return Composite_Node(name, syntax="null", children=children)


def print_tree(data, icon):
    # 转换JSON数据为树形结构
    nodes = [json_to_nodes(k, v) for k, v in data.items()]


    # 打印树形结构
    for i, node in enumerate(nodes):
        is_last = i == len(nodes) - 1
        node.display_node(icon, "", is_last)