from abc import ABC, abstractmethod

class IconFamily(ABC):
    @abstractmethod
    def get_icon(self, value):
        pass


# import json
# from abc import ABC, abstractmethod
#
#
# class IconFamily(ABC):
#     @abstractmethod
#     def get_icon(self, value):
#         pass
#
#
# class ConfigurableIconFamily(IconFamily):
#     def __init__(self, config_file):
#         with open(config_file, 'r') as file:
#             self.config = json.load(file)
#
#     def get_icon(self, value):
#         icon_path = self.config.get('icons', {}).get(value)
#         if icon_path:
#             return f"Loading icon from {icon_path}"
#         else:
#             return "Icon not found"
#
#
# # 使用示例
# icon_family = ConfigurableIconFamily('icons_config.json')
# print(icon_family.get_icon('home'))  # 输出: Loading icon from path/to/home/icon.png
# print(icon_family.get_icon('settings'))  # 输出: Loading icon from path/to/settings/icon.png
# print(icon_family.get_icon('non_existing'))  # 输出: Icon not found
