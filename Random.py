import random

head=0
tail=0
count=0

while (head<21) or (tail<21):
    temp=random.randint(0, 100)
    result=temp%2
    
    if(result==0):
        print("Heads")
        head+=1
        
    else:
        print("Tails")
        tail+=1
        
    if(head==21) or (tail==21):
        break 
    if(head==tail):
        print(tie)
        continue            

print("Head count is: ",head)
print("tail count is: ",tail)
if(head > tail):
    head_result=head-tail
    print("Head wond by : ",head_result)
else:
    tail_result=tail-head
    print("Tail wond by : ",tail_result)
    
    
 