from Data.AbstractDAO import AbstractDAO
from Data.Pairs import Pairs as PairsDAO
from Data.Batches import Batches as BatchesDAO

class Indicators(AbstractDAO):

    def __init__(self):
        super(Indicators, self).__init__()
        self.pairs_dao = PairsDAO()
        self.batches_dao = BatchesDAO()


    def insert(self, indicator): 
        # If IDs are empty -> fetch them
        if not indicator.has_pair_id():
            indicator.pair_id = self.pairs_dao.get_pair_id_by_symbol( indicator.symbol )

        if not indicator.has_batch_id():
            indicator.batch_id = self.batches_dao.get_lastest()

        self.execute(
            """
                INSERT IGNORE INTO indicators 
                    (pair_id, batch_id, indicator_key, indicator_value, timeframe)
                VALUES 
                    (%s,%s,%s,%s,%s);
            """,
            (indicator.pair_id, indicator.batch_id, indicator.key, indicator.value, indicator.timeframe, )
        )
        self.db.commit()
