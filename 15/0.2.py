def nat_nums():
    n = 1
    while True:
        yield n
        n += 1


gen1 = nat_nums()
gen2 = nat_nums()

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen2))
print(next(gen2))
print(next(gen2))
