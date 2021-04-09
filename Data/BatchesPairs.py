from Data.AbstractDAO import AbstractDAO

class BatchesPairs(AbstractDAO):

    def __init__(self):
        super(BatchesPairs, self).__init__()


    def insert(self, pair): 
        self.execute(
            """
                INSERT IGNORE INTO batches_pairs 
                    (pair_id, batch_id, profit, category)
                VALUES 
                    (%s,%s,%s,%s);
            """,
            (pair.pair_id, pair.batch_id, pair.profit, pair.category, )
        )
        self.db.commit()
