import sys

class Input:
    def input_all(self):
        pass

    def input_line(self):
        pass

    def abs_seek(self, pos):
        pass

    def tell(self):
        pass

    def __end__(self):
        pass

CLI_INPUT = 1
class CLI_Input(Input):
    def __init__(self):
        pass

    def input_line(self):
        return input()

    def input_all(self):
        return sys.stdin.read()

    def abs_seek(self, pos):
        return

    def tell(self):
        return

FILE_INPUT = 2
class File_Input(Input):
    def __init__(self, filename, skip_header, header_lines=0):
        self.filename = filename
        self.file_handle = open(filename, "r")
        i = 0
        while i < header_lines and skip_header:
            self.file_handle.readline()
            i += 1

    def input_line(self):
        return self.file_handle.readline().replace("\n", "")

    def input_all(self):
        return self.file_handle.read()

    def abs_seek(self, pos):
        self.file_handle.seek(pos)

    def tell(self):
        return self.file_handle.tell()

    def __end__(self):
        self.file_handle.close()
