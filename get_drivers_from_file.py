#!/usr/bin/python3

import sys

f_ = sys.argv[1]

drivers = []
f = open(f_, 'r')
lines = f.readlines()
for l in lines:
    l = l.strip()
    toks = l.split(" ")
    for tok in toks:
        if tok.startswith("driver=") or tok.startswith("Driver="):
            d = tok.split("=")[1]
            if d not in drivers:
                drivers.append(d)
            #print(tok.split("=")[1])
for d in drivers:
    print(d)
