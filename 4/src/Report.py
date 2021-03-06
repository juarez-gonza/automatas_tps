class Report():
    def __init__(self):
        self.hist = []
        self.status = None

    def summit(self, curr_st, curr_c, nxt_st):
        entry = {
            "curr_st": curr_st,
            "curr_c": curr_c,
            "nxt_st": nxt_st
        }
        self.hist.append(entry)

    def set_status(self, status):
        if not isinstance(status, bool):
            raise ValueError("Report.status %s no es de tipo bool" % status)
        self.status = status

    def gen_log(self):
        pass

class RPrinter(Report):
    def __init__(self):
        super().__init__()

    def row4values(self, values):
        vert_br = "|"
        row = []
        row.append(vert_br)
        for v in values:
            row.append(v)
            row.append(vert_br)
        return row

    def sep4sample(self, sample, maxlen):

        horiz_br = "-" * (maxlen + 2)
        horiz_bord = "+"

        i = 0
        horiz_sep = []
        horiz_sep.append(horiz_bord)
        for key in sample:
            horiz_sep.append(horiz_br)
            horiz_sep.append(horiz_bord)
            i += 1
        return horiz_sep

    def gen_log(self):
        out = []
        sample = self.hist[0]

        maxlen = float("-inf")
        for key in sample:
            maxlen = len(key) if len(key) > maxlen else maxlen

        horiz_sep = self.sep4sample(sample, maxlen)
        hdr = self.row4values(sample.keys())

        out.append(horiz_sep)
        out.append(hdr)
        out.append(horiz_sep)
        for e in self.hist:
            row = self.row4values(e.values())
            out.append(row)
            out.append(horiz_sep)

        i = 0
        for r in out:
            for v in r:
                # por qué i%2 genera output alineado? ni idea
                # pero ya me quedé sin ganas de pensar
                print(v.center(maxlen + i%2), end="")
            i += 1
            print("")

        if self.status:
            print("\n\t\tINPUT ACEPTADO :)\n")
        else:
            print("\n\t\tINPUT RECHAZADO :/\n")

# Exactamente igual a Report, pero su uso es diferente
# Report es más bien la clase a expander por aquellas que la hereden
# RTester es el stub usado por el tester para no generar output innecesario
class RTester(Report):
    def __init__(self):
        super().__init__()
