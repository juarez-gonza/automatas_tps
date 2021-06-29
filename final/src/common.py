from Filter import Filter

CSV_SEP = ";"
USER_FIELD = 1
CONN_ST_FIELD = 2
CONN_END_FIELD = 3
MAC_FIELD = 8

date_filter = Filter("[0-3]?[0-9]/[0-1]?[0-9]/[0-2]0[0-2][0-9]", "dd/mm/yyyy")
mac_filter = Filter("([0-9a-fA-F]{2}(:|-)){5}[0-9a-f-A-F]{2}")
user_filter = Filter("(\S)+")
