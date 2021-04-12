from Indicators.AbstractIndicator import AbstractIndicator

class RecommendationMovingAverages(AbstractIndicator):
            
    def calculate(self):
        return self.data_provider.get_analysis().moving_averages['RECOMMENDATION']
