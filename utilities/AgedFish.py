from utilities.Fish import Fish


class AgedFish(Fish):
    age: int

    def __init__(
        self,
        id: int,
        weight: int,
        length: int,
        liverweight: float,
        gonadweight: float,
        age: int):
        super().__init__(id, weight, length, liverweight, gonadweight)
        self.age = age