from math import hypot, degrees, radians, atan, cos, sin


class Vector2(object):

    @classmethod
    def from_angle(cls, angle_deg, scalar=None):

        if angle_deg > 360.0:
            angle_deg -= 360.0
        if angle_deg < 0.0:
            angle_deg += 360.0

        th = radians(angle_deg)
        angle_vec = cls(cos(th), sin(th))
        if scalar:
            angle_vec.mult(scalar)

        return angle_vec

    def __init__(self, *args):

        if len(args) > 2:
            raise ValueError('Vector2 object can only have 2 elements')

        if not args:
            x = 0.0
            y = 0.0
        elif len(args) == 1:
            x = float(args[0][0])
            y = float(args[0][1])
        else:
            x = args[0]
            y = args[1]

        self.x = x
        self.y = y

    # Getters and setters
    def set(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def get(self):
        return self.x, self.y

    def match(self, vector):
        self.x = vector.x
        self.y = vector.y

    def __getitem__(self, key):

        if key < 0 or key > 1:
            raise IndexError
        if key == 0:
            return self.x
        elif key == 1:
            return self.y

    def __len__(self):
        return 2

    def __iter__(self):
        return (self[v] for v in range(2))

    # Operations
    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

    def sub(self, vec):
        self.x -= vec.x
        self.y -= vec.y

    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def div(self, scalar):
        self.x /= scalar
        self.y /= scalar

    def dot(self, vec):
        return self.x * vec.x + self.y * vec.y

    # Normals
    def get_normalized(self):
        normalized = Vector2(self)
        normalized.div(self.magnitude())
        return normalized

    def normalize(self):
        self.div(self.magnitude())

    def magnitude(self):
        return hypot(self.x, self.y)

    # Output
    @property
    def coord(self):
        return int(round(self.x)), int(round(self.y))

    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)

    # Angles
    def set_angle(self, angle_deg):
        th = radians(angle_deg)
        length = self.magnitude()
        self.set(cos(th), sin(th))
        self.mult(length)

    def get_angle(self):

        if self.x == 0:
            if self.y >= 0:
                return 90
            else:
                return 270

        angle = degrees(atan((self.y / self.x)))
        if self.x < 0:
            angle += 180
        return angle
