import os
import math
from termios import B110


def func1(a, b1) -> int:
    return math.floor(a + b1)


def func2(a, b, c) -> str:
    return os.getcwd()
