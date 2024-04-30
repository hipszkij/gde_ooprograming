# Egységbezárás Pythonban

Az egységbezárás (encapsulation) olyan programozási elv, amely lehetővé teszi az osztályok adattagjainak és metódusainak elrejtését és védelmét a külvilágtól. A Pythonban nincs szigorú privát vagy publikus tagok megkülönböztetése, mint más nyelvekben, de a következő módszerekkel lehet megvalósítani az egységbezárás elvét:

1. **Attribútumok kezdő aláhúzással (_)**: Az attribútumokat, amelyeket az osztályon kívül nem kell hozzáférni, kezdő aláhúzással (`_`) lehet kezdeni. Ez jelzi más fejlesztőknek, hogy ezek az attribútumok belső használatra vannak fenntartva, és nem kell közvetlenül hozzáférni hozzájuk.

2. **Property függvények**: A property függvények lehetővé teszik az attribútumok olvasását, írását és törlését, miközben a belső logika megvalósításától függetleníthetjük az attribútumot.

3. **Metódusok privát jelöléssel**: Az osztályon belüli metódusokat lehet priváttá tenni azáltal, hogy az elnevezésüket két aláhúzással (`__`) kezdjük. Ez azt jelzi, hogy ezek a metódusok belső működéshez kellenek, és nem kell közvetlenül hozzáférni hozzájuk kívülről.

Példa kód:

```python
class Car:
    def __init__(self, make, model):
        self._make = make  # _make attribútum, belső használatra
        self._model = model  # _model attribútum, belső használatra

    def get_make(self):
        return self._make

    def set_make(self, make):
        if make:
            self._make = make

    def _internal_method(self):
        # belső működés
        pass

# Példa használat:
car = Car("Toyota", "Corolla")
print(car.get_make())  # külső hozzáférés a make attribútumhoz
car.set_make("Ford")  # külső hozzáférés a make attribútumhoz
car._internal_method()  # belső metódus hívása
