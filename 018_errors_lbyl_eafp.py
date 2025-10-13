# LBYL - look before your leap
dictionary = {}
if "key" in dictionary:
    value = dictionary["key"]
else:
    value = None

items = []
if len(items) > 0:
    first = items[0]
else:
    first = None

import os
if os.path.exists("data.txt"):
    with open("data.txt") as f:
        content = f.read()

#EAFP - Easier ask fogiveness than permission
try:
    value = dictionary["key"]
except KeyError:
    value = None

try:
    first = items[0]
except IndexError:
    first = None

try:
    with open("data.txt") as f:
        content = f.read()
except FileNotFoundError:
    content = ""