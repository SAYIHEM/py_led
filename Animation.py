from abc import ABC, abstractmethod

class Animation(ABC):

    PixelGroupList = list()

    def addPixelGroup(self, group):
        if group is None:
            print("todo")

    @abstractmethod
    def animate(self):
        pass