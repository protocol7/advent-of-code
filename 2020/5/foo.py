import sys
import re

print(max([int(re.sub("[FL]", "0", re.sub("[BR]", "1", l)), 2) for l in sys.stdin]))