import os

from dates import dd_mm_yyyy_to_date

from Conn import Conn

from Output import File_Output
from Input import File_Input

CSV_SEP = ";"
USER_FIELD = 1
CONN_ST_FIELD = 2
CONN_END_FIELD = 3
MAC_FIELD = 8

err_lines = []

def namelist(f_in):

    if namelist.namecache:
        pass
    elif os.path.isfile(namelist.NAMECACHE_FILENAME):
        f_cache_in = File_Input(namelist.NAMECACHE_FILENAME, False)
        namelist.namecache = [*f_cache_in.input_line().split(",")]
        del f_cache_in
    else:
        f_out = File_Output(namelist.NAMECACHE_FILENAME)

        line = ""
        while line := f_in.input_line():
            fields = line.split(CSV_SEP)
            username = fields[USER_FIELD]
            if username not in namelist.namecache:
                namelist.namecache.append(username)
        f_out.write_output(",".join(namelist.namecache))

        del f_out

    return namelist.namecache
# static variables @ namelist
namelist.namecache = []
namelist.NAMECACHE_FILENAME = "namecache.txt"

def line_parse(line, range_st_obj, range_end_obj, user_filter, date_filter, mac_filter):
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

    return Conn(mac, conn_date_st_obj, conn_date_end_obj)

def parse(inp, user, range_st_obj, range_end_obj, user_filter, date_filter, mac_filter):
    line = ""
    while line := inp.input_line():
        conn = line_parse(line, range_st_obj, range_end_obj, user_filter, date_filter, mac_filter)
        if conn:
            user.push_conn(conn)
