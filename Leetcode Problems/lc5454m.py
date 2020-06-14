def findLeastNumOfUniqueInts(arr, k):
    d = {}
    for n in arr:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    sl = [*d.values()]
    sl.sort()
    r = len(sl)
    i = 0
    while k > 0:
        k -= sl[i]
        r -= 1
        i += 1
    return r if k == 0 else r + 1
