from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, identifier=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.identifier = identifier

    def __repr__(self):
        return "%s:%s" % (self.identifier, self.name)

    def __eq__(self, other):
        return (self.identifier is None or other.identifier is None or self.identifier == other.identifier) \
               and self.name == other.name

    def id_or_max(self):
        if self.identifier:
            return int(self.identifier)
        else:
            return maxsize
