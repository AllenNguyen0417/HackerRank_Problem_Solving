c = [0,0,1,0,0,1,1,0]
n = 8
k = 2

res = 100
i = k
if n != k:
    if c[k] == 0:
        res -= 1
    else:
        res = res - 1 - 2
    while i != 0:
        i = (i + k) % n
        if c[i] == 0:
            res -= 1
        else:
            res = res - 1 - 2
else:
    if c[0] == 0:
        res -= 1
    else:
        res = res - 1 - 2
 

print(res)