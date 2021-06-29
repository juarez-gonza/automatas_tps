from os import path

from Output import File_Output
from Input import File_Input

from common import *

# Cache de lista de nombres para evitar leer todo el archivo en busca
# de nombres cuando posible

def print_namelist(output, namelist):
    out_buff = "Lista de usernames:\n"
    for i in range(len(namelist)):
        out_buff  += ("%s" % namelist[i]).center(20)
        if (i+1) % 4 == 0:
            out_buff += "\n"
    output.write(out_buff + "\n")

class Name_Cache:
    # @file_input: instancia de File_Input por si falla la obtencion de cache
    def namelist(self, file_input):
        pass

class Name_Cache_CSV(Name_Cache):
    def __init__(self, namecache_filename=".namecache.csv"):
        self.namecache = []
        self.namecache_filename = namecache_filename

    def namelist(self, file_input):
        if self.namecache:
            pass
        elif path.isfile(self.namecache_filename):
            self._got_filecache()
        else:
            self._no_cache(file_input)

        return self.namecache

    def _got_filecache(self):
        f_cache_in = File_Input(self.namecache_filename, False)
        self.namecache = [*f_cache_in.getline().split(",")]
        del f_cache_in

    def _no_cache(self, file_input):
        # caller no espera cambios en su posicion de lectura en file_input
        file_input_pos = file_input.tell()

        file_output = File_Output(self.namecache_filename)

        line = ""
        while line := file_input.getline():
            fields = line.split(CSV_SEP)
            username = fields[USER_FIELD]
            if username not in self.namecache:
                self.namecache.append(username)
        file_output.write(",".join(self.namecache))

        del file_output

        # restorar posicion en file_input
        file_input.abs_seek(file_input_pos)
