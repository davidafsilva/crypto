#!/usr/bin/env python3

# vigenere cipher variant implementation
# adds support for cp1251 unicode characters
# @davidafsilva
from math import ceil
from binascii import hexlify, unhexlify

# pads or cuts the according the length l
def key(k, l):
    return (k * ceil(l/len(k)))[:l]

# enc(m1..mt, k) := c1..ct
#   where
#      k -> k1..kt (cut or repeat)
#      ci := [mi xor ki]
def enc(m, k):
    return hexlify(bytes("".join(chr(ord(x) ^ ord(y)) for x, y in zip(m, key(k, len(m)))), "cp1251"))

# dec(c1..ct, k) := m1..mt
#   where
#      k -> k1..kt (cut or repeat)
#      mi := [ci xor ki]
def dec(c, k):
    m = unhexlify(c)
    return "".join(chr(x ^ y) for x, y in zip(m, bytes(key(k, len(m)), "cp1251")))

# test the cipher
print (enc("tellhimaboutme", "cafe"))
print (dec(enc("tellhimaboutme", "cafe"), "cafe"))
