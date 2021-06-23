from Input import File_Input, CLI_Input
from User_Input import CLI_User_Input

from Output import File_Output, CLI_Output
from Fmt_Report import Fmt_Report_CLI, Fmt_Report_CSV

from N_Cache import N_Cache_CSV

from Filter import Filter

from parse import parse

from User import User

INPUT_FILENAME = "acts-user1.txt"
OUTPUT_FILENAME = "output.csv"

# retorna una funcion que puede pasarse como argumento a User.for_each_addr
# logrando que para cada mac_addres del usuario se busque la ultima conexion
# y se añada al buffer de los reporters recibidos por argumentos en la funcion closure
def for_each_addr_reporter_closure(*reporters):
    def reporter_closure(user, addr):
        conn = user.find_last_addr_conn(addr)
        for r in reporters:
            r.report_conn(conn)
    return reporter_closure

def main():
    cli_in = CLI_User_Input(CLI_Input(), CLI_Output())
    f_in = File_Input(INPUT_FILENAME, True, 1)

    date_filter = Filter("[0-3]?[0-9]/[0-1]?[0-9]/[0-2]0[0-2][0-9]", "dd/mm/yyyy")
    mac_filter = Filter("([0-9a-fA-F]{2}(:|-)){5}[0-9a-f-A-F]{2}")
    user_filter = Filter("(\S)+")

    n_cache = N_Cache_CSV()

    while True:

        # file_reporter si o si debe iniciarse aca para reescribir el archivo.
        # De resetear la posicion despues del primer loop podria haber una
        # reescritura solamente parcial (dejando datos viejos).
        cli_reporter = Fmt_Report_CLI(CLI_Output())
        file_reporter = Fmt_Report_CSV(File_Output(OUTPUT_FILENAME))

        cli_reporter.report_namelist(n_cache.namelist(f_in))
        cli_reporter.flush()

        username, range_st, range_end = cli_in.main_input(user_filter, date_filter)

        # esto logra que se puedan tomar expresiones regex como input, pero en el algoritmo fallaria
        # en dividirse conexion segun usuario, o sea, se mostrarian todas las conexiones
        # de los usuarios que hagan match con la expresion pero sin distinguir a qué usuario en particular
        # pertenece cada conexion.
        username_filter = Filter(username)

        user = User(username)
        parse(f_in, user, username_filter, mac_filter, date_filter, range_st, range_end)

        reporter_closure = for_each_addr_reporter_closure(cli_reporter, file_reporter)
        user.for_each_addr(reporter_closure)

        cli_reporter.flush()
        if cli_in.export_prompt():
            file_reporter.flush()

        if not cli_in.continue_prompt():
            break

        f_in.abs_seek(0)

if __name__ == "__main__":
    main()
