from Filter import Filter
from Input import File_Input
from Output import File_Output, CLI_Output

from parse import parse, namelist

import cli

from Fmt_Report import Fmt_Report_CLI, Fmt_Report_CSV, Multi_Report

INPUT_FILENAME = "acts-user1.txt"
OUTPUT_FILENAME = "output.csv"

def for_each_addr_reporter_closure(reporter):
    def reporter_closure(user, addr):
        conn = user.find_last_addr_conn(addr)
        reporter.report_conn(conn)
    return reporter_closure

def main():
    date_filter = Filter("[0-3]?[0-9]/[0-1]?[0-9]/[0-2]0[0-2][0-9]", "dd/mm/yyyy")
    mac_filter = Filter("([0-9a-fA-F]{2}(:|-)){5}[0-9a-f-A-F]{2}")
    user_filter = Filter("(\S)+")

    cli_reporter = Fmt_Report_CLI(CLI_Output())
    file_reporter = Fmt_Report_CSV(File_Output(OUTPUT_FILENAME))
    m_reporter = Multi_Report(file_reporter, cli_reporter)

    f_in = File_Input(INPUT_FILENAME, True, 1)
    while True:

        cli_reporter.report_namelist(namelist(f_in))
        cli_reporter.flush()

        f_in.abs_seek(0)
        f_in.input_line()

        username, range_st, range_end = cli.cli_take_input(user_filter, date_filter)

        # redefinir user_filter para usar como filtro en el archivo, setear el formato tambien
        user_filter = Filter(username, username)

        user = parse(f_in, range_st, range_end, user_filter, date_filter, mac_filter)
        reporter_closure = for_each_addr_reporter_closure(m_reporter)
        user.for_each_addr(reporter_closure)

        cli_reporter.flush()
        if cli.cli_export_prompt():
            file_reporter.flush()

        if not cli.cli_continue_prompt():
            break

        f_in.abs_seek(0)
        m_reporter.clean()

if __name__ == "__main__":
    main()
