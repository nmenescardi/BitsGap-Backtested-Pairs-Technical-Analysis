from Data.AbstractDAO import AbstractDAO

class Pairs(AbstractDAO):

    def __init__(self):
        super(Pairs, self).__init__()
        self.pair_ids = {}


    def insert(self, payload):
        if hasattr(payload, '__iter__'):
            for pair in payload:
                self.__insert(pair)
        else:
            self.__insert(payload)


    def __insert(self, pair): 
        result = self.execute(
            """
                INSERT IGNORE INTO pairs 
                    (symbol, exchanger)
                VALUES 
                    (%s,%s);
            """,
            (pair.symbol, pair.exchanger, )
        )
        self.db.commit()

        if result.lastrowid > 0:
            self.pair_ids[pair.symbol] = result.lastrowid


    def get_pair_id_by_symbol(self, symbol):
        if symbol in self.pair_ids:
            return self.pair_ids[symbol]

        cursor = self.execute("SELECT pair_id FROM pairs WHERE symbol = %s;",
            (symbol,)
        )

        pair_id_result = cursor.fetchone()

        if pair_id_result is None:
            return None #TODO: raise custom exception
        else:
            pair_id = pair_id_result[0]
            self.pair_ids[symbol] = pair_id
            return pair_id
