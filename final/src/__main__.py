import sys

from Input import *
from mac import *
from Conexion import *
from User import *

from User_Write import *
from Conn_Write import *

in_filename = "acts-user1.txt"
CSV_SEP = ";"
USER_FIELD = 1
CONN_INIT_FIELD = 2
CONN_FIN_FIELD = 3
MAC_FIELD = 8

argsp = {}
err_lines = []

def line_parse(line, argsp):
    global CSV_SEP, USER_FIELD, MAC_FIELD, CONN_INIT_FIELD, CONN_FIN_FIELD
    fields = line.split(CSV_SEP)

    user = fields[USER_FIELD]
    if user != argsp["user"]:
        return None

    conn_init = fields[CONN_INIT_FIELD]
    conn_fin = fields[CONN_FIN_FIELD]

    conn_fecha_init = conn_init.split(" ")[0]
    conn_fecha_fin = conn_fin.split(" ")[0]

    try:
        conn_fecha_init = dd_mm_yyyy_to_date(conn_fecha_init)
        conn_fecha_fin = dd_mm_yyyy_to_date(conn_fecha_fin)
    except ValueError:
        err_lines.append(line)
        return None

    if conn_fecha_fin < argsp["rango_init"] or conn_fecha_init >= argsp["rango_fin"]:
        return None

    mac = fields[MAC_FIELD]
    try:
        if not validar_mac(mac):
            raise ValueError("Mac Invalida")
    except ValueError:
        err_lines.append(line)
        return None

    return Conexion(mac, conn_fecha_init, conn_fecha_fin)

def file_parse(filepath):
    user = User(argsp["user"])

    with open(filepath, "r") as f:
        f.readline() # lee el header
        for line in f:
            line = line.replace("\n","")
            conn = line_parse(line, argsp)
            if conn:
                user.push_conn(conn)

    return user

if __name__ == "__main__":
    while True:
        argsp = CLI_Input().take_input()
        user = file_parse(in_filename)
        user_writer = User_Write_CLI(user, Conn_Write_CLI())
        print(user_writer.write())

        if "y" in input("Desearia exportar esto a un archivo .csv?[Y/n]").lower():
            with open("output.cvs", "w") as f:
                user_writer = User_Write_CSV(user, Conn_Write_CSV())
                f.write(user_writer.write())

        if "n" in input("Desearia reutilizar el programa?[Y/n]").lower():
            break
