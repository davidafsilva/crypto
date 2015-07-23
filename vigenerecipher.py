#!/usr/bin/env python3

# basic vigenere cipher implementation
# @davidafsilva
from string import ascii_lowercase as cs
from math import ceil

# pads or cuts the according the length l
def key(k, l):
    return (k * ceil(l/len(k)))[:l]

# enc(m1..mt, k) := c1..ct
#   where
#      k -> k1..kt (cut or repeat)
#      ci := [mi + ki mod 26]
def enc(m, k):
    c = ''
    pk = key(k, len(m))
    for idx, cm in enumerate(m):
        c += cs[(cs.index(cm) + cs.index(pk[idx])) % len(cs)]
    return c

# dec(c1..ct, k) := m1..mt
#   where
#      k -> k1..kt (cut or repeat)
#      mi := [ci - ki mod 26]
def dec(c, k):
    m = ''
    pk = key(k, len(c))
    for idx, cc in enumerate(c):
        m += cs[(cs.index(cc) - cs.index(pk[idx])) % len(cs)]
    return m

# test the cipher
print (enc("seeyouatnoon", "spy"))
print (dec(enc("seeyouatnoon", "spy"), "spy"))
