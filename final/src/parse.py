from dates import dd_mm_yyyy_to_date
from common import *

from Conn import Conn
from User import User

def check_username(user, user_field):
    if user.get_username() != user_field:
        return False
    return True

def check_date(range_st_obj, range_end_obj, conn_st_field, conn_end_field):
    conn_date_st = conn_st_field.split(" ")[0]
    conn_date_end = conn_end_field.split(" ")[0]

    if not date_filter.match(conn_date_st) or not date_filter.match(conn_date_end):
        return False

    conn_date_st_obj = dd_mm_yyyy_to_date(conn_date_st)
    conn_date_end_obj = dd_mm_yyyy_to_date(conn_date_end)

    if conn_date_end_obj < range_st_obj \
        or conn_date_st_obj > range_end_obj:
        return False

    return True

def check_mac(mac_field):
    if not mac_filter.match(mac_field):
        return False
    return True

def conn_line_filter(line, user, range_st_obj, range_end_obj):
    fields = line.split(CSV_SEP)

    # check username
    username = fields[USER_FIELD]
    if not check_username(user, username):
        raise ValueError("Username no coincide")

    # check MAC
    mac = fields[MAC_FIELD]
    if not check_mac(mac):
        raise ValueError("Error parseando mac address")

    # check conn date
    conn_st = fields[CONN_ST_FIELD]
    conn_end = fields[CONN_END_FIELD]
    if not check_date(range_st_obj, range_end_obj, conn_st, conn_end):
        raise ValueError("Error parseando fecha")

    return Conn(user, mac, conn_st, conn_end)

def parse(inp, username, range_st, range_end):

    user = User(username)
    range_st_obj = dd_mm_yyyy_to_date(range_st)
    range_end_obj = dd_mm_yyyy_to_date(range_end)
    line = ""

    i = 0
    while line := inp.getline():
        i += 1
        try:
            conn = conn_line_filter(line, user, range_st_obj, range_end_obj)
        except ValueError:
            continue
        user.push_conn(conn)
    return user
