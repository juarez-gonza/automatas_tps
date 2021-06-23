import dates

class Fmt_Report:
    def report_conn(self, conn):
        pass

    def report_namelist(self):
        pass

    def flush(self):
        pass

    def clean(self):
        pass

class Fmt_Report_CLI(Fmt_Report):
    def __init__(self, out):
        self.out = out
        self.out_msg = ""

    def report_conn(self, conn):
        if self.out_msg == "":
            self.out_msg += "\n" + "MAC".center(20) + "\t|\t" + "INI_CONN".center(20) + "\t|\t" + "FIN_CONN".center(20) + "\n"
        self.out_msg += ("%s" % conn.get_addr()).center(20)
        self.out_msg += "\t|\t"
        self.out_msg += ("%s" % conn.get_st()).center(20)
        self.out_msg += "\t|\t"
        self.out_msg += ("%s" % conn.get_end()).center(20)
        self.out_msg += "\n"

    def report_namelist(self, namelist):
        self.clean()
        self.out_msg = "Lista de usernames:\n"
        for i in range(len(namelist)):
            self.out_msg  += ("%s" % namelist[i]).center(20)
            if (i+1) % 4 == 0:
                self.out_msg += "\n"

    def flush(self):
        self.out.write_output(self.out_msg + "\n")
        self.clean()

    def clean(self):
        self.out_msg = ""

class Fmt_Report_CSV(Fmt_Report):
    def __init__(self, out):
        self.out = out
        self.out_msg = ""

    def report_conn(self, conn):
        if self.out_msg == "":
            self.out_msg = "MAC,INI_CONN,FIN_CONN\n"
        self.out_msg += "%s,%s,%s\n" % (
            conn.get_addr(),
            conn.get_st(),
            conn.get_end()
            )

    def report_namelist(self, namelist):
        pass

    def flush(self):
        self.out.write_output(self.out_msg + "\n")
        self.clean()

    def clean(self):
        self.out_msg = ""
