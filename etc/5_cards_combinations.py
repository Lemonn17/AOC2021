import sys

my_limit = sys.getrecursionlimit()
sys.setrecursionlimit(my_limit + 10000)
print(sys.getrecursionlimit())

suits = ["Club", "Diamond"]
# suits = ["Club", "Diamond", "Heart", "Spade"]

ranks = ["A","2", "3", "4", "5","6"]
# ranks = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10","J", "Q", "K"]


# def is_straight_flush(h: Hand):
    
all_cards = list() 


for suit in suits:
    for rank in ranks:
        tuple_temp = (suit,rank)
        all_cards.append(tuple_temp)

# print(all_cards)
# print(len(all_cards[1:]))


suits = ["Club"]
#suits = ["Club", "Diamond", "Heart", "Spade"]

       
ranks = ["A" # index_1 
,"2" # index_
, "3"
, "4"
, "5"
,"6"]
list_all_hand = [] # ans 
current_hand = [] # ans for each hand
index_1 = 0
index_2 = 1
index_3 = 2
index_4 = 3
index_5 = 4
# 2 card
def all_hands(current_deck,index_1,index_2,index_3,index_4,index_5):
    
    if index_5 < len(current_deck)-1 and index_4 < len(current_deck)-2 and index_3 < len(current_deck)-3 and index_2 < len(current_deck)-4 and index_1 < len(current_deck)-5 :
        
        
        current_hand = [[current_deck[index_1],current_deck[index_2],current_deck[index_3],current_deck[index_4],current_deck[index_5]]]
        
        print('case1',index_1,index_2,index_3,index_4,index_5,current_hand)
        return current_hand + all_hands(current_deck,index_1,index_2,index_3,index_4,index_5+1)

    #5 max
    if index_5 == len(current_deck)-1 and index_4 < len(current_deck)-2 and index_3 < len(current_deck)-3 and index_2 < len(current_deck)-4 and index_1 < len(current_deck)-5 :
        
        current_hand = [[current_deck[index_1],current_deck[index_2],current_deck[index_3],current_deck[index_4],current_deck[index_5]]]
        
        print('case2',index_1,index_2,index_3,index_4,index_5,current_hand)
        index_4 = index_4 + 1
        index_5 = index_4 + 1
        return current_hand + all_hands(current_deck,index_1,index_2,index_3,index_4,index_5) 
    #4 max
    if index_5 == len(current_deck)-1 and index_4 == len(current_deck)-2 and index_3 < len(current_deck)-3 and index_2 < len(current_deck)-4 and index_1 < len(current_deck)-5 :
        current_hand = [[current_deck[index_1],current_deck[index_2],current_deck[index_3],current_deck[index_4],current_deck[index_5]]]
        
        print('case3',index_1,index_2,index_3,index_4,index_5,current_hand)

        index_3 = index_3 + 1
        index_4 = index_3 + 1
        index_5 = index_4 + 1
        return  current_hand + all_hands(current_deck,index_1,index_2,index_3,index_4,index_5)

    #3 max
    if index_5 == len(current_deck)-1 and index_4 == len(current_deck)-2 and index_3 == len(current_deck)-3 and index_2 < len(current_deck)-4 and index_1 < len(current_deck)-5 :
        current_hand = [[current_deck[index_1],current_deck[index_2],current_deck[index_3],current_deck[index_4],current_deck[index_5]]]
        
        print('case4',index_1,index_2,index_3,index_4,index_5,current_hand)
        index_2 = index_2 + 1
        index_3 = index_2 + 1
        index_4 = index_3 + 1
        index_5 = index_4 + 1
        return current_hand + all_hands(current_deck,index_1,index_2,index_3,index_4,index_5)
    #2 max
    if index_5 == len(current_deck)-1 and index_4 == len(current_deck)-2 and index_3 == len(current_deck)-3 and index_2 == len(current_deck)-4 and index_1 < len(current_deck)-5 :
        current_hand = [[current_deck[index_1],current_deck[index_2],current_deck[index_3],current_deck[index_4],current_deck[index_5]]]
        
        print('case5',index_1,index_2,index_3,index_4,index_5,current_hand)
        index_1 = index_1 + 1
        index_2 = index_1 + 1
        index_3 = index_2 + 1
        index_4 = index_3 + 1
        index_5 = index_4 + 1
        return current_hand + all_hands(current_deck,index_1,index_2,index_3,index_4,index_5)


    else:
        current_hand = [[current_deck[index_1],current_deck[index_2],current_deck[index_3],current_deck[index_4],current_deck[index_5]]]
        print('case6',index_1,index_2,index_3,index_4,index_5,current_hand)
        return current_hand
        
print('#############')
print(len(all_hands(all_cards,index_1,index_2,index_3,index_4,index_5)))
# print(all_cards) 


###################################################

###################################################
###################################################


