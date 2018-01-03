#sept 5-6, 2017
'''
Details: If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Finish the
solution so that it returns the sum of all the multiples of 3 or 5 below
the number passed in.
Note: If the number is a multiple of both 3 and 5, only count it once.
'''

def solution(num):
    numbers3 = []
    numbers5 = []
    i = 1
    z = 3
    y = 5
    while z < num:
        numbers3.append(z)
        i += 1
        z = 3 * i
    i = 1
    while y < num:
        numbers5.append(y)
        i += 1
        y = 5 * i

    combList = numbers3
    for i in numbers5:
        if i not in numbers3:
            combList.append(i)

    combList.sort()
    total = sum(combList)

    print(f"Here are the multiples of 3 and 5 below {num}:")
    print(combList)
    print("Sum of those multiples:")
    return total
