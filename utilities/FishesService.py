from typing import Dict, List
import pandas as pd;
import random
from utilities.Fish import Fish

class LearningData:
    trainingSet: List[Fish] = []
    testSet: List[Fish] = []
    
    def __init__(self, learningSet: List[Fish]) -> None:
        random.shuffle(learningSet)
        half_length = len(learningSet) // 2
        self.trainingSet, self.testSet = learningSet[:half_length], learningSet[half_length:]
        

def readTestFishesFromCsv(path: str) -> Dict[int, Fish]:
    return _readFromCsv(path, _FishFromRow)


def _readTrainingFishesFromCsv(path: str) -> Dict[int, Fish]:
    return _readFromCsv(path, _FishFromRow)

def _readFromCsv(path: str, reader):
    rawFishes: pd.DataFrame = pd.read_csv(path, index_col=0)
    fishesById: Dict[int, Fish] = {id: reader(value) for (id, value) in rawFishes.to_dict('index').items()}
    return fishesById

def _FishFromRow(row):
    columns = ['weight', 'length', 'liverweight', 'gonadweight', 'age']
    return Fish(*[row.get(key) for key in columns])


def getLearningData(path: str) -> LearningData:
    return LearningData(list(_readTrainingFishesFromCsv(path).values()))