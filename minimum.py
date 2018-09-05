x=[8,3,5,9,1,0,56,5]
z=len(x)-1
i=0
for i in range(z):
    if x[i]<x[i+1]:
        y=x[i]
    else:
        y=x[i+1]
print(y)

