

class Node(object):

    def __init__(self, parent):

        self.parent = None
        self.children = []

        if parent:
            self.assign_parent(parent)

    def assign_parent(self, new_parent):

        if self.parent:
            self.orphan()
        self.parent = new_parent
        if new_parent:
            new_parent.add_child(self)

    def add_child(self, child):

        self.children.append(child)

    def remove_child(self, child):

        self.children.remove(child)

    def orphan(self):

        if self.parent:
            self.parent.remove_child(self)
            self.parent = None

    def abandon_children(self):

        [child.orphan() for child in self.children]

    def is_descendant(self, node):

        """ Returns true if the given node is a parent or ancestor of
        this node """

        if node is self.parent:
            return True
        if self.parent is None:
            return False
        else:
            return self.parent.is_descendant(node)

    def insert(self, target_node):

        self.assign_parent(target_node.parent)
        target_node.assign_parent(self)

    def prune(self):

        [child.assign_parent(self.parent) for child in  self.children]
        self.orphan()
