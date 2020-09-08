import model

def zacetek(igra):
    return ("Začne X.")

def zahtevaj_vnos(igra):
    return (f"Na vrsti je {igra.igralec}.")

def izpis_zmage(igra):
    return (f"Zmagal je {igra.igralec}.")

def pozeni_vmesnik():
    igra = model.nova_mreza()
    while True:
        print(zacetek(igra))
        poskus = zahtevaj_vnos()
        stanje = igra.dodaj_znak(poskus)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break

pozeni_vmesnik()