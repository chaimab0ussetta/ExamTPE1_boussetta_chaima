
def somme (T):
    S=0
    for t in T:
        S+=t
        return S

Data = [1, 3, 5]
Som = somme(Data)
print('la somme est :', Som)
Data=[1,3,5]
if Data:
    print('la somme est:',sum(Data))
    print('le min est:',min(Data))
    print('le max est:',max(Data))
else:
    print('dossier vide')
