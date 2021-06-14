n, m = input().split()
one_set  = {input() for _ in range(int(n))}
two_set  = {input() for _ in range(int(m))}

for numbers in one_set.intersection(two_set):
    print(numbers)