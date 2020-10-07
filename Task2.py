s = 0
i = 1
f = [ 1 , 1 ]
while f[i] < 4000000:
    if f[i] % 2 == 0:
        s += f[i]
    f.append(f[i-1] + f[i])
    i += 1
print(s)
