# !/usr/local/bin/python3


def pair_search(l, p):
    assert(len(l) > 0)
    found = False
    calls = 1
    mid = len(l) // 2
    if l[mid] == p:
        found = True
        return found, calls
    elif len(l) == 1 and l[0] != p:
        return found, calls
    else:
        if (l[mid][0] == p[0] and l[mid][1] > p[1]) or \
            (l[mid][0] > p[0] and l[mid][1] == p[1]) or \
                (l[mid][0] > p[0] and l[mid][1] > p[1]):
            searchresult = pair_search(l[0:mid], p)
            found = searchresult[0] or found
            calls = calls + searchresult[1]
            # print("left")
            # print(calls)
        elif (l[mid][0] == p[0] and l[mid][1] < p[1]) or\
            (l[mid][0] < p[0] and l[mid][1] == p[1]) or\
                (l[mid][0] < p[0] and l[mid][1] < p[1]):
            if len(l) != 2:
                searchresult = pair_search(l[mid + 1:len(l)], p)
                found = searchresult[0] or found
                calls = calls + searchresult[1]
                # print('right')
                # print(calls)
        else:
            if len(l) == 2:
                searchresult = pair_search(l[0], p)
                found = searchresult[0] or found
                calls = calls + searchresult[1]
                # print()
                # print(calls)
            else:
                searchresultA = pair_search(l[0:mid], p)
                searchresultB = pair_search(l[mid + 1:len(l)], p)
                found = searchresultA[0] or searchresultB[0] or found
                calls = calls + searchresultA[1] + searchresultB[1]
                # print(calls)
        return found, calls


L = [(0, 1), (1, 0), (0, 1), (1, 1), (1, 2), (3, 1), (3, 1), (2, 2),
     (2, 3), (3, 2), (2, 3), (4, 3), (3, 4), (4, 4), (4, 5), (5, 5)]

for item in L + [(0, 0), (2, 1), (3, 3), (5, 4)]:
    found, calls = pair_search(L, item)
    iteminl = item in L
    assert found == iteminl, "Found item {} {} time(s) instead of {}".format(
        item, int(found), int(iteminl))
    print("Found {} {} time(s) in {} calls".format(item, int(iteminl), calls))


for item in [(0, 0), (2, 1), (3, 3), (5, 4)]:
    found, calls = pair_search(L, item)
    iteminl = item in L
    assert found == iteminl, "Found item {} {} time(s) instead of {}".format(
        item, int(found), int(iteminl))
    print("Found {} {} time(s) in {} calls".format(item, int(iteminl), calls))
