from Input import CLI_Input
from Output import CLI_Output

def cli_take_input(user_filter, date_filter, range_st_default="1/1/2000", range_end_default="31/12/2029"):
    out = CLI_Output()

    username = ""
    while not user_filter.match(username):
        username = CLI_Input("Nombre de usuario a buscar").input_line()

    range_st = CLI_Input("Inicio de rango de busqueda en formato %s [default]" % date_filter.get_fmt()).input_line()
    if not date_filter.match(range_st):
        out.write_output("Formato de '%s' no reconocido, Se procederá con el valor default para el campo" % range_st)
        range_st = range_st_default

    range_end = CLI_Input("Fin de rango de busqueda en formato %s [default]" % date_filter.get_fmt()).input_line()
    if not date_filter.match(range_end):
        out.write_output("Formato de '%s' no reconocido, Se procederá con el valor default para el campo" % range_end)
        range_end = range_end_default

    return username, range_st, range_end

def cli_continue_prompt():
    out = CLI_Output()
    if "y" in CLI_Input("Desea volver a correr el programa? [Y/n]").input_line().lower():
        return True
    return False

def cli_export_prompt():
    out = CLI_Output()
    if "y" in CLI_Input("Desea exportar los resultados a un archivo .cvs? [Y/n]").input_line().lower():
        return True
    return False
