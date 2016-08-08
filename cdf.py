#!/usr/bin/python3

import sys

with open(sys.argv[1], 'r') as test_cases:
    lista = [float(x) for x in test_cases]
    size = len(lista)

    for i, test in enumerate(lista):
        print("%f    %f" % (test,(i+1)/size))
