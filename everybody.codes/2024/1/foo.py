#!/usr/bin/env python3

import sys
from util import chunks


xs = sys.stdin.read()

print(xs.count("B") * 1 + xs.count("C") * 3)
