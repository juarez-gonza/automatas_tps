import dates

class Conn:
    def __init__(self, address, st, end):
        self.address = address # string
        self.st = st # objeto date
        self.end = end # objeto date

    def get_addr(self):
        return self.address

    def get_st_str(self):
        return dates.date_to_dd_mm_yyyy(self.st)

    def get_end_str(self):
        return dates.date_to_dd_mm_yyyy(self.end)
