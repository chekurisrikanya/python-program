def sumOfAP( a, d,n) :
    sum = 0
    i = 0
    while i < n :
        sum = sum + a
        a = a + d
        i = i + 1
    return sum
n = 4.8
a = 3.5
d = 7.7
print (sumOfAP(a, d, n))
 
