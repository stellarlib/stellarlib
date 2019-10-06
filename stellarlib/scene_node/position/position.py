from stellarlib.vector import PositionVector


class Position(object):

    def __init__(self, node, pos):
        self.node = node
        self._pos = PositionVector(pos)
        self.position = PositionVector(pos)

        self.draw_position = PositionVector()

    def update(self):
        self.update_draw_pos()

    def display(self):
        return self.node.get_display()

    def update_draw_pos(self):
        self.draw_position.set(*self.relative_pos(self.display()))

    def local_pos(self):
        return self.position.coord

    def screen_pos(self, final=True):

        if self.node.parent:
            return self.position.peek_add(
                self.node.parent.position.screen_pos(final=False), integer=final)
        else:
            return self.local_pos()

    def relative_pos(self, node):

        if node is self.node:
            return 0, 0
        elif node is self.node.parent:
            return self.local_pos()

        if not self.node.is_descendant(node):
            raise ValueError(str(self) + ' has no relative position to ' + str(node))

        return self._relative_pos(node)

    def _relative_pos(self, node, final=True):

        if node is self.node.parent:
            return self.local_pos()
        else:
            return self.position.peek_add(
                self.node.parent.position._relative_pos(node, final=False), integer=final)
