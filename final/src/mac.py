import re
mac_re = re.compile("([0-9a-fA-F]{2}(:|-)){5}[0-9a-f-A-F]{2}")
def validar_mac(mac):
    if not mac_re.match(mac):
        return False
    return True
