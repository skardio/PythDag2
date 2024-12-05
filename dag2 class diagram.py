#class Vestiging

class Vestiging:
    def __init__(self, vestigingsnr, adres, manager, werknemers=[], products=[]):
        self.vestigingsnr   = vestigingsnr
        self.adres          = adres
        self.manager        = manager
        self.products       = products
        self.werknemers     = werknemers
    
    def wijzigManager(self, nr):
        if self.manager != nr:
            self.manager = nr
    
    def nieuweMdwrkr(self, nr):
        self.werknemers.append(nr)    

    def vertrekMdwrkr(self, nr):
        for werknr in self.werknemers:
            if werknr.nr == nr:
                self.werknemers.remove(nr)

    
    def nieuw_in_assortiment(self, pnr):
        self.products.append(pnr)
    
    def verwijder_uit_assortiment(self, pnr):
        for product in self.products:
            if product.pnr == pnr:
                self.products.remove(pnr)
                break

class Product:
    def __init__(self, pnr, naam, kostprijs, verkoopprijs, aantal):
        self.pnr            = pnr
        self.naam           = naam
        self.kostprijs      = kostprijs
        self.verkoopprijs   = verkoopprijs
        self.aantal         = aantal
    
    def inkoop(self, pnr, aantal):
        self.aantal += aantal
    
    def verkoop(self, pnr, aantal):
        self.aantal -= aantal

#testen vestiging class
myVestiging = Vestiging(1, "Apeldoorn", "Baas")
myVestiging.nieuweMdwrkr(1)
myVestiging.nieuweMdwrkr(2)

for medewerkers in myVestiging.werknemers:
    print(f"Medewerker: {medewerkers}")

class Warenhuis:
    def __init__(self, naam, manager):
        self.naam = naam
        self.manager = manager

    def wijzigNaam(self, naam):
        print(f"Warenhuisnaam gewijzigd naar {naam}.")
        self.naam = naam

    def wijzigManager(self, manager):
        print(f"Warenhuis heeft een neiwe manager: {manager}.")
        self.manager = manager


class Werknemer:
    def __init__(self, nr, naam, salaris, standplaats, functie, adres):
        self.nr = nr
        self.naam = naam
        self.salaris = salaris
        self.standplaats = standplaats
        self.functie = functie
        self.adres = adres

    def uitdienst(self, nr):
        print(f"Werknemer {nr} is uit dienst.")

    def indienst(self, naam, salaris, standplaats, functie, adres):
        print(f"Nieuwe werknemer {naam} aangenomen met functie {functie} op {standplaats}.")

    def verhuizing(self, nr, adres):
        print(f"Werknemer {nr} heeft een neiwe adres {adres}.")
        self.adres = adres

    def salarismutatie(self, nr, salaris):
        print(f"Salaris van werknemer {nr} is nu {salaris}.")
        self.salaris = salaris

# Testen product class    
myProduct = Product(1, "Knipperlicht vloeistof", 3.95, 14.85, 1000)
print(f"Vooraad {myProduct.naam} is : {myProduct.aantal}")

myProduct.verkoop(1, 30)
print(f"Vooraad {myProduct.naam} is : {myProduct.aantal}")

myProduct.inkoop(1, 30)
print(f"Vooraad {myProduct.naam} is : {myProduct.aantal}")

warenhuis = Warenhuis("Blokker","Manager A")

warenhuis.wijzigNaam("Blokker 2.0")
warenhuis.wijzigManager("The manager")


werknemer = Werknemer(1, "Jan Jan", 3500, "Amsterdam", "functie A", "Prinsengracht 1 Adam")
werknemer.indienst("Jan Jan2", 3000, "Rotterdam", "Developer", "Prinsengracht 12 Adam")
