import argparse
from json_parser import Jsonparser
from factories.tree_style_factory import TreeStyleFactory
from factories.rectangle_style_factory import RectangleStyleFactory
from icons.poker_face_icon_family import PokerFaceIconFamily
from icons.mod_icon_family import ModIconFamily
from icons.star_icon_family import StarIconFamily
from icons.empty_icon_family import EmptyIconFamily


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Funny JSON Explorer")
    parser.add_argument('-f', '--file', required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', required=True, choices=['tree', 'rectangle'], help='Style to display the JSON')
    parser.add_argument('-i', '--icon',  choices=['poker','star','mod',],default=' ', help='Icon family to use')

    args = parser.parse_args()

    json_parser = Jsonparser(args.file)
    data = json_parser.get_data()

    if args.style == 'tree':
        style_factory = TreeStyleFactory()
    elif args.style == 'rectangle':
        style_factory = RectangleStyleFactory()

    style = style_factory.create_style()

    if args.icon == 'poker':
        icon_family = PokerFaceIconFamily()
    elif args.icon == 'star':
        icon_family = StarIconFamily()
    elif args.icon == 'mod':
        icon_family = ModIconFamily()
    else:
        icon_family = EmptyIconFamily()


    style.display(data, icon_family)

