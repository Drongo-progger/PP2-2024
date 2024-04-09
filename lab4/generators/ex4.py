def ab(a,b):
    for i in range(a,b+1):
        yield i**2
a= int(input())
b= int(input())
c=ab(a,b)
for i in c:
    print(i, end=",")