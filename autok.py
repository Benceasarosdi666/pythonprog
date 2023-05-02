class Autok:
  def __init__(self, sor):
   oszlop = sor.split(";")
   self.ferohely = int(oszlop[0])
   self.nev = oszlop[1] 
   self.ar = int(oszlop[2]) 
   self.kategoria = oszlop[3]

fajl = open("ipl.txt","r",encoding="utf-8")
fajl.readline()
k_lista = [Autok(sor.strip()) for sor in fajl]

print(f"számuk: {len(k_lista)} db")

osszeg = 0
for k in k_lista:
    osszeg = osszeg + k.ar
print(f"Az autók száma: {osszeg} Ft")