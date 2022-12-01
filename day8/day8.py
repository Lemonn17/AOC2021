
#  aaaa 
# b    c
# b    c
#  dddd 
# e    f
# e    f
#  gggg 


# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf


def part1(data):
    ans = 0
    for item in data:
        digits = item[1].strip().split(' ')
        for i in digits:
            if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
                ans += 1
    return ans

def part2(data):
    temp  = 0
    for item in data:
        digits = item[0].strip().split(' ')
        dict = {}
        list_6 = []
        list_5 = []
        for i in digits:
            if len(i) == 2 : 
                dict[1] =  ''.join(sorted([e for e in i]))
            elif len(i) == 4 : 
                dict[4] =  ''.join(sorted([e for e in i]))
            elif len(i) == 3 : 
                dict[7] =  ''.join(sorted([e for e in i]))
            elif len(i) == 7 : 
                dict[8] =  ''.join(sorted([e for e in i]))
            else:  
                if len(i) == 6 : 
                    list_6.append( ''.join(sorted([e for e in i])))
                if len(i) == 5 : 
                    list_5.append( ''.join(sorted([e for e in i])))

        temp_7 = set(dict[7])
        temp_4 = set(dict[4])

        for i in list_5:
            temp_set = set(i)
            if len(temp_set-temp_7) == 2 :
                dict[3] = i
            elif len(temp_set-temp_4) == 3:
                dict[2] = i
            else:
                dict[5] = i
           
        temp_5 = set(dict[5])
        temp_3 = set(dict[3])
        for i in list_6:
            temp_set = set(i)
            if len(temp_set-temp_3) == 1 :
                dict[9] = i
            elif len(temp_set-temp_5) == 1 :
                dict[6] = i
            else:
                dict[0] = i
        # print(dict)

        output = item[1].strip().split(' ')

        ans = ''
        for i in output:
            for key,value in dict.items():
                if len(set(i) - set(value)) == 0 and len(set(value) - set(i) )  == 0:
                    ans += str(key)
                    # print(i,value)
        # print(item[1],' : ',ans)

        temp += int(ans)
    return temp



def main():
    data = []
    

    with open("input.txt") as f:
        for line in f:
            i,j = line.strip().split(' | ')
            data.append((i,j))
    # print(data)
    

    print(f'Part 1 : {part1(data)}')
    print(f'Part 2 : {part2(data)}')



if __name__ == "__main__":
    main()



