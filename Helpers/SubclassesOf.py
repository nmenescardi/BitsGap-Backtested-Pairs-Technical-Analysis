import glob, importlib, inspect, os

class SubclassesOf:
    
    def __init__(self, parent_class, in_directory ):
        self.parent_class = parent_class
        self.in_directory = in_directory
    
    def get_list(self):
        subclasses = []
        
        current_module_name = os.path.splitext(os.path.basename( self.in_directory ))[0]
        for file in glob.glob(self.in_directory  + "/*.py"):
            name = os.path.splitext(os.path.basename(file))[0]

            # Ignore __ files
            if name.startswith("__"):
                continue

            module = importlib.import_module("." + name, package=current_module_name)

            for member in dir(module):
                handler_class = getattr(module, member)

                if handler_class and inspect.isclass(handler_class):
                    if issubclass(handler_class,  self.parent_class) and handler_class !=  self.parent_class:
                        subclasses.append(handler_class)

        return subclasses
        