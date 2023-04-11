"""Tee yksinkertainen Supermarket-ohjelma,

jossa kymmenen tuotteen hinnat ovat listassa seuraavasti: [10,14,22,33,44,13,22,55,66,77].

joka kysyy (input) tuotteen numeroa väliltä 1 - 10 ja laskee listasta haettavan tuotteen 
hinnan mukaan ostosten kokonaissummaan, samalla tulostaen haetun tuotteen numeron ja hinnan.

joka kysyy tuotteita kunnes käyttäjä antaa '0' lopettaakseen ohjelman (while-silmukka).

joka lopuksi tulostaa 'Yhteensä:' ostosten kokonaissumma ja pyytää käyttäjältä summan 
'Maksu:' ja tulostaa lopuksi palautettavat vaihtorahat 'Vaihto:' (maksu - summa) käyttäjälle.

Ohjelmassa on käytettävä: while, input"""

"""Ohjelmaan lisätty edellisen tehtävänannon lisäksi try/except -rakenteet käyttäjän 
virhesyötteiden poistamiseksi, sekä testi siitä onko käyttäjän antama numero 1-10 välillä. 
Lisätty myös yksinkertainen verranto joka ilmoittaa jos käyttäjällä ei ole rahaa tuotteisiin."""

prices = [10,14,22,33,44,13,22,55,66,77]
total_sum = 0

while True:
    try:
        user_input = int(input('Valitse tuote (1-10) 0 lopetus:'))
    except ValueError:
        print('Virheellinen valinta')
        continue
    
    if user_input >= 1 and user_input <= 10:
        total_sum = total_sum + prices[user_input -1]
        print(f'Tuote: {user_input} Hinta: {prices[user_input -1]}')
    elif user_input == 0:
        print(f'Yhteensä: {total_sum}')
        try:
            pay = int(input('Maksu: '))
        except ValueError:
            print('Virheellinen syöte')
            continue
        print(f'Vaihto: {pay - total_sum}')

        if pay < total_sum:
            print('Sinulla ei riitä rahat!')
        break
    else:
        print('Valinta ei käytössä')
        continue