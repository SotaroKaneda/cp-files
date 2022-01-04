weight = float(input()) 
positive = False
even = False
if weight > 3:
    positive = True
if weight % 2 == 0:
    even = True
if even & positive:
    print("YES")
else:
    print("NO")

