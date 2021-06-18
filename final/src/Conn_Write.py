class Conn_Write:
    def __init__(self):
        pass

    def write():
        pass

class Conn_Write_CSV(Conn_Write):
    def __init__(self):
        super().__init__()

    def write_header(self):
        return "Address,Conn_Inicio,Conn_Fin\n"

    def write(self, conn):
        return "%s,%s,%s\n" % (conn.address, str(conn.inicio), str(conn.fin))

class Conn_Write_CLI(Conn_Write):
    def __init__(self):
        super().__init__()

    def write_header(self):
        return "Address".center(20) + "Conn_Inicio".center(20) + "Conn_Fin".center(20) + "\n"

    def write(self, conn):
        return str(conn.address).center(20) + str(conn.inicio).center(20) + str(conn.fin).center(20) + "\n"
