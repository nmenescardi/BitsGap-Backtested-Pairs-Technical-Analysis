import os
from Helpers.SubclassesOf import SubclassesOf
from Indicators.AbstractIndicator import AbstractIndicator

class Setup():
    
    def __init__(self):
        self.indicators = []

    def get_config(self):
        if len(self.indicators) > 0:
            return self.indicators

        current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        
        self.indicators = SubclassesOf(
            parent_class = AbstractIndicator,
            in_directory = current_dir,
        ).get_list()

        return self.indicators
