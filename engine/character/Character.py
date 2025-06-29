from enum import Enum

from engine.GameObject import GridGameObject

class CharacterState(Enum):
    IDLE = 0
    MEELEE_ATTACKING = 1
    RANGE_ATTACKING = 2
    CASTING = 3
    EATING = 4
    DRINKING = 5
    STRUCK = 6
    DEAD = 7

class Character(GridGameObject):
    state:int

    name:str
    hp:int
    maxHp:int
    mp:int
    maxMp: int

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.state = CharacterState.IDLE
    
    