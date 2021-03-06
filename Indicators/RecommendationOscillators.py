from Indicators.AbstractIndicator import AbstractIndicator

class RecommendationOscillators(AbstractIndicator):
                  
    def key(self):
        return 'OSCILLATORS'

      
    def calculate(self):
        return self.data_provider.get_analysis().oscillators['RECOMMENDATION']
