#!/usr/bin/env python3

# basic shift cipher implementation
# @davidafsilva
from string import ascii_lowercase as cs

# enc(m1..mt, k) := c1..ct
#   where ci := [mi + k mod 26]
def enc(m, k):
    c = ''
    for cm in m:
        c += cs[(cs.index(cm) + k) % 26]
    return c

# dec(c1..ct, k) := m1..mt
#   where mi := [ci - k mod 26]
def dec(c, k):
    m = ''
    for cc in c:
        m += cs[(cs.index(cc) - k) % 26]
    return m

# test the cipher
print (enc("cryptoisfun",25))
print (dec(enc("cryptoisfun",25), 25))
