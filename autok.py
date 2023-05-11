class Autok:
  def __init__(self, sor):
   oszlop = sor.split(";")
   self.ferohely = int(oszlop[0])
   self.nev = oszlop[1] 
   self.ar = int(oszlop[2]) 
   self.kategoria = oszlop[3]
print("---------------------------")
fajl = open("ipl.txt","r",encoding="utf-8")
fajl.readline()
k_lista = [Autok(sor.strip()) for sor in fajl]
print("Autók neve és áruk($):")
for auto in k_lista:
  print(auto.nev,auto.ar)
print("---------------------------")
print(f"számuk: {len(k_lista)} db")

osszeg = 0
for k in k_lista:
    osszeg = osszeg + k.ar
print(f"Az autók összértéke: {osszeg} $")
print("---------------------------")
print("1.000.000 $ feletti autók:")
for auto in k_lista:
    if auto.ar > 1000000:
        print("\t"+auto.nev)
print("---------------------------")

auto_szam = 0
for auto in k_lista:
    if auto.ar > 1000000:
        auto_szam += 1
print(f"1.000.000 $ feletti autók száma: {auto_szam} db")
print("---------------------------")
sorba = sorted(k_lista, key=lambda n: n.ar)
print(f"A legdrágább autó neve: {sorba[-1].nev}")

legdragabb = max(f.ar for f in k_lista)
for item in k_lista:
     if item.ar == legdragabb:
         print(f"a legdrágább autó ára: {item.ar}")
print("---------------------------")