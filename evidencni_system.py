from pojistenec import Pojistenec
#Trida evidencniho systemu, jsou v ni funkce, ktere pracuji s instancemi pojistence.
class Evidencni_System:
#Konstruktor tridy Evidencni_System
    def __init__(self):
        self.pojistenci = []
#Funkce vytvarejici noveho pojistence do seznamu self.pojistenci
    def vytvor_pojistence(self, jmeno, prijmeni, vek, mobil):
        pojistenec = Pojistenec(jmeno, prijmeni, vek, mobil)
        self.pojistenci.append(pojistenec)
# Funkce vypisujici vsechny ulozene pojistence ze seznamu self.pojistenci
    def vypis_pojistence(self):
        for i, pojistenec in enumerate(self.pojistenci, 0):
            print(f"Index: {i}\n {pojistenec}")
            print()
#Funkce, ktera prohledava seznam self.pojistenci podle zadaneho jmena a  prijmeni (staci pouze jmeno/prijmeni/cast jmena)
    def najdi_pojistence_xy(self, hledane_jmeno, hledane_prijmeni):
        nalezeni_pojistenci = []
        for pojistenec in self.pojistenci:
            if (hledane_jmeno.lower() in pojistenec.jmeno.lower()) and (hledane_prijmeni.lower() in pojistenec.prijmeni.lower()):
                nalezeni_pojistenci.append(pojistenec)

        if nalezeni_pojistenci:
            return nalezeni_pojistenci

        return f"Nikoho jmena {hledane_jmeno} a prijmeni {hledane_prijmeni} jsme nenasli!"