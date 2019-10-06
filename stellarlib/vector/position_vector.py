from .vector2 import Vector2


class PositionVector(Vector2):

    def peek_add(self, other, integer=False):
        x = self.x + other[0]
        y = self.y + other[1]
        if integer:
            return int(round(x)), int(round(y))
        return x, y

    def peek_subtract(self, other, integer=False):
        x = self.x - other[0]
        y = self.y - other[1]
        if integer:
            return int(round(x)), int(round(y))
        return x, y
