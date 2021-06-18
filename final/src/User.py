class User:
    def __init__(self, username):
        self.username = username
        self.conns = []
        self.addresses = []

    def push_conn(self, conn):
        if conn.address not in self.addresses:
            self.addresses.append(conn.address)
        self.conns.append(conn)

    def addr_quant(self):
        return len(self.addresses)
