class Conn:
    def __init__(self, owner, address, st, end):
        self.owner = owner      # User obj
        self.address = address  # string
        self.st = st            # string
        self.end = end          # string

    def get_owner(self):
        return self.owner

    def get_addr(self):
        return self.address

    def get_st(self):
        return self.st

    def get_end(self):
        return self.end
