from factories.style_factory import StyleFactory
from styles.tree_style import TreeStyle


class TreeStyleFactory(StyleFactory):
    def create_style(self):
        return TreeStyle()
