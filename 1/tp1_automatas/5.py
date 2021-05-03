#!/usr/bin/env python3

import re



if __name__ == "__main__":
    expr = re.compile("([0-9]{1,3}\.){3}([0-9]{1,3})")

    with open("consigna5") as f:
        while r := f.readline():
            found = expr.match(r)
            if not found:
                continue
            print(found.group())
