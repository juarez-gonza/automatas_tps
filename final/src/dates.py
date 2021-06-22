from datetime import date

DATE_SEP = "/"
def dd_mm_yyyy_to_date(string):
    listf = [int(val) for val in string.split(DATE_SEP)]
    return date(listf[2], listf[1], listf[0])

def date_to_dd_mm_yyyy(date_obj):
    date_str = str(date_obj).split("-")
    dd = date_str[2]
    mm = date_str[1]
    yyyy = date_str[0]
    return dd + DATE_SEP + mm + DATE_SEP + yyyy
