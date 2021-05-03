#!/usr/bin/env python3
import re

if __name__ == "__main__":
    expr = re.compile("([A-Za-z0-9]|_){4,15}")
    with open("consigna2") as f:
        while r := f.readline():
            found = expr.match(r)
            if not found:
                continue
            print(found.group())
