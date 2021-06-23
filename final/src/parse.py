from dates import dd_mm_yyyy_to_date
from common_const import *

from Conn import Conn

err_lines = []

def conn_line_filter(line, user_filter, date_filter, range_st_obj, range_end_obj, mac_filter):
    fields = line.split(CSV_SEP)

    # check username
    username = fields[USER_FIELD]
    if not user_filter.match(username):
        return None

    # check conn date
    conn_st = fields[CONN_ST_FIELD]
    conn_end = fields[CONN_END_FIELD]

    conn_date_st = conn_st.split(" ")[0]
    conn_date_end = conn_end.split(" ")[0]
    if not date_filter.match(conn_date_st) or not date_filter.match(conn_date_end):
        err_lines.append(line)
        return None

    conn_date_st_obj = dd_mm_yyyy_to_date(conn_date_st)
    conn_date_end_obj = dd_mm_yyyy_to_date(conn_date_end)

    if conn_date_end_obj < range_st_obj \
        or conn_date_st_obj >= range_end_obj:
        return None

    # check MAC
    mac = fields[MAC_FIELD]
    if not mac_filter.match(mac):
        err_lines.append(line)
        return None

    return Conn(mac, conn_st, conn_end)

def parse(inp, user, range_st, range_end, user_filter, date_filter, mac_filter):

    range_st_obj = dd_mm_yyyy_to_date(range_st)
    range_end_obj = dd_mm_yyyy_to_date(range_end)
    line = ""

    while line := inp.input_line():
        conn = conn_line_filter(line, user_filter, date_filter, range_st_obj, range_end_obj, mac_filter)
        if not conn:
            continue
        user.push_conn(conn)
    return user
