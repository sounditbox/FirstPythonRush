a = []
for i in range(50):
    for j in range(30):
        if i % 3 == 0 and j % 7 == 0:
            if i + j < 15:
                a.append(i * j)
            else:
                a.append(i + j)
print(a)

print([i * j if i + j < 15 else i + j for i in range(50) for j in range(30) if i % 3 == 0 and j % 7 == 0])
