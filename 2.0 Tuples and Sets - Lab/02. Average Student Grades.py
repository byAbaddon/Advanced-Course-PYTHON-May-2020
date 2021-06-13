loop = int(input())
student_dict = {}
string = ''

for _ in range(loop):
    token = input().split()
    key, val =  token[0], float(token[1])
    if key not in student_dict:
        student_dict[key] = []
    student_dict[key].append(val)


for key, val in student_dict.items():
    for v in val:
        string += f'{v:.2f} '
    print(f'{key} -> {string}(avg: {sum(val) / len(val):.2f})')
    string = ''