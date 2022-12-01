
import statistics



def sum_1_to_n(n):
    return n*(n+1)/2


def cal_feul(initial_list,med):
    temp = 0
    for item in initial_list:
        temp += abs(item-med)
    return temp

def cal_feul_2(initial_list,avg):
    temp = 0
    for item in initial_list:
        temp += sum_1_to_n(abs(item-avg))
    return temp

def main():
    mapping_y = {}
    with open("input.txt") as f:
        initial_list = list(map(int, f.readline().split(',')))
    
    med = statistics.median(initial_list)
    avg = sum(initial_list)//len(initial_list)
    print(med,avg)
    for item in initial_list:
        if mapping_y.get(item):
            mapping_y[item] += 1
        else:
            mapping_y[item] = 1

    print(cal_feul(initial_list,med))
    print(cal_feul_2(initial_list,avg))

if __name__ == "__main__":
    main()

