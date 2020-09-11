from model import *

krizci_krozci = Igra()

st_potez = 1

print(" " + "|" + " " + "|" + " ")
print("-----")
print(" " + "|" + " " + "|" + " ")
print("-----")
print(" " + "|" + " " + "|" + " ")

while True:
    if st_potez % 2 == 1:
        znak = 'X'
        print("Na vrsti je X.")
        
    else:
        znak = 'O'
        print("Na vrsti je O.")
        

    pozicija = int(input('Vpišite pozicijo : '))
    if not krizci_krozci.preveri_indeks(pozicija):
        print('Pozicija ni pravilna.')
        continue

    if not krizci_krozci.preveri_razpolozljivost(pozicija):
        print('Pozicija ni prosta.')
        continue

    krizci_krozci.dodaj_znak(pozicija, znak.upper())
    krizci_krozci.displayString()

    if krizci_krozci.zmaga():
        print('Zmaga!')
        break

    if st_potez >= 9:
        print('Igra je izenačena.')
        break

    st_potez = st_potez + 1