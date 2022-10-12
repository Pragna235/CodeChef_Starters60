# cook your dish here
for i in range(int(input())):
    n=int(input())
    cards=input()
    #print(cards)
    cards=cards.split()
    #print(cards)
    count=[cards.count(i) for i in cards]
    #print(count)
    #print(max(count))
    print(n-max(count))
    
    
    
    
    
    
    
    
