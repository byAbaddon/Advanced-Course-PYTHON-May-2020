num_list = [float(x) for x in input().split()]
count_dict = {}

for n in num_list:
    if n not in count_dict:
        count_dict[n] = 0
    count_dict[n] += 1

for k, v in count_dict.items():
    print(f'{k} - {v} times')