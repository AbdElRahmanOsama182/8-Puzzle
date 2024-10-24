from abc import ABC, abstractmethod

class Heuristic(ABC):
    @abstractmethod
    def heuristic(self):
        pass