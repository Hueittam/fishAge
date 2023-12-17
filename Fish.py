

class Fish:
    id: int
    weight: int
    length: int
    liverweight: float
    gonadweight: float

    def __init__(
        self,
        id: int,
        weight: int,
        length: int,
        liverweight: float,
        gonadweight: float):
        self.id = id
        self.weight = weight
        self.length = length
        self.liverweight = liverweight
        self.gonadweight = gonadweight
        
    def __str__(self):
        return "; ".join([str(self.id), str(self.weight), str(self.length), str(self.liverweight), str(self.gonadweight)])