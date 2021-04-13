from Data.Scores import Scores

scores_dao = Scores()
result = scores_dao.get_best_oscillators()
print(result)