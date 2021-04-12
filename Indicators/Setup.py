import os
from Helpers.SubclassesOf import SubclassesOf
from Indicators.AbstractIndicator import AbstractIndicator

class Setup():
        
    def get_config(self):
        
        current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        
        indicators = SubclassesOf(
            parent_class = AbstractIndicator,
            in_directory = current_dir,
        ).get_list()

        return indicators
