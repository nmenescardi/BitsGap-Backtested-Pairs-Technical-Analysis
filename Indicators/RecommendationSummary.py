from Indicators.AbstractIndicator import AbstractIndicator

class RecommendationSummary(AbstractIndicator):
                      
    def key(self):
        return 'SUMMARY'

              
    def calculate(self):
        return self.data_provider.get_analysis().summary['RECOMMENDATION']
