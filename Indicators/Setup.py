from Indicators.RecommendationSummary import RecommendationSummary
from Indicators.RecommendationOscillators import RecommendationOscillators
from Indicators.RecommendationMovingAverages import RecommendationMovingAverages

class Setup():
		
	config = {
		'SUMMARY' : RecommendationSummary,
		'OSCILLATORS' : RecommendationOscillators,
		'MOVING_AVERAGES' : RecommendationMovingAverages,
	}
	
