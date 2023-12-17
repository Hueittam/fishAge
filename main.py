import pandas as pd
from models.model import Model
from utilities.Fish import Fish
from utilities.FishesService import getLearningData, readTestFishesFromCsv, LearningData
from typing import Dict, List

TESTPATH = 'ressources/test.csv'
TRAINPATH = 'ressources/train.csv'
OUTPUTPATH = 'output/submission.csv'

trainFishes: LearningData = getLearningData(TRAINPATH)
testFishes: Dict[int, Fish] = readTestFishesFromCsv(TESTPATH)

# fonctions diverses
def exportPredictionsAsFile(predictions: Dict[int, int]):
    pd.DataFrame([(id, age) for (id, age) in predictions.items()]).to_csv(OUTPUTPATH, index=False)
    
def predict(model: Model) -> Dict[int, int]:
    return { id:model.predict(fish) for (id, fish) in testFishes.items() }

# model Knn?
knnModel: Model = Model()
# model decision Tree?
treeModel: Model = Model()
# model regression?
regressionModel: Model = Model()
# perfs = [Perfs(knnModel, knnModel.train()), ... ]

# model associé à leur erreur (erreur reste à definir)
models = [knnModel, treeModel, regressionModel]
perfs = {model:model.train(trainFishes) for model in models}

# ???
# afficher les perfs, dicuter de leur pertinence 
# TODO choisir le model
# par exemple, on prend l'erreur minimale
meilleurModel: Model = min(perfs, key=perfs.get)
predictions = predict(meilleurModel)
exportPredictionsAsFile(predictions)