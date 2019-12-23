"""
Вивести з рядка всі числа та конвертувати їх з двійкової системи в 16-кову
"""
import re
s=input()
a=re.findall(r'\d+',s)

print(a)
def convert_base(num):
    alpabet =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    n=int(num)
    if n<16:
        return alpabet[n]
    else:
        return convert_base(n//16)+alpabet[n%16]

for i in a:
    c=convert_base(i)
    print(c)