def my_split(sentence, split_list):
    """Funktio ottaa käyttäjän inputin, kierrättää sen loopin läpi kirjain kerrallaan, 
    erottaa sanat perustuen välilyönteihin ja palauttaa sen array-listana"""
    split_list = []
    word = ''
    for c in sentence:
        if c == ' ':
            split_list.append(word)
            word = ''
        else:
            word += c
    if word:
        split_list.append(word)

    return split_list
 

def my_join(item_list, separator):
    """Funktio ottaa vastaan tässä tapauksessa my_split-funktion tuottaman listan, 
    menee for-loopin läpi käyden läpi listan jokaisen erillisen alkion palauttaen
    lopulta listan merkkijonona, lisäten toisena parametrina annetun merkin jokaisen
    alkion perään pois lukien viimeiseen"""
    result = ''
    for i, item in enumerate(item_list):
        if i > 0:
            result += separator
        result += str(item)
    return result

sentence = str(input('Kirjoita lause: '))
print(my_join(my_split(sentence,' '),','))
print(my_join(my_split(sentence,' '),'\n'))