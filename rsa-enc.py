#!/usr/bin/env python3
from fractions import gcd
import pip, sys, argparse, random

#Parses Arguments
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Process flags for the program.')
    parser.add_argument('-k','--key', required= 'True', help='key file')
    parser.add_argument('-i','--input', required= 'True', help='input file')
    parser.add_argument('-o','--output', required= 'True', help='output file')
    results = parser.parse_args(args)
    return (results.key, results.input, results.output)

def mod_exp(n, e, m):
    if m == 1: return 0
    rv = 1
    n = n % m
    while e > 0:
        if e & 1 == 1:
            rv = (rv * n) % m
        e >>= 1
        n = (n ** 2) % m
    return rv

def rsa_encrypt(m, l, N, e):
    pad = (1 << (l - 1))
    print(m)
    m |= pad
    print(m)
    return mod_exp(m, e, N)

k, i, o = check_arg(sys.argv[1:])

key = open(k, 'r').read()
pub_key = key.split()
value = int(open(i, 'r').read())
c = rsa_encrypt(value, int(pub_key[0]), int(pub_key[1]), int(pub_key[2]))

output = open(o, 'w')
output.write(str(c))
