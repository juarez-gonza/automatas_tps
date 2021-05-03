#!/usr/bin/env python3
import sys
import os

# programita para solucionar el carriage return de windows
# desarrolladores involucrados en este tp (? usaron windows
# y sus newline '\n' no venían solos ('\r' <-- tiene la culpa)

if __name__ == "__main__":
    if len(sys.argv) < 1 or not os.path.isfile(sys.argv[1]):
        print("Usage: %f filepath" % __file__)
        sys.exit(1)

    fd = os.open(sys.argv[1], os.O_RDWR) # el argumento tiene q ser el archivo con '\r' en sus newline.
    c = b""
    while c := os.read(fd, 1):
        if c == b'\x0D':
            os.lseek(fd, -1, os.SEEK_CUR)
            os.write(fd, b'\x0A')
    sys.exit(0)
