# Egyetemi Rendszer

Az egyetemi rendszer egy olyan alkalmazás, amely lehetővé teszi a tanárok, diákok, kurzusok és osztályzatok kezelését egy egyetemen.

## Objektumok Leírása

### Diák
Egy diák objektum az alábbi tulajdonságokkal rendelkezik:
- Neve: A diák neve
- Diákazonosító: Azonosító, amely azonosítja a diákot a rendszerben
- Tanulmányi átlag: A diák tanulmányi átlaga

### Tanár
Egy tanár objektum az alábbi tulajdonságokkal rendelkezik:
- Neve: A tanár neve
- Munkatársi azonosító: Azonosító, amely azonosítja a tanárt a rendszerben
- Szak: A tanár szakterülete vagy szakja

### Kurzus
Egy kurzus objektum az alábbi tulajdonságokkal rendelkezik:
- Kurzuskód: Azonosító, amely azonosítja a kurzust a rendszerben
- Név: A kurzus neve
- Tanár: A kurzust oktató tanár

### Osztályzat
Egy osztályzat objektum az alábbi tulajdonságokkal rendelkezik:
- Diák: A diák, akit az osztályzat érint
- Kurzus: A kurzus, amelynek keretében az osztályzatot kapta a diák
- Érdemjegy: Az osztályzat érdemjegye

## Funkciók
Az egyetemi rendszer több funkciót kínál, köztük:
- Új diákok és tanárok hozzáadása, szerkesztése és törlése
- Új kurzusok létrehozása és szerkesztése
- Diákok kurzusokhoz való hozzáadása és eltávolítása
- Osztályzatok hozzáadása és szerkesztése

A rendszer célja, hogy hatékonyan kezelje az egyetemi közösséget és azok tanulmányi teljesítményét, valamint segítse az adminisztrációs feladatokat.

## Felhasználás
Az egyetemi rendszer könnyen integrálható egy webes vagy asztali alkalmazásba, ahol a felhasználók könnyen hozzáférhetnek az egyetemi információkhoz, regisztrálhatnak kurzusokra és megtekinthetik az osztályzataikat.

A rendszer lehetővé teszi az egyetemek számára, hogy hatékonyabban kezeljék az oktatási folyamatokat és nyomon kövessék a hallgatók teljesítményét.
