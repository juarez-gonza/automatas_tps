#!/usr/bin/env python3

import re



if __name__ == "__main__":

    expr = re.compile("[A-Z]?[0-9]{4}([A-Z]{3})?")

    with open("consigna8") as f:
        while r := f.readline():
            found = expr.match(r)
            if not found:
                continue
            print(found.group())
