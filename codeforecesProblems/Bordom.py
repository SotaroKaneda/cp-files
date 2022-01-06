input()
numbers = map(int, input().split())
z=[0]*(100001)
for i in numbers:
    z[i] += i
a=b=0
for i in z:
    a, b = max(a, b + i), a
print(a)
