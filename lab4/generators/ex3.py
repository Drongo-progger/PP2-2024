def tf(n):
    for i in range(0,n):
        if (i%3==0 and i%4==0):
            yield i 
n = int(input())
s = tf(n)
for i in s:
    print(i)           