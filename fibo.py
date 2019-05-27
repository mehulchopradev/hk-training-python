n = int(input('Enter n : '))

a, b = 0, 1

print(a)
print(b)

for v in range(1, n - 1):
    c = a + b
    print(c)
    a, b = b, c