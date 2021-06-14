loop = int(input())
names_set = { input() for _ in range(loop)}

for names in names_set:
    print(names)