class User:
    def __init__(self, username):
        self.username = username
        self.conns = []
        self.addresses = []

    def get_username(self):
        return self.username

    def push_conn(self, conn):
        if conn.address not in self.addresses:
            self.addresses.append(conn.address)
        self.conns.append(conn)

    def has_multiple_conn(self):
        return self.addr_quant() > 1

    def addr_last_conn(self, addr):
        for i in range(len(self.conns)-1, -1, -1):
            if self.conns[i].get_addr() == addr:
                return self.conns[i]

    def for_each_addr(self, addr_fc):
        for addr in self.addresses:
            addr_fc(self, addr)

class addr_f_obj:
    def __init__(self, *reporters):
        self.reporters = reporters

    def __call__(self, user, addr):
        conn = user.addr_last_conn(addr)
        for r in self.reporters:
            r.summit_conn(conn)
