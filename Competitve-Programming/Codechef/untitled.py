__author__ = 'Akshay'

"""
Created on Fri Jan 17 17:19:18 2014
"""

'''a=(raw_input(''))
while (int(a)>0):
    if(a[:]==a[::-1]):
        print a
        break
    else:
        a=str(int(a)+1)'''

'''a=int(raw_input('limit'))
b=int(raw_input('number'))
count=0
for i in range(1,a+1):
    for j in range(i+1,a+1):
        if((i+j)%b==0):
            count=count+1

        else:
            continue
print (count)'''

a = int(raw_input('enter the no of cells'))
e = []
f = []

for i in range(a):
    b = raw_input('enter the individual cells')
    c, d = b.split(' ')
    print(c, d)
    e.append(c)
    print(e)
    f.append(d)

def sum(x=[]):
    c = 0

    for i in x:
        if x.count(i) > 1:
            c = c + x.count(i)
            x.remove(i)

        return c
g=sum(e)
h=sum(f)
print(-g - h + a + 1)
