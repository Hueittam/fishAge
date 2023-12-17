from Fish import Fish;
import pandas as pd;

def readFishesFromCsv(path: str):
    rawFishes: pd.DataFrame = pd.read_csv(path)
    # fishes = [Fish(a., a.two) for a in df.itertuples()]
    
    # return [FishFromTupple(row) for row in rawFishes.itertuples()]
    return list(Fish(*row) for row in rawFishes.values)
    # return rawFishes.apply(lambda row: Fish(**row), axis=1)
    # return rawFishes.itertuples()
    
    
def FishFromTupple(row) -> Fish:
    return Fish(row.id, row.weight, row.length, row.liverweight, row.gonadweight)