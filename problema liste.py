x=[1,10,4,3,-6,8,-5,7,0]
y=x.copy()
print(x)
b=sorted(x)
print(b)
c=b
c.sort(reverse=True)
print(c)
print(len(x))
print(max(x))
print(min(x))
x.extend([111])
print(x)
y.insert(2,222)
print(y)