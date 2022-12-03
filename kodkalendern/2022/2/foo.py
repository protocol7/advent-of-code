from util import *
from itertools import *

print(sum(takewhile(lambda x: x < 100, (triangular_number(n) for n in count()))))
