import os
os.system('clear')

people = input().split()
n = int(input())

while len(people) != 1:
    for i in range(1, n):
        people.append(people.pop(0))
    else:
        print('Removed', people.pop(0))

print('Last is', people.pop())