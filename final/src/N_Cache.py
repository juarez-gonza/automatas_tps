from os import path

from Output import File_Output
from Input import File_Input

from common_const import *

# Cache de lista de nombres para evitar leer todo el archivo en busca
# de nombres cuando posible

class N_Cache:
    # @f_in: instancia de File_Input por si falla la obtencion de cache
    def namelist(self, f_in):
        pass

class N_Cache_CSV(N_Cache):
    def __init__(self, namecache_filename=".namecache.csv"):
        self.namecache = []
        self.namecache_filename = namecache_filename

    def namelist(self, f_in):
        if self.namecache:
            pass
        elif path.isfile(self.namecache_filename):
            self._got_filecache()
        else:
            self._no_cache(f_in)

        return self.namecache

    def _got_filecache(self):
        f_cache_in = File_Input(self.namecache_filename, False)
        self.namecache = [*f_cache_in.input_line().split(",")]
        del f_cache_in

    def _no_cache(self, f_in):
        # caller no espera cambios en su posicion de lectura en f_in
        f_in_pos = f_in.tell()

        f_out = File_Output(self.namecache_filename)

        line = ""
        while line := f_in.input_line():
            fields = line.split(CSV_SEP)
            username = fields[USER_FIELD]
            if username not in self.namecache:
                self.namecache.append(username)
        f_out.write_output(",".join(self.namecache))

        del f_out

        # restorar posicion en f_in
        f_in.abs_seek(f_in_pos)
