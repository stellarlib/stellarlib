from math import sqrt


class Vector3(object):

    def __init__(self, *args):

        if len(args) > 3:
            raise ValueError('Vector4 object can only have 4 elements')

        if not args:
            x = 0.0
            y = 0.0
            z = 0.0
        elif len(args) == 1:
            x = float(args[0][0])
            y = float(args[0][1])
            z = float(args[0][2])
        else:
            x, y, z = args

        self.x = x
        self.y = y
        self.z = z

    def set(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def match(self, vector):
        self.x = vector.x
        self.y = vector.y
        self.z = vector.z

    @property
    def coord(self):
        return int(float(self.x)), int(float(self.y))

    def __getitem__(self, key):

        if key < 0 or key > 2:
            raise IndexError
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z

    def __len__(self):
        return 3

    def __iter__(self):
        return (self[v] for v in range(len(self)))

    # Operations
    def add(self, vec):
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z

    def sub(self, vec):
        self.x -= vec.x
        self.y -= vec.y
        self.z -= vec.z

    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    def div(self, scalar):
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar

    def dot(self, vec):
        return self.x * vec.x + self.y * vec.y + self.z * vec.z

    def cross(self, vec):
        x = self.y*vec.z - self.z*vec.y
        y = self.z*vec.x - self.x*vec.z
        z = self.x*vec.y - self.y*vec.x
        return Vector3(x, y, z)

    def __str__(self):
        return '(%f, %f, %f)' % (self.x, self.y, self.z)

    # Normals
    def get_normalized(self):
        normalized = Vector3(self)
        normalized.div(self.magnitude())
        return normalized

    def normalize(self):
        if self.magnitude():
            self.div(self.magnitude())
        return self

    def magnitude(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):

        return Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
        return Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )
