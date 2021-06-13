import sys

cups = [int(x) for x in input().split()]
bottles = list(reversed([int(x) for x in input().split()]))

water = 0

while True:
    for i in range(10):
        try:
            if cups[i] <= bottles[i]:
                if cups[i] < bottles[i]:
                    water += abs(cups[i] - bottles[i])
                    cups.pop(i)
                    bottles.pop(i)
                    break
                else:    
                    cups.pop(i)
                    bottles.pop(i)
                    break

            elif cups[i] > bottles[i]:
                cups[i] -= bottles[i]
                bottles.pop(i)
                break
        except:
            if cups:
                print('Cups:', *cups)
            else:    
                print('Bottles:', *bottles)

            print(f'Wasted litters of water: {water}')
            sys.exit() 