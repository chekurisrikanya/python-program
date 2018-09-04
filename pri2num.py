lower = 900
upper=1000

print("Prime numbehttps://www.programiz.com/python-programming/examples/prime-number-intervalsrs between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
