class Input:
    # kwargs puede ser usado por input para el tester (setear el input)
    # o para el nombre de un archivo en el caso de toma de input por archivo
    def take_input(self, **kwargs):
        pass

class CLI_Input(Input):
    def take_input(self, **kwargs):
        msg = "Ingresar cadena a evaluar:"
        horiz_sep = "+" + "-" * (len(msg) + 2) + "+"
        vert_br = "|"
        cuadro = horiz_sep + "\n" + vert_br + msg.center(len(horiz_sep)-2) + vert_br +\
            "\n" + horiz_sep
        print(cuadro)
        inp = input("\t----> ")
        return inp

class Input_Tester(Input):
    def take_input(self, **kwargs):
        inp = kwargs["inp"]
        return inp
