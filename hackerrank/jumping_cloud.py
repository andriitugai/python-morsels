import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    idx = 0

    while idx < len(c)-1:
        # distance to the next thunder:
        ptr = idx
        while ptr < len(c)-1 and c[ptr+1] != 1:
            ptr += 1

        # ptr stopped before thunder
        dist = ptr - idx
        jumps += math.ceil(dist/2)
        idx = ptr
        # if it's the last cloud
        if idx == len(c) - 1:
            break
        # jump over
        jumps += 1
        idx += 2

    return jumps


if __name__ == '__main__':
    print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))