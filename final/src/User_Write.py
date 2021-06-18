class User_Write:
    def __init__(self, user, conn_writer):
        self.user = user
        self.conn_writer = conn_writer

    def write():
        pass

class User_Write_CSV(User_Write):
    def __init__(self, user, conn_writer):
       super().__init__(user, conn_writer)

    def write(self):
        res = self.conn_writer.write_header()
        for conn in self.user.conns:
            res += self.conn_writer.write(conn)
        return res

class User_Write_CLI(User_Write):
    def __init__(self, user, conn_writer):
       super().__init__(user, conn_writer)

    def write(self):
        res = self.conn_writer.write_header()
        for conn in self.user.conns:
            res += self.conn_writer.write(conn)
        return res
