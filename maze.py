class Cell:
    def __init__(self, x1, y1, x2, y2,win):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
    
    def draw(self):
        if self.has_left_wall == True:
            return
        if self.has_right_wall == True:
            return
        if self.has_top_wall == True:
            return
        if self.has_bottom_wall == True:
            return