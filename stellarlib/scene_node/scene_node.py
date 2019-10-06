from .node import Node
from .position import Position


class SceneNode(Node):

    def __init__(self, parent, pos=(0, 0)):

        Node.__init__(self, parent)
        self.position = Position(self, pos)
        self.components = []

    # Drawable interface
    def _get_draw_target(self):
        return self.parent._get_draw_target()

    def _get_draw_pos(self, pos=(0, 0)):
        # return the relative pos to this node's display added with the input pos
        return self.position.draw_position.peek_add(pos)

    def relative_pos(self, node):
        return self.position.relative_pos(node)

    def get_display(self):
        return self.parent.get_display()

    def update(self):

        self.position.update()
        [component.update() for component in self.components]
        [child.update() for child in self.children]

    def render_to(self, target):

        [component.draw(self) for component in self.components]
        [child.render_to(target) for child in self.children]

    def add_component(self, component):

        self.components.append(component)
