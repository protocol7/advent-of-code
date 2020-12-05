import sys
import re

a = sorted([int(re.sub("[FL]", "0", re.sub("[BR]", "1", l)), 2) for l in sys.stdin])

print(*(set(range(a[0], a[-1])) - set(a)))
