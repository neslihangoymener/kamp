class Matematik:
    def __init__(self,sayi1,sayi2):
        self.s1 = sayi1
        self.s2 = sayi2
        print("Matematik başladı(referansı oluştu)")
    def topla(self): 
        return self.s1 + self.s2
    def cikar(self):
        return self.s2 - self.s1
    def bol(self):
        return self.s1 / self.s2
    def carp(self):
        return self.s2 * self.s1

matematik = Matematik(6,7)
sonuc = matematik.carp()
print("Sonuç : " + str(sonuc))
         