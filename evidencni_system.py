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
    def vypis_vsechny_pojistence(self):
        for i, pojistenec in enumerate(self.pojistenci, 0):
            print(f"Index: {i}\n {pojistenec}\n")
    #Funkce, ktera prohledava seznam self.pojistenci podle zadaneho jmena a  prijmeni (staci pouze jmeno/prijmeni/cast jmena)
    def najdi_pojistence_xy(self, hledane_jmeno, hledane_prijmeni):
        nalezeni_pojistenci = []
        for pojistenec in self.pojistenci:
            if (hledane_jmeno.lower() in pojistenec.jmeno.lower()) and (hledane_prijmeni.lower() in pojistenec.prijmeni.lower()):
                nalezeni_pojistenci.append(pojistenec)

        if nalezeni_pojistenci:
            return nalezeni_pojistenci

        return f"Nikoho jmena {hledane_jmeno} a prijmeni {hledane_prijmeni} jsme nenasli!"

    #Funkce, ktera meni data o uzivateli.
    def zmen_data_pojistence(self, index_pojistence, novy_pojistenec):
        self.pojistenci[index_pojistence] = novy_pojistenec
        return f"Na indexu {index_pojistence}, jste prave prepsali pojistence:\n{novy_pojistenec}"

    #Funkce, ktera maze pojisteneho podle indexu.
    def smaz_pojistence(self, index_pojistence):
       odstraneny_pojistenec = self.pojistenci.pop(index_pojistence)
       return f"Prave jsi na indexu: {index_pojistence} smazal pojistence: \n{odstraneny_pojistenec}"
