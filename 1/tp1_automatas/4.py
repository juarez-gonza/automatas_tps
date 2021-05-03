#!/usr/bin/env python3
import re

if __name__ == "__main__":
    expr = re.compile("(.+://)?(.*\\.)+([a-zA-Z0-9_\\-]+/?)+(\\?.*=.*&?)?")
    with open("consigna4") as f:
        while r := f.readline():
            found = expr.match(r)
            if not found:
                continue
            print(found.group())
