import pygame

from engine.ui.Component import Component

class Container(Component):
    __children:list[Component]

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.__children = []

    def set_x(self, value):
        delta = value - self.__x
        super().set_x(value)
        for child in self.__children:
            child.set_x(child.get_x() + delta)
        
    def set_y(self, value):
        delta = value - self.__y
        super().set_y(value)
        for child in self.__children:
            child.set_y(child.get_y() + delta)

    def getChildren(self): return self.__children

    def addChild(self, component:Component):
        component.set_x(component.get_x() + self.__x)
        component.set_y(component.get_y() + self.__y)
        self.__children.append(component)
    
    def removeChild(self, component:Component):
        if(component == None): return
        self.__children.remove(component)
        
    def getChild(self, index:int):
        if(index < -len(self.__children)): return None
        if(index > len(self.__children)): return None
        return self.__children[index]

    def alterChild(self, index:int, component:Component):
        if(index < -len(self.__children)): return
        if(index > len(self.__children)): return
        if(component == None):return
        self.__children[index] = component

    def update(self):
        super().update()
        for child in self.__children:
            child.update()

    def draw(self, screen):
        super().draw(screen)
        for child in self.__children:
            child.draw(screen)
