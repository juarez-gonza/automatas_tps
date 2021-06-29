# Abstraer lo basico necesario para generar output ya sea
# por CLI, archivos, etc.

import sys

class Output:
    def write(self, msg):
        pass

class CLI_Output(Output):
    def __init__(self):
        pass

    def write(self, msg):
        sys.stdout.write(msg)
        sys.stdout.flush()

class File_Output(Output):
    def __init__(self, filename, mode="w"):
        self.filename = filename
        self.mode = mode
        self.file_handle = None

    def write(self, msg):
        if not self.file_handle:
            self.file_handle = open(self.filename, self.mode)
        self.file_handle.write(msg)
        self.file_handle.flush()

    def __end__(self):
        if self.file_handle is not None:
            self.file_handle.close()
