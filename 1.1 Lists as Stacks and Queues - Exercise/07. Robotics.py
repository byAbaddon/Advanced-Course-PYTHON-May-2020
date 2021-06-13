#---------------------------------WTF------------TODO  
import datetime, sys

robot_dict = { x.split('-')[0]: int(x.split('-')[1]) for x in input().split(';')}
h, m, s = list(map(int,input().split(':')))

def time(add_sec):
    time = datetime.datetime(2020, 7, 16, h, m, s)
    new_time = time + datetime.timedelta(0, add_sec)
    return new_time.time()


sec = 0

for key in robot_dict:
    item = input()
    sec += 1
    print(f'{key} - {item} [{time(sec)}]') 


sort_robot_dict = dict(sorted(robot_dict.items(), key = lambda x: x[1]))
    
item_list = []
while True:
    item = input()
    if item == 'End':
        break
    item_list.append(item)


time = datetime.datetime(2020, 7, 16, h, m, s)    

while True:
    for key, val in  sort_robot_dict.items():
        try:
            item = item_list.pop()
            
            new_time = time + datetime.timedelta(0, sec + val)
            time = datetime.datetime(2020, 7, 16,new_time.hour, new_time.minute, new_time.second)
            sec = 0
            print(f'{key} - {item} [{new_time.time()}]')
           
        except:
            sys.exit()

   
        
        


