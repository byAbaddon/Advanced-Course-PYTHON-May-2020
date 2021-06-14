text = input()
chars_dict = {}

for char in text:
    if char not in chars_dict:
        chars_dict[char] = 0
    chars_dict[char] += 1

sorted_chars_dict = dict(sorted(chars_dict.items()))

for k, v in sorted_chars_dict.items():        
    print(f'{k}: {v} time/s')