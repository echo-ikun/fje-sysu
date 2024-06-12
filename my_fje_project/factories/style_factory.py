from abc import ABC, abstractmethod

class StyleFactory(ABC):
    @abstractmethod
    def create_style(self):
        pass
