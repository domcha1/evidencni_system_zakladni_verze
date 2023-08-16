#Trida pro vytvoreni instance pojisteneho.
#Uklada se do evidencni_system.py > list(self.pojistenci)
class Pojistenec:

    def __init__(self, jmeno, prijmeni, vek, mobil):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.mobil = mobil

    def __str__(self):
        return f"Jméno: {self.jmeno}, Příjmení: {self.prijmeni}\n Vek: {self.vek}\n Mobil: {self.mobil}"