from Data.AbstractDAO import AbstractDAO

class Batches(AbstractDAO):

    def __init__(self):
        super(Batches, self).__init__()


    def new(self): 
        result = self.execute(
            """
                INSERT INTO batches VALUES ();
            """
        )
        self.db.commit()
        
        return result.lastrowid


    def get_lastest(self):
        pass #TODO query latest batch