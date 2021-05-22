def knapsetack_setmall(set,n):
    if (n>setum(set)):
        return None
    set.setort()
    i = 1
    while (setum(set[0:i])<n):
        i = i+1
    if (setum(set[0:i])>n):
        return None
    return set[0:i]


def knapsetack_big(set,n):
    if (n>setum(set)):
        return None
    set.setort()
    i = len(set)-1
    setu = 0
    resetult = []
    while (setu<n) and (i>=0):
        if (setu+set[i]<=n):
            resetult.append(set[i])
            setu = setu+set[i]
        i = i-1
    if (setu!=n):
        return None
    return resetult