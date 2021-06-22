class User:
    def __init__(self, username):
        self.username = username
        self.conns = []
        self.addresses = []

    def get_username(self):
        return self.username

    def get_addresses(self):
        return [*self.addresses]

    def push_conn(self, conn):
        if conn.address not in self.addresses:
            self.addresses.append(conn.address)
        self.conns.append(conn)

    def addr_quant(self):
        return len(self.addresses)

    def has_multiple_conn(self):
        return self.addr_quant() > 1


    def find_last_addr_conn(self, addr):
        for i in range(len(self.conns)-1, -1, -1):
            if self.conns[i].get_addr() == addr:
                return self.conns[i]
