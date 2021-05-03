#!/usr/bin/env python3

import re



if __name__ == "__main__":

    expr = re.compile("(0|\+54 9)? ?([0-9]{4})? ?(15)? ?[0-9]{2}-[0-9]{4}")

    with open("consigna7") as f:
        while r := f.readline():
            found = expr.match(r)
            if not found:
                continue
            print(found.group())
