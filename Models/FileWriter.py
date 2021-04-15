
class FileWriter:
    
    def __init__(self, file_dir='./'):
        self.file_dir = file_dir


    def log(self, content):
        f = open(self.file_dir, "w")
        f.write(content)
        f.close()
