from Indicators.AbstractIndicator import AbstractIndicator

class RecommendationMovingAverages(AbstractIndicator):
            
    def key(self):
        return 'MOVING_AVERAGES'


    def calculate(self):
        return self.data_provider.get_analysis().moving_averages['RECOMMENDATION']
