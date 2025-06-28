def selectTaget(caster:Character, minRange:int = 0, maxRange:int=1, includeEnemies:bool = True, includeAlies:bool = True)-> Character:
    pass

def selectCircularArea(caster:Character, minRange:int = 0, maxRange:int=1, radius:int = 1)-> List[Position]:
    pass

def selectConicArea(caster:Character, maximunRange:int = 1, angle:int = 30)->List[Position]:
    pass

def selectLinearArea(caster:Character, minimumrange:int = 0, maximumRange:int = 1)-> list[Position]:
    pass

def getAffectedCharactersInArea(area:List[Postion])->list[Character]:
    pass