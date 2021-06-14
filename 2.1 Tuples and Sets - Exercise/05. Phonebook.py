phone_dict = {}

while True:
        token = input().split('-')
        if len(token) == 2:
            name, phone = token[0], token[1]
            if name not in phone_dict:
                phone_dict[name] = ''
            phone_dict[name] = phone
        else:
            loop = int(token[0])
            for _ in range(loop):
                name = input()
                if name not in phone_dict:
                    print(f'Contact {name} does not exist.')
                else:
                    print(name, '->', phone_dict[name])
            break                
