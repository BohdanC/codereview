"""
Вивести усі слова котрі містять в слові велику букву
"""
A=input("Введіть рядок:")
slova = A.split(" ")
list=[]
slovo=0
bukwa=0
for slovo in slova:
    for bukwa in slovo:
        if (bukwa.isupper()):
            list.append(slovo)
            break
print(list)