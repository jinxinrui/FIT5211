# !/usr/local/bin/python3


import math
import random
from assignment.Exercise3 import recursivelog
random.seed(0)
n = 100
ntest = 10

for b in range(2, 11):
    for _ in range(ntest):
        x = random.uniform(1, 10 ^ 6)
        mylog = recursivelog(n, x, b)
        mathlog = math.log(x, b)
        assert math.isclose(mylog, mathlog, abs_tol=0.00001), "for x={0} and b={1}, mylog={2} is not close enough to mathlog={3}".format(
            x, b, mylog, mathlog)
