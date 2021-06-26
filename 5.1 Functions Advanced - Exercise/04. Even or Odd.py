def even_odd(*args):
    command = args[-1]
    if command == 'even':
       return list(filter(lambda x: not int(x) & 1, args[0:-1] ))
    else:
        return list(filter(lambda x: int(x) & 1, args[0:-1]))

