n=int(input('enter the num of strings'))
l=[]
s=[]
c=1
z=0

print('enter the strings')
for i in range(n):
    s.append(input())
m= min(len(x) for x in s)
for j in range(0,m):
    c=1
    for i in range(1,n):
        if s[i-1][j]==s[i][j]:
            c=c+1
        else:
            z=1
            break

        if c==n:
            l.append(s[i][j])
    if z==1:
        break


print(l)
