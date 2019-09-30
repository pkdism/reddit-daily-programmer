def tally(s):
    counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
    for i in s:
        if i in counts.keys():
            counts[i] += 1
        elif i.lower() in counts.keys():
            counts[i.lower()] -= 1

    sorted_keys = sorted(counts, key = counts.get, reverse = True)
    res = ""
    for k in sorted_keys:
        res += (k + ":" + str(counts[k]) + ", ")
    print(res)

tally("abcde")
tally("dbbaCEDbdAacCEAadcB")
tally("EbAAdbBEaBaaBBdAccbeebaec")
