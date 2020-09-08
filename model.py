MREZA = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]

ZMAGA = "W"

def displayString(mreza):
    print(mreza[7] + '|' + mreza[8] + '|' + mreza[9])
    print(mreza[4] + '|' + mreza[5] + '|' + mreza[6])
    print(mreza[1] + '|' + mreza[2] + '|' + mreza[3])

def zmaga(mreza):
    if mreza[7] == mreza[8] == mreza[9] != " ":
        return ZMAGA
    
    if mreza[4] == mreza[5] == mreza[6] != " ":
        return ZMAGA

    if mreza[1] == mreza[2] == mreza[3] != " ":
        return ZMAGA

    if mreza[7] == mreza[4] == mreza[1] != " ":
        return ZMAGA

    if mreza[8] == mreza[5] == mreza[2] != " ":
        return ZMAGA

    if mreza[9] == mreza[6] == mreza[3] != " ":
        return ZMAGA

    if mreza[7] == mreza[5] == mreza[3] != " ":
        return ZMAGA

    if mreza[9] == mreza[5] == mreza[1] != " ":
        return ZMAGA

    else:
        return False


def dodaj_znak(mreza, celica, znak):
    if 1 <= celica <= 9 and znak in 'XO' and not zasedeno(mreza, celica):
        return True

def zasedeno(mreza, celica):
    if 1 <= celica <= 9 and celica != " ":
        return True 

def nova_mreza():
    return MREZA



