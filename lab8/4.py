import math
import time

def sq(n, delay_ms):
    sec = delay_ms / 1000.0
    time.sleep(sec)
    result = math.sqrt(n)
    print(f"Square root of {n} after {msec} miliseconds is {result}")

n = int(input())
msec = int(input())
sq(n, msec)