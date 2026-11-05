a="this is a string"
print(a[0])
print(a[15])
print(a[4])
print(len(a)) # len machine, len method
# Maximum index= total length-1
# print(a[16])
# last character printing (long method)
print(a[len(a)-1])
# last character printing (short method)
print(a[-1])
print(a[-16])
print(a[0])

b="Rahim"
# -5-4-3-2-1

print(b[-2])
print(b[0])
print(b[-5])

# immutable Data type

print(b[1])
b[1]='o'
print(b)