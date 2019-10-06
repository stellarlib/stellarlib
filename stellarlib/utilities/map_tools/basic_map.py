

class BasicMap(object):

    def __init__(self, w, h, base_value=None):

        self.w = w
        self.h = h
        self._map = [base_value] * w * h

    def _get_index(self, coord):
        x, y = coord
        return y * self.w + x

    def get(self, coord):
        x, y = coord
        return self._map[self._get_index((x, y))]

    def set(self, coord, value):
        x, y = coord
        self._map[self._get_index((x, y))] = value

    @property
    def all_points(self):
        return ((x, y) for y in range(self.h) for x in range(self.w))

    def in_bounds(self, coord):
        x, y = coord
        return 0 <= x < self.w and 0 <= y < self.h
