import sys
import re
import getopt
from datetime import date

SEP = ";"
USER_FIELD = 1
C_INIT = 2
C_FIN = 3
MAC_FIELD = 8

MAC_IDX = 0

usuarios = {
    #"user": [
    #{
    #    "mac": "FF-FF-FF-FF-FF-FF"
    #    "c_init": 28/08/2019 10:06,
    #    "c_fin": 28/08/2019 10:06,
    #}]
}

usuarios_rep = []
err_lines = []

mac_re = re.compile("([0-9a-fA-F]{2}(:|-)){5}[0-9a-f-A-F]{2}")
def validar_mac(mac):
    if not mac_re.match(mac):
        return False
    return True

fecha_re = re.compile("[0-3][0-9]/[0-1][0-9]/[0-2]0[0-2][0-9]")
def validar_fecha(fecha):
    if not fecha_re.match(fecha):
        return False
    return True

def calc_max_rep(usuarios_rep, usuarios):
    max_rep = -1 * sys.maxsize
    for user in usuarios_rep:
        mac_count = len(usuarios[user])
        if mac_count > max_rep:
            max_rep = mac_count
    return max_rep

if __name__ == "__main__":
    # mega parseo de argumentos
    opt, args = getopt.getopt(sys.argv[1:], "i:f:", ["inicio=", "fin="])
    rango_init = None
    rango_fin = None
    for tup in opt:
        o = tup[0].replace("-","")
        if o[0] == "i":
            rango_init = tup[1]
            rango_init = [int(val) for val in rango_init.split("/")]
            rango_init = date(rango_init[2], rango_init[1], rango_init[0])
        if o[0] == "f":
            rango_fin = tup[1]
            rango_fin = [int(val) for val in rango_fin.split("/")]
            rango_fin = date(rango_fin[2], rango_fin[1], rango_fin[0])

    if not rango_init:
        rango_init = date(1, 1, 1)
    if not rango_fin:
        rango_fin = date(9999, 12, 31)

    # mega parseo de txt
    with open("acts-user1.txt", "r") as f:
        f.readline()
        for line in f:
            # campos iniciales
            fields = line.split(SEP)
            user = fields[USER_FIELD]
            mac = fields[MAC_FIELD].replace("\n", "")
            c_init = fields[C_INIT]
            c_fin = fields[C_FIN]

            # validacion de fecha en rango
            f_init = c_init.split(" ")[0]
            try:
                if not validar_fecha(f_init):
                    raise ValueError("Fecha Invalida")
            except ValueError:
                err_lines.append(line)
                continue
            f_init = [int(val) for val in f_init.split("/")]
            f_init = date(f_init[2], f_init[1], f_init[0])
            if rango_init > f_init or f_init > rango_fin:
                continue

            # validacion de mac
            try:
                if not validar_mac(mac):
                    raise ValueError("Mac Invalida")
            except ValueError:
                err_lines.append(line)
                continue

            # chequeo de usuarios
            if user in usuarios.keys():
                p = False
                i = 0
                while i < len(usuarios[user]):
                    # chequeo de macs
                    if mac == usuarios[user][i]["mac"]:
                        p = True
                        break
                    i += 1
                if p:
                    usuarios[user][i]["c_init"] = "Multiples conexiones"
                    usuarios[user][i]["c_fin"] = "Multiples conexiones"
                else:
                    usuarios[user].append({
                        "mac": mac,
                        "c_init": c_init,
                        "c_fin": c_fin
                        })
                    if user not in usuarios_rep:
                        usuarios_rep.append(user)

            else:
                usuarios[user] = [{
                    "mac": mac,
                    "c_init": c_init,
                    "c_fin": c_fin
                    }]

    max_rep = calc_max_rep(usuarios_rep, usuarios)

    # escritura de output
    with open("res.csv", "w") as f:
        header = "nombre de usuario"
        for i in range(max_rep):
            header += ",MAC_%d,Inicio de Conexion_%d,Fin de Conexion %d" % (i, i, i)
        f.write(header + "\n")
        for user in usuarios_rep:
            out = user
            for mac in usuarios[user]:
                c_init = "-" if mac["c_init"] is None else mac["c_init"]
                c_fin = "-" if mac["c_fin"] is None else mac["c_fin"]
                out += (",%s,%s,%s" % (mac["mac"], c_init, c_fin))
            f.write(out + "\n")
