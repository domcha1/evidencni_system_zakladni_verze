from evidencni_system import Evidencni_System
import asyncio

evidencni_system = Evidencni_System()

async def main():
    pokracovani = True
    while (pokracovani == True):
        print("________________________")
        print("Evidence pojistenych")
        print("________________________")
        print("Vyberte si akci:")
        print("1 - Pridat noveho pojisteneho")
        print("2 - Vypsat vsechny pojistene")
        print("3 - Vyhledat pojisteneho")
        print("4 - Smazat pojisteneho")
        print("5 - Konec")

        operace = int(input("Jakou operaci si prejete provest? Zadejte prosim operaci 1 - 5:\n"))
        match operace:
            case 1:
                print("Zadani noveho pojistence:\n")
                jmeno = input("Zadejte jmeno pojistence:\n")
                prijmeni = input("Zadejte prijmeni pojistence:\n")
                vek = input("Zadejte vek pojistence:\n")
                mobil = input("Zadejte cislo mobilniho telefonu pojistence:\n")

                evidencni_system.vytvor_pojistence(jmeno, prijmeni, vek, mobil)

                print(f"Prave jsi uspesne pridal pojisteneho:\nJmeno a prijmeni: {jmeno} {prijmeni}\nVek: {vek}\nKontakt: {mobil}")
            case 2:
                print("Vypis vsech pojistenych:\n")
                evidencni_system.vypis_vsechny_pojistence()

            case 3:
                print("Vyhledani pojistence:\n")
                hledane_jmeno_pojisteneho = input("Zadejte jmeno pojisteneho:\n")
                hledane_prijmeni_pojisteneho = input("Zadejte prijmeni pojisteneho:\n")

                nalezeni_pojistenci = evidencni_system.najdi_pojistence_xy(hledane_jmeno_pojisteneho, hledane_prijmeni_pojisteneho)

                if isinstance(nalezeni_pojistenci, list):
                    print("\nVýsledky vyhledávání:")
                    for pojistenec in nalezeni_pojistenci:
                        print(f"Jméno: {pojistenec.jmeno}, Příjmení: {pojistenec.prijmeni}, Věk: {pojistenec.vek}, Mobil: {pojistenec.mobil}")
                else:
                    print(nalezeni_pojistenci)

            case 4:
                print("Smazani pojistence:")
                index_pojistence = int(input("Zadejte index pojistence, ktereho si prejete smazat:\n"))
                print(evidencni_system.smaz_pojistence(index_pojistence))

            case 5:
                pokracovani = False
                print("Evidence bude ukoncena za 5 sekund!\nPrejeme vam krasny zbytek dne. :)")
                await asyncio.sleep(5)

if (__name__ == "__main__"):
    asyncio.run(main())