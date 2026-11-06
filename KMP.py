def failure(P):
    F = [0] * len(P)
    k = 0
    for j in range(1, len(P)):
        while k > 0 and P[j] != P[k]:
            k = F[k - 1]
        if P[j] == P[k]:
            k += 1
        F[j] = k
    return F

def kmp(T, P):
    F= failure(P)
    j=0
    out=[]
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = F[j - 1]
        if T[i] == P[j]:
            j += 1
        if j == len(P):
            out.append(i - len(P) + 1)
            j = F[j - 1]
    return out

T = "UNIVERSITY"
P = "VER"
print(failure(P))
print( kmp(T, P))
