from typing import Dict, List

from utilities.AgedFish import AgedFish
from utilities.Fish import Fish
from utilities.FishesService import LearningData


class Model:
    def predict(self, fish: Fish) -> int:
        """Predict age of fish"""
        # TODO
        return 0
    
    def train(self, learningSet: LearningData) -> float:
        """train model, return error"""
        return 100.0
    
    def evaluateError(self, testSet: List[AgedFish]):
        predictions = { {fish:self.predict(fish)} for fish in testSet }
        return Model.mse(predictions) 
    
    @staticmethod
    def mse(predictions: Dict[Fish, int]):
        # sum([(predicted_value - real_value)**2 for i in range(N)])/N N étant le nombre de valeur
        size = len(predictions)
        return sum([(prediction - actual.age)**2 for actual, prediction in predictions.items()])/ size