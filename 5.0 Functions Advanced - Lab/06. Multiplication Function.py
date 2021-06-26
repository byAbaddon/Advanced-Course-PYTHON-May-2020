from functools import reduce 

def multiply (*args):
   return reduce(lambda a, x:  a * x , args)

