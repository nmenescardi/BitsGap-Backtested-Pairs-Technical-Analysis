from Data.Scores import Scores
from Models.TradingViewList import TradingViewList
from Models.FileWriter import FileWriter

scores_dao = Scores()
result = scores_dao.get_best_oscillators()

writer = FileWriter(
    file_dir = './tradingView_list.txt'
)
tv_list = TradingViewList(result, writer)
tv_list.create()
print(result)
