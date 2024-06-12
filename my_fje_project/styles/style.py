from abc import ABC, abstractmethod

class Style(ABC):
    @abstractmethod
    def display(self, data, icon_family):
        pass