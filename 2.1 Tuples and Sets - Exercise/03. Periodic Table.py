n = int(input())
element_set = set()

while n:
    n -= 1
    for el in input().split():
        element_set.add(el)

for el in element_set:
    print(el)