import sys
from collections import *
from itertools import *
from util import *

c = 0
for i in range(2, 401):
    c += str(i * i).endswith(str(i))

print(c)