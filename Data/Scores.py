from Data.AbstractDAO import AbstractDAO

class Scores(AbstractDAO):

    def __init__(self):
        super(Scores, self).__init__()


    def get_best_oscillators(self): 
        iterator = self.execute(
            """
                SELECT COUNT(*) AS score, p.symbol AS symbol
                FROM indicators as i
                INNER JOIN pairs AS p ON (i.pair_id = p.pair_id)
                WHERE p.symbol LIKE '%BTC'
                AND i.indicator_key = 'OSCILLATORS'
                AND i.indicator_value IN ('BUY', 'STRONG_BUY')
                AND i.batch_id = (select MAX(batch_id) FROM batches)
                GROUP BY i.pair_id
                ORDER BY score DESC
            """,
            named_tuple=True
        )
        
        return {symbol: score for (score, symbol) in iterator}
