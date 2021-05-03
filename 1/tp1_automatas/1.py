#!/usr/bin/env python3
import re

if __name__ == "__main__":
    expr = re.compile("[A-Za-z\.]+@.*\.?um\.edu\.ar")
    with open("consigna1") as f:
        while r := f.readline():
            found = expr.match(r)
            if not found:
                continue
            print(found.group())
