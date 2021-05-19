class Input:
    def take_input(self):
        pass

class CLI_Input(Input):
    def take_input(self):
        msg = "Ingresar cadena a evaluar:"
        horiz_sep = "+" + "-" * (len(msg) + 2) + "+"
        vert_br = "|"
        cuadro = horiz_sep + "\n" + vert_br + msg.center(len(horiz_sep)-2) + vert_br +\
            "\n" + horiz_sep
        print(cuadro)
        inp = input("\t----> ")
        return inp
