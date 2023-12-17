from Fish import Fish
from Reader import readFishesFromCsv
from typing import List

TESTPATH = 'ressources/test.csv'

fishes: List[Fish] = readFishesFromCsv(TESTPATH)
[print(fish) for fish in fishes]