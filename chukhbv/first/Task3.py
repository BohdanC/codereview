"""
Порахувати суму САМЕ чисел в списку
"""
list=[1,2,555,241,7777,[],'slovo','hvatit',999129,[]]
print(list)
sum=0
for i in list:
    if isinstance(i,int):
        sum+=i
print(sum)