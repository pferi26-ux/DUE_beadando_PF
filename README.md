README - Pámer Ferenc - XJ3HCP - DUE levelező - Nagy beadandó
----------------------------------------------------------------

-----------------------------------
A program rövid leírása:
-----------------------------------
A program gépjárművek olajcsere szervizének kilométer alapú nyilvántartására szolgál. A felhasználó gépjármű típus és tulajdonos alapján tudja nyomonkövetni melyik gépjárműnek mikor esedékes km alapon a következő szervizelése. Van lehetőség új ügyfelet felvenni, meglévőt törölni vagy módosítani.

-----------------------------------
Első futtatás előtti teendők
-----------------------------------
A program első futtatása előtt az interpreter-hez hozzá kell adni az alábbi csomagokat:
 - jsonfy
 - flask
 - requests

-----------------------------------
Program indítása
-----------------------------------
Az interpreter csomagok telepítése után a program indítása az alábbi sorrendben kell történjen:
	1. PF_app.py fájlt kell elindítani és futni hagyni (háttér localhost adatbázist ez futtatja).
	2. main.py fáj futtatásával elindul a program és megjelenik a felhasználói felület.

-----------------------------------
Program használata:
-----------------------------------
 - A program indításakor megjelenik az üdvözlő képernyő majd a nyilvántartó rendszer is elindul.
 - Első indításkor a programban nem lesznek adatok egy üres panel fog megjelenni az adatbeviteli mezőkkel és funkciógombokkal.
 - Programból kilépni a windows fejlécen lévő bezárás ikonnal lehetséges.

-----------------------------------
Program funkciók használata
-----------------------------------
 Meglévő ügyfelek adatainak listázása
 -----------------------------------
- A program indításkor automatikusan betölti, ha van már rögzített ügyfél adat.

 Új ügyfél hozzadása:
 -----------------------------------
- A program alján a "Jármű" mezőbe vegyük fel a gépjármű márkáját és típusát.
- A "Tulajdonos" mezőbe a gépjármű tulajdonosának nevét írjuk be.
- A "Következő olajcsere" mezőbe pedig a legközelebb esedékes olajcsere km értékét vegyük fel.
- Ha megadtuk a fenti adatokat akkor nyomjunk a "Hozzáadás" gombra, ezt követően a rendszer felveszi az ügyfelet.
- Sikeres felvételt követően az ügyfél automatikusan megjelenik a nyilvántartó táblázatában.

Meglévő ügyfélhez új olajcsere km megadása:
-----------------------------------
- A nyilvántartó táblázatban válasszuk ki a módosítani kívánt ügyfelet
- A "Következő olajcsere" mezőbe a legközelebb esedékes olajcsere km értékét vegyük fel (többi mezőt ne töltsük!).
- Ha megadtuk a fenti adatot akkor nyomjunk a "Módosítás" gombra, ezt követően a rendszer módosítja a km értéket.
- Sikeres módosítást követően az ügyfél adatai automatikusan módosulnak a nyilvántartó táblázatában.

Meglévő ügyfél törlése:
-----------------------------------
- A nyilvántartó táblázatban válasszuk ki a törölni kívánt ügyfelet.
- Ha kiválasztottuk az ügyfelet akkor nyomjunk a "Törlés" gombra, ezt követően a rendszer törli az ügyfelet.
- Sikeres törlést követően az ügyfél adatai automatikusan eltűnnek a nyilvántartó táblázatból.

-----------------------------------
Technikai leírás
-----------------------------------

Modulok
-----------------------------------
 - main: Fő futtató modul innen történik a felhasználói műveletek kérése és a felhasználói felület generálása.
 - PF_app: A kért műveletek adatbázisban való végrehajtását tartalmazó függvények vannak itt tárolva, localhost futtatásáért is felel.
 - PF_database: Adatbázi kapcsolat létrehozásáért felelős, ha még nem létezik akkor új adatbázis generálását is elvégzi.
 - PF_back: Adat átadás és összekötést biztosítja a main.py és a PF_app.py modul között.
 - PF_logo_draw: A program indításakori üdvözlő képernyő/logo rajzolását végzi turtle modul segítségével.

Függvények
-----------------------------------
 - pf_list_intervals: Lekéri az adatbázisban szereplő értékeket.
 - pf_load_intervals: Betölti a táblázatba a pf_list_intervals által lekért elemeket.
 - pf_add_interval: A megadott adatokkal az új ügyfelet felveszi az adatbázisba.
 - pf_mod_interval: A kiválasztott ügyfél id-nál módosítja az adatbáziban szereplő km értékét az újonnan megadottra.
 - pf_delete_interval: A kiválasztott ügyvél id összes adatát törli.
 - init_db: Adatbázis létrehozása.
 - get_connection: Adatbázis kapcsolat létrehozása.
 - pf_draw_logo: A program indításakor megjelenő üdvözlő képernyő rajzolása.
