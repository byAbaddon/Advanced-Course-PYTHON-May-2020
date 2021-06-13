number_of_guests = int(input())
guests_list = [input() for _ in range(number_of_guests)]
vip_list = []

while True: 
    guest = input()
    if guest == 'END':
        print(len(guests_list))
        break
    else:
        if guest in guests_list:
            guests_list.remove(guest)


for guest in guests_list:
    if guest[0].isdigit():
        vip_list.append(guest)
        guests_list.remove(guest)

sorted_vip_list = sorted(vip_list)
for vip in sorted_vip_list:
    print(vip)

sorted_guests_list = sorted(guests_list)
for ordinary in sorted_guests_list:
    print(ordinary)    



