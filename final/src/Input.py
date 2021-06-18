import getopt
from fecha import *

class Input:
    # kwargs puede ser usado por input para el tester (setear el input)
    # o para el nombre de un archivo en el caso de toma de input por archivo
    def take_input(self, **kwargs):
        pass

class CLI_Input(Input):
    def take_input(self, **kwargs):
        argsp = {
            "user": None,
            # valores default para delimitar el rango
            "rango_init": None,
            "rango_fin": None,
        }
        while not argsp["user"]:
            argsp["user"] = input("Ingresar nombre del usuario a trackear: ").replace("\n", "")

        try:
            argsp["rango_init"] = dd_mm_yyyy_to_date(input("Ingresar fecha de inicio -en formato dd/mm/yyyy- de la busqueda (1/1/1000 por default): "))
        except ValueError:
            argsp["rango_init"] = dd_mm_yyyy_to_date("1/1/1000")

        try:
            argsp["rango_fin"] = dd_mm_yyyy_to_date(input("Ingresar fecha de fin -exclusiva y en formato dd/mm/yyyy- de la busqueda (31/12/2029 por default): "))
        except ValueError:
            argsp["rango_fin"] = dd_mm_yyyy_to_date("31/12/2029")

        return argsp

class Argv_Input(Input):
    def take_input(self, **kwargs):
        argv = kwargs["argv"]
        return self.parse_args(argv)

    def parse_args(self, argv):
        opt, args = getopt.getopt(argv, "u:i:f:", ["usuario=", "inicio=", "fin="])
        argsp = {
            "user": None,
            # valores default para delimitar el rango
            "rango_init": dd_mm_yyyy_to_date("1/1/1000"),
            "rango_fin": dd_mm_yyyy_to_date("31/12/2029"),
        }

        for tup in opt:
            o = tup[0].replace("-","")
            if o[0] == "u":
                argsp["user"] = tup[1]
            elif o[0] == "f":
                argsp["rango_fin"] = dd_mm_yyyy_to_date(tup[1])
            elif o[0] == "i":
                argsp["rango_init"] = dd_mm_yyyy_to_date(tup[1])
            else:
                raise ValueError("Opcion '%s' no reconocida" % o)

        if not argsp["user"]:
            raise ValueError("Falta parametro necesario\n\nUso:\n\t %s [--user -u] username" % __file__)

        return argsp
