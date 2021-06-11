water = int(input())
people = []

while True:
    token = input()
    if token == 'Start':
        break
    people.append(token)

while True:
    token = input().split()
    if token[0] == 'End':
        print(f'{water} liters left')
        break
    elif token[0] == 'refill':
        water += int(token[1])
    else:
        person_name = people.pop(0)
        if  water >= int(token[0]):
            water -= int(token[0]) 
            print(f'{person_name} got water')
        else:
            print(f'{person_name} must wait')

        