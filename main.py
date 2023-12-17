from models.model import Model
from utilities.AgedFish import AgedFish
from utilities.Fish import Fish
from utilities.FishesService import exportPredicitonsAsFile, getLearningData, readTestFishesFromCsv, LearningData
from typing import List

TESTPATH = 'ressources/test.csv'
TRAINPATH = 'ressources/train.csv'
OUTPUTPATH = 'output/submission.csv'

trainFishes: LearningData = getLearningData(TRAINPATH)
testFishes: List[Fish] = readTestFishesFromCsv(TESTPATH)

def predict(model: Model) -> List[AgedFish]:
    return [ AgedFish.fromFish(fish, model.predict(fish)) for fish in testFishes]

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
exportPredicitonsAsFile(predictions, OUTPUTPATH)