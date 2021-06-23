class Output:
    def write_output(self, msg):
        pass

CLI_OUTPUT = 1
class CLI_Output(Output):
    def __init__(self):
        pass

    def write_output(self, msg):
        print(msg)

FILE_OUTPUT = 2
class File_Output(Output):
    def __init__(self, filename, mode="w"):
        self.filename = filename
        self.mode = mode
        self.file_handle = None

    def write_output(self, msg):
        if not self.file_handle:
            self.file_handle = open(self.filename, self.mode)
        self.file_handle.write(msg)

    def __end__(self):
        if self.file_handle is not None:
            self.file_handle.close()
