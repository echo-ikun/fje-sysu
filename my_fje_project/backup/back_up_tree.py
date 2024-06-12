## 展示树的备份代码（现已修改为组合模式）

import json
from styles.style import Style

class TreeStyle(Style):
    def display( self, data, icon_family):
        icon = icon_family.get_icon()
        print_tree(data, icon)

class Tree_Node:
    def __init__(self, name, syntax="null", children=None):
        self.name = name
        self.syntax = syntax
        self.children = children if children is not None else []

    def display_node(self, icon, prefix="", is_last=True):
        # 1. 只有最后一个显示会是 └─， 否则是 ├─
        connector = "└─" if is_last else "├─"

        line = prefix + connector + icon + self.name

        if self.syntax != "null":
            line += ": " + self.syntax
        print(line)

        if self.children:
            new_prefix = prefix + ("    " if is_last else "│   ") # 这一句只会约束 初始传入的最后一个节点
            for i, child in enumerate(self.children):
                is_child_last = i == len(self.children) - 1
                child.display_node(icon, new_prefix, is_child_last)



def json_to_nodes(name, data):
    if not isinstance(data, dict):
        if data :
            return Tree_Node(name, syntax=data, children=None)
        else:
            return Tree_Node(name, syntax="null", children=None)
    else:
        children = []
        for key, value in data.items():
            child_node = json_to_nodes(key, value)
            children.append(child_node)
        return Tree_Node(name, syntax="null", children=children)



def print_tree(data, icon):
    # 转换JSON数据为树形结构
    nodes = [json_to_nodes(k, v) for k, v in data.items()]

    # 打印树形结构
    for i, node in enumerate(nodes):
        is_last = i == len(nodes) - 1
        node.display_node(icon, "", is_last)