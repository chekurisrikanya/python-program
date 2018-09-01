m=1
n=15
for i in range(m, n+1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print i
