from enum import Enum

class CharacterState(Enum):
    IDLE = 0
    MEELEE_ATTACKING = 1
    RANGE_ATTACKING = 2
    CASTING = 3
    EATING = 4
    DRINKING = 5
    STRUCK = 6
    DEAD = 7

class Character:
    state:int

    def __init__(self):
        self.state = CharacterState.IDLE
    
    