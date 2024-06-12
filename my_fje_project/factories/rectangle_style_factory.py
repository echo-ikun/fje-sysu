# from style_factory import StyleFactory
# from ..styles.rectangle_style import RectangleStyle

from factories.style_factory import StyleFactory
from styles.rectangle_style import RectangleStyle

class RectangleStyleFactory(StyleFactory):
    def create_style(self):
        return RectangleStyle()
