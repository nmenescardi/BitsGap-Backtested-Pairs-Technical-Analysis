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
        
        cursor = self.execute("SELECT batch_id FROM batches ORDER BY created_date DESC LIMIT 1;")

        batch_id_result = cursor.fetchone()
        if batch_id_result is None:
            return None #TODO: raise custom exception

        return batch_id_result[0]
