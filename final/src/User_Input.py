# La idea es tener una interfaz contra la cual se pueda obtener input del usuario
# podría haber una interfaz para CLI, input por archivo, por argumentos en linea de comandos, etc

class User_Input:
    def main_input(self):
        pass

    def export_prompt(self):
        pass

    def continue_prompt(self):
        pass

class CLI_User_Input():
    def __init__(self, c_in, c_out):
        self.c_in = c_in
        self.c_out = c_out

    def main_input(self, user_filter, date_filter, range_st_default="1/1/2000", range_end_default="31/12/2029"):
        username = ""
        while not user_filter.match(username):
            self.c_out.write_output("Nombre de usuario a buscar: ")
            username = self.c_in.input_line().strip()

        self.c_out.write_output("Fecha de inicio de rango de busqueda en formato %s [default]: " % date_filter.get_fmt())
        range_st = self.c_in.input_line().strip()
        if not date_filter.match(range_st):
            self.c_out.write_output("Formato de '%s' no reconocido, Se procederá con el valor default para el campo\n" % range_st)
            range_st = range_st_default

        self.c_out.write_output("Fecha de fin de rango de busqueda en formato %s [default]: " % date_filter.get_fmt())
        range_end = self.c_in.input_line().strip()
        if not date_filter.match(range_end):
            self.c_out.write_output("Formato de '%s' no reconocido, Se procederá con el valor default para el campo\n" % range_end)
            range_end = range_end_default

        return username, range_st, range_end

    def continue_prompt(self):
        self.c_out.write_output("Desea volver a correr el programa? [Y/n]: ")
        if "y" in self.c_in.input_line().strip().lower():
            return True
        return False

    def export_prompt(self):
        self.c_out.write_output("Desea exportar los resultados a un archivo .cvs? [Y/n]: ")
        if "y" in self.c_in.input_line().strip().lower():
            return True
        return False
