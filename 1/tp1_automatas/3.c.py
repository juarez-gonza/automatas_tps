#!/usr/bin/env python3
import re
import sys

if __name__ == "__main__":
    expr = re.compile(".*(\W|[0-9])\S.*")
    with open("consigna3") as f:
        while r := f.readline():
            found = expr.match(r)
            if not found:
                continue
            print(found.group())
