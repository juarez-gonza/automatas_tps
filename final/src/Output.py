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
        self.file_handle = open(filename, mode)

    def write_output(self, msg):
        self.file_handle.write(msg)

    def __end__(self):
        self.file_handle.close()
