from Filter import Filter
from Input import File_Input
from Output import File_Output

from User import User

from dates import dd_mm_yyyy_to_date

from parse import parse, namelist

import cli

INPUT_FILENAME = "acts-user1.txt"
OUTPUT_FILENAME = "output.cvs"

def cvs_report_user(user, f_out):
    if not user.has_multiple_conn():
        out.write("%s no tiene multiples conexiones" % user.get_username())
    else:
        out = "USERNAME,MAC,INI_CONN,FIN_CONN\n"
        for addr in user.get_addresses():
            conn = user.find_last_addr_conn(addr)
            out += "%s,%s,%s,%s\n" % (user.get_username(), conn.get_addr(), conn.get_st_str(), conn.get_end_str())
        f_out.write_output(out)

def file_parse(f_in, range_st_obj, range_end_obj, user_filter, date_filter, mac_filter):
    user = User(user_filter.get_fmt())

    parse(f_in, user, range_st_obj, range_end_obj, user_filter, date_filter, mac_filter)

    return user

def main():
    date_filter = Filter("[0-3]?[0-9]/[0-1]?[0-9]/[0-2]0[0-2][0-9]", "dd/mm/yyyy")
    mac_filter = Filter("([0-9a-fA-F]{2}(:|-)){5}[0-9a-f-A-F]{2}")
    user_filter = Filter("(\S)+")

    while True:
        f_in = File_Input(INPUT_FILENAME, True, 1)

        cli.cli_report_namelist(namelist(f_in))

        f_in.abs_seek(0)
        f_in.input_line()

        username, range_st, range_end = cli.cli_take_input(user_filter, date_filter)
        range_st_obj = dd_mm_yyyy_to_date(range_st)
        range_end_obj = dd_mm_yyyy_to_date(range_end)

        # redefinir user_filter para usar como filtro en el archivo, setear el formato tambien
        user_filter = Filter(username, username)

        user = file_parse(f_in, range_st_obj, range_end_obj, user_filter, date_filter, mac_filter)
        cli.cli_report_user(user)

        if cli.cli_export_prompt():
            f_out = File_Output(OUTPUT_FILENAME)
            cvs_report_user(user, f_out)
            del f_out

        if not cli.cli_continue_prompt():
            break

        del f_in

if __name__ == "__main__":
    main()
