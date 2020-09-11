class Igra:
    mreza = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]  

    def displayString(self):
        print(self.mreza[6] + '|' + self.mreza[7] + '|' + self.mreza[8])
        print(self.mreza[3] + '|' + self.mreza[4] + '|' + self.mreza[5])
        print(self.mreza[0] + '|' + self.mreza[1] + '|' + self.mreza[2])

    def dodaj_znak(self, indeks, znak):
        indeks = indeks - 1
        if 0 <= indeks <= 8 and self.mreza[indeks] == " ":
            self.mreza[indeks] = znak

    def zmaga(self):
        if self.mreza[6] == self.mreza[7] == self.mreza[8] != " ":
            return True
        elif self.mreza[3] == self.mreza[4] == self.mreza[5] != " ":
            return True
        elif self.mreza[0] == self.mreza[1] == self.mreza[2] != " ":
            return True
        elif self.mreza[6] == self.mreza[3] == self.mreza[0] != " ":
            return True
        elif self.mreza[7] == self.mreza[4] == self.mreza[1] != " ":
            return True
        elif self.mreza[8] == self.mreza[5] == self.mreza[2] != " ":
            return True
        elif self.mreza[6] == self.mreza[4] == self.mreza[2] != " ":
            return True
        elif self.mreza[8] == self.mreza[4] == self.mreza[0] != " ":
            return True
        else:
            return False

    def preveri_indeks(self, indeks):
        indeks = indeks - 1
        if 0 <= indeks <= 8:
            return True
        else:
            return False

    def preveri_razpolozljivost(self, indeks):
        indeks = indeks - 1
        if self.mreza[indeks] == " ":
            return True
        else:
            return False

