
from os import X_OK


## initial_state >> {3: 2, 4: 1, 1: 1, 2: 1}




def calculate_grow(initial_state, days):
    new_state = {}
    if days > 0:
        for i in [1,2,3,4,5,6,7,8,0]:
            if i != 0  and initial_state.get(i):
                new_state[i-1] = initial_state[i]
            elif i == 0 and initial_state.get(i):
                temp = initial_state[i]

                if new_state.get(6):
                    new_state[6] += temp
                else:
                    new_state[6] = temp
                
                if new_state.get(8):
                    new_state[8] += temp
                else:
                    new_state[8] = temp

        # print(new_state.items() )
        # print('###########')
        return calculate_grow(new_state, days-1)
    else:
        return initial_state



def main():
    days = 256   
    initial_state = {}
    result_state = {}
    with open("input.txt") as f:
        initial_list = list(map(int, f.readline().split(',')))

    for item in initial_list:
        if initial_state.get(item):
            initial_state[item] += 1
        else:
            initial_state[item] = 1

    # print(initial_state.items())
    # print('###### --------- ######')

    result_state = calculate_grow(initial_state, days)
    print(result_state)
    qty = 0
    for key in result_state.keys():
        qty += result_state[key]
    print(qty)

if __name__ == "__main__":
    main()







