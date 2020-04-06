"""
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
"""


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    appeared = {n}
    while n != 1:
        nums = []
        n = str(n)
        for i in n:
            nums.append(int(i))
        n = 0
        for i in nums:
            n += i*i
        if n in appeared:
            return False
        else:
            appeared.add(n)
    return True


inp = 19
exp = True
print(isHappy(inp) is True)