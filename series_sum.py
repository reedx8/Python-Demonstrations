'''Sum of the first nth term of Series'''
from decimal import Decimal

def series_sum(x):
    series = []
    b = 1.00    # series must start with '1' number, so I hardcoded it in.
    c = 1   # increments the denominator thru each iteration. See c in loop below.
    for series_number in range(0,x):
        series.append(("%.2f" % b)) # adds b to list & rounds it off @ 2 dec points
        b = 1/(c+3)    # renames b as a fraction from here on out. Incr.'s w/ c.
        c += 3
        print("b =", b)
        print("c =", c)
    print(series)
    print(sum(series))

number = int(input("Give me a number: "))
series_sum(number)
