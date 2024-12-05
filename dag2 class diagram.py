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

# Testen product class    
myProduct = Product(1, "Knipperlicht vloeistof", 3.95, 14.85, 1000)
print(f"Vooraad {myProduct.naam} is : {myProduct.aantal}")

myProduct.verkoop(1, 30)
print(f"Vooraad {myProduct.naam} is : {myProduct.aantal}")

myProduct.inkoop(1, 30)
print(f"Vooraad {myProduct.naam} is : {myProduct.aantal}")