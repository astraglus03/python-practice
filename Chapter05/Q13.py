import random
res=[]
while len(res)<6:
    num=random.randint(1,45)
    if(num not in res):
        res.append(num)
print(res)