file = open('input.txt','r')

gamma = ''
epsilon =''
#####0,1

bitcount= []

oxygen =  []
CO2 = []
for line in file:
    if bitcount == []:
        bitcount = [[0,0]]*len(line.strip())
    for i in range(len(line.strip())):
        bitcount[i][int(line[i])] += 1 
    oxygen.append(line.strip())
    CO2.append(line.strip())
    
#-1,0,-1
bitcount_O2 = bitcount

while len(oxygen) > 1:
    
    for i in range(len(bitcount_O2)):

        if bitcount_O2[i][0] <= bitcount_O2[i][1]:
            if len(oxygen) > 1:
                for j in range(len(oxygen)-1,-1,-1):
                    if oxygen[j][i] == '0':
                        oxygen.pop(j)

        if bitcount_O2[i][0] > bitcount_O2[i][1]:
            if len(oxygen) > 1:
                for j in range(len(oxygen)-1,-1,-1):
                    if oxygen[j][i] == '1':
                        oxygen.pop(j)


        bitcount_O2 = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        for i in oxygen:
            for j in range(len(i)):
                bitcount_O2[j][int(i[j])] += 1 


bitcount_C02 = bitcount
while len(CO2) > 1:
    
    for i in range(len(bitcount_C02)):
        
        if bitcount_C02[i][0] <= bitcount_C02[i][1]:
            if len(CO2) > 1:
                for k in range(len(CO2)-1,-1,-1):
                    if CO2[k][i] == '1':
                        CO2.pop(k)

        if bitcount_C02[i][0] > bitcount_C02[i][1]:
            if len(CO2) > 1:
                for k in range(len(CO2)-1,-1,-1):
                    if CO2[k][i] == '0':
                        CO2.pop(k)

        bitcount_C02 = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
       
        for i in CO2:
            for j in range(len(i)):
                bitcount_C02[j][int(i[j])] += 1 

print(oxygen,CO2)
print(int(oxygen[0],2),int(CO2[0],2))

print(int(oxygen[0],2)*int(CO2[0],2))

# print(int(CO2[0],2),int(oxygen[0],2))
# print(int(CO2[0],2)*int(oxygen[0],2))


# for i in bitcount:
#     if i[0] > i[1]:
#         gamma = gamma + '0'
#         epsilon = epsilon + '1'
#     else:
#         gamma = gamma + '1'
#         epsilon = epsilon + '0'



# print(gamma,epsilon)
# print(int(gamma,2),int(epsilon,2))

# print(int(gamma,2)*int(epsilon,2))

