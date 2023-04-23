"""Tee funktio bubble_sort, joka käyttää kuplalajittelualgoritmia lajitellakseen käyttäjän antamat numerot 
pienimmästä suurimpaan.

Kuplalajittelu on yksinkertainen lajittelualgoritmi, joka toistuvasti vaihtaa peräkkäiset alkiot keskenään 
mikäli ne ovat väärässä järjestyksessä."""

def bubble_sort(a):
    for passed in range(len(a)-1,0,-1):
        for i in range(passed):
            if a[i] > a[i+1]:
                num = a[i]
                a[i] = a[i+1]
                a[i+1] = num
    return a

a = []
number = int(input('Anna lajiteltavien numeroiden määrä: '))
for i in range(number):
    value = int(input('Anna taulukon %d numero: ' %i))
    a.append(value)
print('Lajiteltu lista nousevassa järjestyksessä: ',bubble_sort(a))