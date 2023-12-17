from typing import List
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