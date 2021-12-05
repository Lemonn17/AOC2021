import re
import ast


file = open('input.txt','r')

# 2 8 14

board = dict()
count = 0

board_temp = []


for line in file:
    if count == 0:
        numbers = [e for e in line.strip().split(',')]
    elif len(board_temp) == 5:
        board[str(board_temp)] = [([0]*5) for i in range(5)]
        board_temp = []

    elif line.strip() != '':
        board_temp.append([e for e in re.sub(r"\s{2,}",' ',line.strip()).split(' ')])
        #print(board_temp)


    count = 1

def score(key_list,value_list,index):
    score_value_temp = 0
    for row in range(len(value_list[index])):
        for column in range(len(value_list[index][row])):
            if value_list[index][row][column] == 0:
                score_value_temp += int(key_list[index][row][column])
    return score_value_temp


key_list = []

for key in board.keys():
    key_list.append(ast.literal_eval(key))


value_list = list(board.values())


score_value = 0

#winorder = number_index : (score,order)
win_order = {}
order = 0
for number_index in range(len(numbers)):
    # if score_value == 0:
    for key_index in range(len(key_list)):
        for row_index in range(len(key_list[key_index])):
            for column_index in range(len(key_list[key_index][row_index])):
                #hit
                if int(numbers[number_index]) == int(key_list[key_index][row_index][column_index]) and key_index not in win_order.keys() :
                    value_list[key_index][row_index][column_index] = 1

    #check bingo
    for value_index in range(len(value_list)):
        
        for row_index in range(len(value_list[value_index])):
            
            if value_list[value_index][row_index] == [1,1,1,1,1] and value_index not in win_order.keys() :
                # print('################',value_list[value_index][row_index],value_index)
                # print('row bingo')
                score_value = int(score(key_list,value_list,value_index)) * int(numbers[number_index])
                win_order[value_index] = (score_value,order,int(numbers[number_index]))
                order += 1
            
            column =[]
            for temp in range(5):
                
                column.append(value_list[value_index][temp][row_index])

                if column == [1,1,1,1,1] and value_index not in win_order.keys() :
                    # print('column bingo')
                    # print('################',value_list[value_index][row_index],value_index)
                    score_value = int(score(key_list,value_list,value_index)) * int(numbers[number_index])
                    win_order[value_index] = (score_value,order,int(numbers[number_index]))
                    order += 1


print(win_order)
