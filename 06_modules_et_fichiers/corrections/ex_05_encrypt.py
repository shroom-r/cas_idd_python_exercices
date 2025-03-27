#!/usr/bin/env python

import sys
import pathlib

filename = "06_modules_et_fichiers/corrections/test.txt"
key = "test"
# try:
#     filename, key = sys.argv[1:]
# except:
#     print(f'usage: {sys.argv[0]} file key')
#     sys.exit(1)

try:
    # Ouvrir le fichier binaire en lecture-écriture
    f = open(filename, 'r+b')
except Exception as e:
    print("Erreur à l'ouverture du fichier:")
    print(e)
    sys.exit(1)

index = 0
key = bytes(key, encoding='utf-8')
l = len(key)

print(repr(key)[2:-1])

while c := f.read(1):
    val = key[index]
    encrypted = bytes([c[0] ^ key[index]])
    f.seek(-1, 1)
    f.write(encrypted)
    index = (index + 1) % l

f.close()