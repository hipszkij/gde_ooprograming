from Teglalap import Teglalap
from Poligon import Poligon

teglalap = Teglalap(2,3)
kerulet = teglalap.kerulet()
terulet = teglalap.terulet()

print(f"A téglalap kerülete {kerulet}")
print(f"A téglalap területe {terulet}")

print(teglalap.tipus())
