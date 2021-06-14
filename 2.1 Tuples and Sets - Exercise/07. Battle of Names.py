loop = int(input())
odd_num_set = set()
even_num_set = set()

for index in range(1, loop + 1):
    ascii_sum  = sum([ord(x) for x in  input()]) // index
    if ascii_sum & 1:
        odd_num_set.add(ascii_sum)
    else:
        even_num_set.add(ascii_sum)
         
odd_sum = sum(odd_num_set)
even_sum = sum(even_num_set)

if even_sum == odd_sum:
    result = odd_num_set.union(even_num_set)
    print(', '.join(str(x) for x in result))
elif odd_sum > even_sum:
    result = odd_num_set.difference(even_num_set)
    print(', '.join(str(x) for x in result)) 
else:
    result = odd_num_set.symmetric_difference(even_num_set)
    print(', '.join(str(x) for x in result))   