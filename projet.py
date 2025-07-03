def somme (T):
    S=0
    for t in T:
        S+=t
        return S

Data = [1, 3, 5]
Som = somme(Data)
print('la somme est :', Som)