a = int(input())
b = int(input())
c = int(input())

# put your python code here
edge_sum = 4*(a + b + c)
surface_sum = 2*(a*b+b*c+a*c)
v = a*b*c

print(edge_sum)
print(surface_sum)
print(v)