from Indicators.AbstractIndicator import AbstractIndicator

class RecommendationSummary(AbstractIndicator):
            
    def calculate(self):
        return self.data_provider.get_analysis().summary['RECOMMENDATION']
