from abc import ABC, abstractmethod

class AbstractJob(ABC):
    
    @abstractmethod
    def run(self):
        pass
