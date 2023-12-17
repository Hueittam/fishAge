from typing import List
import pandas as pd;
import random
from utilities.AgedFish import AgedFish
from utilities.Fish import Fish

class LearningData:
    trainingSet: List[AgedFish] = []
    testSet: List[AgedFish] = []
    
    def __init__(self, learningSet: List[AgedFish]) -> None:
        random.shuffle(learningSet)
        half_length = len(learningSet) // 2
        self.trainingSet, self.testSet = learningSet[:half_length], learningSet[half_length:]
        

def readTestFishesFromCsv(path: str) -> List[Fish]:
    rawFishes: pd.DataFrame = pd.read_csv(path)
    return list(Fish(*row) for row in rawFishes.values)

def _readTrainingFishesFromCsv(path: str):
    rawFishes: pd.DataFrame = pd.read_csv(path)
    return list(AgedFish(*row) for row in rawFishes.values)

def getLearningData(path: str) -> LearningData:
    return LearningData(_readTrainingFishesFromCsv(path))

def exportPredicitonsAsFile(predictions: List[AgedFish], path: str):
    # TODO avec panda
    pass