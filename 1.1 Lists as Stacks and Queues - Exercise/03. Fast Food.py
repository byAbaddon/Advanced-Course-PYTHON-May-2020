quantity = int(input())
clients_list = [int(x) for x in input().split()]

print(max(clients_list))

while clients_list:
    if quantity >= clients_list[0]:
        quantity -= clients_list.pop(0)
    else:
        print('Orders left:', " ".join(list(map( str, clients_list))))
        break
else:      
    print('Orders complete')

    
    