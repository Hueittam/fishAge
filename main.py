from utilities.Fish import Fish
from utilities.FishesService import getLearningData, readTestFishesFromCsv, LearningData
from typing import List

TESTPATH = 'ressources/test.csv'
TRAINPATH = 'ressources/train.csv'

testFishes: LearningData = getLearningData(TRAINPATH)
trainFishes: List[Fish] = readTestFishesFromCsv(TESTPATH)
[print(fish) for fish in trainFishes]