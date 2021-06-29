# la idea es tener que se encargue del formato
# la cual tenga la posibilidad de poner datos en un buffer
# que luego puede descargarse en una instancia de Output con un flush()

class Conn_Reporter:
    def summit_conn(self, conn):
        pass

    def flush(self):
        pass

    def clean(self):
        pass

class CLI_Conn_Reporter(Conn_Reporter):
    def __init__(self, c_out):
        self.c_out = c_out
        self.conn_buff = ""

    def summit_conn(self, conn):
        if self.conn_buff == "":
            self.conn_buff += "\n" + "MAC".center(20) + "\t|\t"         \
                            + "INI_CONN".center(20) + "\t|\t"           \
                            + "FIN_CONN".center(20) + "\n"
        self.conn_buff += ("%s" % conn.get_addr()).center(20) + "\t|\t" \
                       + ("%s" % conn.get_st()).center(20) + "\t|\t"    \
                       + ("%s" % conn.get_end()).center(20) + "\n"

    def flush(self):
        self.c_out.write(self.conn_buff)
        self.clean()

    def clean(self):
        self.conn_buff = ""

class CSV_Conn_Reporter(Conn_Reporter):
    def __init__(self, c_out):
        self.c_out = c_out
        self.conn_buff = ""

    def summit_conn(self, conn):
        if self.conn_buff == "":
            self.conn_buff += "USERNAME,MAC,INI_CONN,FIN_CONN\n"
        self.conn_buff += "%s,%s,%s,%s\n" % (conn.get_owner().get_username(),
                                            conn.get_addr(),
                                            conn.get_st(),
                                            conn.get_end())

    def flush(self):
        self.c_out.write(self.conn_buff)
        self.clean()

    def clean(self):
        self.conn_buff = ""
