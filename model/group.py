class Group:
    def __init__(self, name=None, header=None, footer=None, identifier=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.identifier = identifier

    def __repr__(self):
        return "%s:%s" % (self.identifier, self.name)

    def __eq__(self, other):
        return self.name == other.name and self.identifier == other.identifier
