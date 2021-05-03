#!/usr/bin/env python3
import re

if __name__ == "__main__":
    expr = re.compile(".*[a-z].*[a-z].*")
    with open("consigna3") as f:
        while r := f.readline():
            found = expr.match(r)
            if not found:
                continue
            print(found.group())
