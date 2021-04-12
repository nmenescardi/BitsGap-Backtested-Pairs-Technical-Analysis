from abc import ABC, abstractmethod

class AbstractIndicator(ABC):
    def __init__(self, data_provider):
        self.data_provider = data_provider


    @abstractmethod
    def calculate(self, **kwargs):
        pass
