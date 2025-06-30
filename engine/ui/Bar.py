from engine.ui import Component


class Bar(Component):
    def init(self, parent=None, **kwargs):
        super().init(parent, **kwargs)
        self.__value = kwargs.get('value', 0)
        self.__max_value = kwargs.get('max_value', 100)
        self.__color = kwargs.get('color', (0, 255, 0))  # Default to green
        self.__width = kwargs.get('width', 100)
        self.__height = kwargs.get('height', 12)
    
    def update(self):
        pass
        
    def set_value(self, value):
        """Set the value of the bar and update its appearance."""
        self.__value = value
        if self.__value < 0:
            self.__value = 0
        elif self.__value > self.__max_value:
            self.__value = self.__max_value
    
    def get_value(self):
        """Get the current value of the bar."""
        return self.__value
    
    def set_max_value(self, max_value):
        """Set the maximum value of the bar."""
        self.__max_value = max_value
        if self.__value > self.__max_value:
            self.__value = self.__max_value
    
    def get_max_value(self):
        """Get the maximum value of the bar."""
        return self.__max_value
    
    def draw(self, surface):
        """Draw the bar on the given surface."""
        self.filled_width = (self.__value / self.__max_value) * self.__width
        #TODO: update the textures for the bar
        # Placeholder for drawing logic
        #TODO: Implement actual drawing logic