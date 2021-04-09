from Data.AbstractDAO import AbstractDAO

class Pairs(AbstractDAO):

    def __init__(self):
        super(Pairs, self).__init__()


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
        
        print('query result: ')
        print(vars(result))


    def get_pair_id_by_symbol(self, symbol):

        cursor = self.execute("SELECT pair_id FROM pairs WHERE symbol = %s;",
            (symbol,)
        )

        pair_id_result = cursor.fetchone()

        if pair_id_result is None:
            return None

        return pair_id_result[0]
