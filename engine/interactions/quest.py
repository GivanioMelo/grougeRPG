import json


class QuestStage:
    code:int
    description:str
    completed:bool

class QuestReward:
    description:str
    xp:int
    gold:int
    grantedItems: list[int]
    itemsForChose: list[int]
    nItensForChose: int

    def __init__(self): pass

class Quest:
    name:str
    description:str
    stages: list[QuestStage]
    reward: QuestReward

    def __init__(self, name = ""):
        self.name = name
        self.stages = []
        self.reward = None
    
    @classmethod
    def fromFile(cls,fileName):
        quest = cls()
        data = json.load(open(fileName))

        quest.name = data["name"]
        quest.description = data["description"]
        #TODO adicionar os dados dos estagios da quest e da recompensa