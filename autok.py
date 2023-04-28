class Autok:
    def def __init__(self, Ferohely, Nev, ar, Kategoria):
      oszlop = sor.strip().split(";")  
      self.Ferohely = int(oszlop[0])
      self.Nev = oszlop[1] 
      self.ar = int(oszlop[2]) 
      self.Kategoria = oszlop[3] 
fajl = open("ipl.txt","r",encoding="utf-8")

