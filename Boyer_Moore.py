def boyer_moore(text, pat):
    n = len(text)
    m = len(pat)
    dect = {}
    for x in range(m):
        dect[pat[x]] = x
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        c = text[s + j]
        s += max(1, j - dect.get(c, -1))
    return -1

text = "BANANABREAD"
pat = "ANA"
r = boyer_moore(text, pat)
print(r)
