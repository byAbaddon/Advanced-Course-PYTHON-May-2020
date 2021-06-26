def age_assignment(*args, **kwargs):
    info_dict = {}
    for name in args:
        info_dict[name] = kwargs[name[0:1]] 

    return info_dict    
