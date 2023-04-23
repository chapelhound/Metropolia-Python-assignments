"""Määrittele aluksi luokka Employee ja sen alustus-metodi. Employee -luokalla on kaksi
attribuuttia: id ja name.

Tee ohjelma,

    - joka lisää listaan Employee-luokan olioita. Id on laskennallinen järjestysnumero alkaen 
    luvusta 1 ja name (nimi) kysytään käyttäjältä. 
    - jonka suoritus lopetetaan käyttäjän antaessa nimen sijasta '0'.
    - joka lopussa tulostaa listan sisällön alla olevan esimerkin mukaisesti.

Ohjelmassa on käytettävä: class, def, for"""

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

employees = []
i = 1

while True:
    name = input("Anna työntekijän nimi (0 lopetus): ")
    if name == "0":
        break
    employee = Employee(i, name)
    employees.append(employee)
    i += 1

for employee in employees:
    print(f"Id: {employee.id} Nimi: {employee.name}")