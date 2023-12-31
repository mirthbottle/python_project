"""Show the problem with floats

and how to profile

You can run things that are in a string
but you have to separately import Decimal
It doesn't take the definition from the module

cProfile.run("sum([Decimal('0.1')]*1000)")

It's better to use with cProfile.Profile() anyway
"""

import cProfile
import math
from decimal import Decimal, getcontext

f = 1.2 - 1
f != 0.2

f = sum([float(0.1)] * 10)
f != 1

math.fsum([0.1] * 10) == 1

with cProfile.Profile() as pr:
    sum([0.1] * 10)

    pr.print_stats()
