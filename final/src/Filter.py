import re

class Filter:
    def __init__(self, regex, fmt=""):
        self.expr = re.compile(regex)
        self.fmt = fmt

    def match(self, string):
        return self.expr.match(string)

    def get_fmt(self):
        return self.fmt
