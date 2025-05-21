# Függvény, amely egy adott nap hőmérséklete alapján visszaad egy szöveges diagram-sort
def keszit_diagram_sort(nap_szama, homerseklet):
    # Átalakítja a hőmérsékletet egész számmá (ha esetleg nem lenne az)
    csillagok_szama = int(homerseklet)
    # A csillagok száma a hőmérséklettel arányos (pl. 12°C -> 12 db csillag)
    csillagok = '*' * csillagok_szama
    # Összeállítja a kiírandó sort: Nap száma, csillagok, és a konkrét hőmérséklet
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"
    return sor  # Visszatér a kész sorral

# Függvény, amely kiírja az egész heti hőmérséklet diagramját
def rajzolj_diagram(homersekletek):
    # Cím kiírása a diagramhoz
    print("Napi átlaghőmérséklet diagram (°C)")
    # Vízszintes elválasztó vonal
    print("-" * 40)

    # Végigmegy a hőmérsékletlista minden elemén (minden nap hőmérsékletén)
    for i in range(len(homersekletek)):
        nap = i + 1  # A nap számozása 1-től kezdődik (nem 0-tól)
        # Meghívja a diagram sorát előállító függvényt az adott napra
        sor = keszit_diagram_sort(nap, homersekletek[i])
        # Kiírja az adott nap diagramját
        print(sor)

# Lista, amely tartalmazza egy hét napi átlaghőmérsékleteit Celsius fokban
napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

# Meghívja a diagramrajzoló függvényt a lista alapján
rajzolj_diagram(napi_atlaghomersekletek)
