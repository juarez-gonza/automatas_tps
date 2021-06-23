class Conn:
    def __init__(self, address, st, end):
        self.address = address # string
        self.st = st # objeto date
        self.end = end # objeto date

    def get_addr(self):
        return self.address

    def get_st(self):
        return self.st

    def get_end(self):
        return self.end
