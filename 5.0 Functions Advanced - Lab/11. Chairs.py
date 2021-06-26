collection = []
def combination(names, loop):
    
    if len(collection) == loop:
        print(', '.join(collection))
        return

    for i in range(len(names)):
        collection.append(names[i])
        combination(names[i + 1:], loop)
        collection.pop()


combination(input().split(', '), int(input()))