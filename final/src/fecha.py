import re
from datetime import date

fecha_re = re.compile("[0-3]?[0-9]/[0-1]?[0-9]/[0-2]0[0-2][0-9]")
def validar_fecha(fecha):
    if not fecha_re.match(fecha):
        return False
    return True

DATE_SEP = "/"
def _dd_mm_yyyy_to_date(string):
    listf = [int(val) for val in string.split(DATE_SEP)]
    return date(listf[2], listf[1], listf[0])

def dd_mm_yyyy_to_date(string):
    if not validar_fecha(string):
        raise ValueError("Formato %s no reconocido, el formato aceptado es dd/mm/yyyy" % string)
    return _dd_mm_yyyy_to_date(string)
