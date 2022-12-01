
from os import X_OK


file = open('input.txt','r')



input = []


tmp = -99999

for line in file:
    a,b = line.strip().split(' -> ')

    start =  [int(e) for e in a.split(',')]
    end = [int(e) for e in  b.split(',')]
    input.append((start,end)) 
    tmp = max([tmp]+start+end)


tmp = tmp+1

array = []

for x in range(tmp):
    array.append([])
    for y in range(tmp):
        array[x].append(0)

# print(len(array[0]))



# print(input)

# array = [
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# ,[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# ,[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# ,[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# ,[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# ,[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# ,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]


for Corr in range(len(input)):
    start_x,start_y = input[Corr][0]
    end_x,end_y = input[Corr][1]

    if start_x == end_x:
        y = min(start_y,end_y)
        while y <= max(start_y,end_y):
            array[start_x][y] +=1
            y+=1

    elif start_y == end_y:
        x = min(start_x,end_x)

        while x <= max(start_x,end_x):
            array[x][start_y] +=1
            x= x + 1
   #### ADDITIONAL STAR         
    else:
        if (start_x > end_x and start_y > end_y) or (start_x < end_x and start_y < end_y):
            start_line_x = min(start_x,end_x)
            start_line_y = min(start_y,end_y)
            end_line_x = max(start_x,end_x)
            end_line_y = max(start_y,end_y)
            
            while start_line_x <= end_line_x:
                array[start_line_x][start_line_y] +=1
                start_line_x += 1
                start_line_y += 1 

        else:
            start_line_x = min(start_x,end_x)
            start_line_y = max(start_y,end_y)
            end_line_x = max(start_x,end_x)
            end_line_y = min(start_y,end_y)
            while start_line_x <= end_line_x:
                array[start_line_x][start_line_y] +=1
                start_line_x +=1
                start_line_y -= 1


ans = 0
for i in array:
    for j in i:
        if j > 1:
            ans+= 1

print(ans)


















