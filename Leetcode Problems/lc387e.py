"""
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

Note: You may assume the string contains only lowercase English letters.
"""

import collections


def firstUniqChar(s):
    c = collections.Counter(s)
    for i, x in enumerate(s):
        if c[x] == 1:
            return i
    return -1
