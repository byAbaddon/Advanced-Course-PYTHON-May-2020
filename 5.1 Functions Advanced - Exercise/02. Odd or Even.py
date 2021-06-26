command = input()
num_list = input().split()

even_list = [int(x) for x in num_list if not int(x) & 1]
odd_list = [int(x) for x in num_list if  int(x) & 1]

if command == 'Even':
    print(sum(even_list) * len(num_list))
else:
    print(sum(odd_list) * len(num_list))   
