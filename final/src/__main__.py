# IO simple
from Input import File_Input, CLI_Input
from Output import File_Output, CLI_Output

# IO por encima de la interfaz simple
from User_Input import CLI_User_Input
from Conn_Reporter import CLI_Conn_Reporter, CSV_Conn_Reporter

# Cache de nombres
from Name_Cache import Name_Cache_CSV, print_namelist

from User import User, addr_f_obj

from parse import parse

INPUT_FILENAME = "acts-user1.txt"
OUTPUT_FILENAME = "output.csv"

def main():
    inp = CLI_Input()
    outp = CLI_Output()
    cli_input = CLI_User_Input(inp, outp)
    file_input = File_Input(INPUT_FILENAME, True, 1)
    namecache = Name_Cache_CSV()

    while True:
        cli_reporter = CLI_Conn_Reporter(outp)
        file_reporter = CSV_Conn_Reporter(File_Output(OUTPUT_FILENAME))

        print_namelist(outp, namecache.namelist(file_input))
        username, range_st, range_end = cli_input.main_input()

        user = User(username)
        parse(file_input, user, range_st, range_end)

        addr_fc = addr_f_obj(cli_reporter, file_reporter)
        user.for_each_addr(addr_fc)

        cli_reporter.flush()
        if cli_input.export_prompt():
            file_reporter.flush()

        if not cli_input.continue_prompt():
            break

        file_input.abs_seek(0)

if __name__ == "__main__":
    main()
