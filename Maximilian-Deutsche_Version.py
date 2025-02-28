import time
import pygame

pygame.mixer.init()

Musik = "SalmonLikeTheFish - Zion.mp3"

def Spiele_Musik():
    pygame.mixer.music.load(Musik)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)


Tageszähler = 1
Pflanzen = 0
Aktueller_Wasserverbrauch = 0
Münzen = 100
Stromgenerator_Anzahl = 1
Wassertank_Anzahl = 1
Max_Wasserverbrauch = Wassertank_Anzahl * 100
Energie_produziert = Stromgenerator_Anzahl * 50
Energie_verbraucht = 0
Heute_geerntet = 0

def Stats():
    global Heute_geerntet
    print("\n-----------------------------------------------------------------------")
    print("Deine Stats:")
    print(f"Tag ☀️:: {Tageszähler}")
    print(f"Pflanzen 🌱: {Pflanzen}")
    print(f"Wasser-Verbrauch 💧: {Aktueller_Wasserverbrauch}/{Max_Wasserverbrauch}L")
    print(f"Energie-Verbrauch ⚡: {Energie_verbraucht}/{Energie_produziert}W")
    print(f"Münzen 💰: {Münzen}")
    print(f"Heute geerntet: {Heute_geerntet} Münzen")
    Stats_Zurück = input("Um zurück zu gehen, drücke '1'.\n")
    if Stats_Zurück in ["1"]:
        Hauptmenü()

def Schlaf_Animation():
    Schlaf_Animation_Zeilen = [
        "Zzz... 🌙💤               ",
        "Zzz... 🌙💤 💤            ",
        "Zzz... 🌙💤 💤 💤         ",
        "Zzz... 🌙💤 💤 💤 💤      ",
        "Zzz... 🌙💤 💤 💤 💤 💤  ",
        "                            "
    ]
    print("\n\n\n")
    print("                            ")
    print("\n\n\n")
    for i in range(3):
        for frame in Schlaf_Animation_Zeilen:
            print(frame, end="\r\n\n\n\n")
            time.sleep(0.5)
    print("\n\n")


Schon_geerntet = False
Ertrag = 0
weizen_Anzahl = 0
Mais_Anzahl = 0
Kartoffel_Anzahl = 0
Sonnenblumen_Anzahl = 0
Apfelbaum_Anzahl = 0
Kirschbaum_Anzahl = 0
Birnenbaum_Anzahl = 0
Orangenbaum_Anzahl = 0
Erdbeerbusch_Anzahl = 0
Himbeerbusch_Anzahl = 0
Blaubeerbusch_Anzahl = 0
Schwarzbeerbusch_Anzahl = 0

Wasserverbrauch = {
    "weizen": 5,
    "mais": 10,
    "kartoffel": 50,
    "sonnenblume": 100,
    "apfelbaum": 8,
    "kirschbaum": 16,
    "birnenbaum": 32,
    "orangenbaum":64,
    "erdbeerbusch": 12,
    "himbeerbusch": 24,
    "blaubeerbusch": 48,
    "schwarzbeerbusch": 96
}
Infrastruktur_Preise = {
    "Stromgenerator": 50,
    "wassertank": 300
}

Pflanzen_Preise = {
    "weizen": 25,
    "mais": 50,
    "kartoffel": 100,
    "sonnenblume": 200,
    "apfelbaum": 40,
    "kirschbaum": 80,
    "birnenbaum": 160,
    "orangenbaum":320,
    "erdbeerbusch": 60,
    "himbeerbusch": 120,
    "blaubeerbusch": 240,
    "schwarzbeerbusch": 480
}

Ernte_Faktor = {
    "weizen": 2.5,
    "mais": 5,
    "kartoffel": 10,
    "sonnenblume": 20,
    "apfelbaum": 4,
    "kirschbaum": 8,
    "birnenbaum": 16,
    "orangenbaum": 32,
    "erdbeerbusch": 6,
    "himbeerbusch": 12,
    "blaubeerbusch": 24,
    "schwarzbeerbusch": 48
}

Freischalttag = {
    "weizen": 1,
    "mais": 20,
    "kartoffel": 40,
    "sonnenblume": 80,
    "apfelbaum": 16,
    "kirschbaum": 32,
    "birnenbaum": 64,
    "orangenbaum": 128,
    "erdbeerbusch": 24,
    "himbeerbusch": 48,
    "blaubeerbusch": 96,
    "schwarzbeerbusch": 198
}

def Feldfrucht():
    global Münzen, weizen_Anzahl, Mais_Anzahl, Kartoffel_Anzahl, Sonnenblumen_Anzahl, Ertrag, Pflanzen, Max_Wasserverbrauch, Aktueller_Wasserverbrauch, Energie_verbraucht
    
    print("\n-----------------------------------------------------------------------")
    Feldfrucht_Wahl = input(f"Welche Feldfrucht möchtest du anplanzen?\nDu hast {Münzen} Münzen\n1. Weizen 🌾 (25 Münzen)\n2. Mais 🌽 (50 Münzen)\n3. Kartoffel 🥔 (100 Münzen)\n4. Sonnenblume 🌻 (200 Münzen)\n\n").lower().strip()

    if Feldfrucht_Wahl in ["1", "weizen"]:    
        Feldfrucht_Name = "weizen"
        Feldfrucht_Anzahl = "weizen_Anzahl"
    elif Feldfrucht_Wahl in ["2", "mais"]:
        Feldfrucht_Name = "mais"
        Feldfrucht_Anzahl = "Mais_Anzahl"
    elif Feldfrucht_Wahl in ["3", "kartoffel"]:
        Feldfrucht_Name = "kartoffel"
        Feldfrucht_Anzahl = "Kartoffel_Anzahl"
    elif Feldfrucht_Wahl in ["4", "sonnenblume"]:
        Feldfrucht_Name = "sonnenblume"
        Feldfrucht_Anzahl = "Sonnenblumen_Anzahl"
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        return

    if Tageszähler < Freischalttag[Feldfrucht_Name]:
        print(f"Du musst Tag {Freischalttag[Feldfrucht_Name]} erreichen, um {Feldfrucht_Name.replace('_', ' ').capitalize()} kaufen zu können.")
        time.sleep(2)
        return
    if Max_Wasserverbrauch < Aktueller_Wasserverbrauch + Wasserverbrauch[Feldfrucht_Name]:
        print("Du hast nicht genug Wasser, um diese Pflanze pflanzen zu können..")
        time.sleep(2)
        return

    if Energie_produziert < Energie_verbraucht + 25:
        print(f"Du musst einen neuen Stromgenerator bauen, um die Wasserpumpe anzutreiben.")
        time.sleep(2)
        return

    if Münzen >= int(Pflanzen_Preise[Feldfrucht_Name]):
        Münzen -= Pflanzen_Preise[Feldfrucht_Name]
        globals()[Feldfrucht_Anzahl] += 1
        Pflanzen +=1
        Energie_verbraucht += 25
        Aktueller_Wasserverbrauch += Wasserverbrauch[Feldfrucht_Name]
        Ertrag += Ernte_Faktor[Feldfrucht_Name]
        
        print(f"Du hast 1 {Feldfrucht_Name.capitalize()} angepflanzt! 🌱 (Restliche Münzen: {Münzen})")
    else:
        print(f"Nicht genug Münzen! Du brauchst {Pflanzen_Preise[Feldfrucht_Name] - Münzen} Münzen mehr. ❌")

def Fruchtbäume():
    global Münzen, Apfelbaum_Anzahl, Kirschbaum_Anzahl, Birnenbaum_Anzahl, Orangenbaum_Anzahl, Ertrag, Pflanzen, Max_Wasserverbrauch, Aktueller_Wasserverbrauch, Energie_verbraucht
    
    print("\n-----------------------------------------------------------------------")
    Fruchtbaum_Wahl = input(f"Welchen Fruchtbaum möchtest du anpflanzen?\nDu hast {Münzen} Münzen\n1. Apfelbaum 🍏 (40 Münzen)\n2. Kirschbaum 🍒 (80 Münzen)\n3. Birnenbaum 🍐 (160 Münzen) \n4. Orangenbaum 🍊 (320 Münzen)\n\n").lower().strip()

    if Fruchtbaum_Wahl in ["1", "apfelbaum"]:   
        Fruchtbaum_Name = "apfelbaum"
        Fruchtbaum_Anzahl = "Apfelbaum_Anzahl"
    elif Fruchtbaum_Wahl in ["2", "kirschbaum"]:
        Fruchtbaum_Name = "kirschbaum"
        Fruchtbaum_Anzahl = "Kirschbaum_Anzahl"
    elif Fruchtbaum_Wahl in ["3", "birnenbaum"]:
        Fruchtbaum_Name = "birnenbaum"
        Fruchtbaum_Anzahl = "Birnenbaum_Anzahl"
    elif Fruchtbaum_Wahl in ["4", "orangenbaum"]:
            Fruchtbaum_Name = "orangenbaum"
            Fruchtbaum_Anzahl = "Orangenbaum_Anzahl"
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        return

    if Tageszähler < Freischalttag[Fruchtbaum_Name]:
        print(f"Du musst Tag {Freischalttag[Fruchtbaum_Name]} erreichen, um {Fruchtbaum_Name.replace('_', ' ').capitalize()} kaufen zu können.")
        time.sleep(2)
        return
    
    if Max_Wasserverbrauch < Aktueller_Wasserverbrauch + Wasserverbrauch[Fruchtbaum_Name]:
        print("Du hast nicht genug Wasser, um diese Pflanze pflanzen zu können.")
        time.sleep(2)
        return
    
    if Energie_produziert < Energie_verbraucht + 25:
        print(f"Du musst einen neuen Stromgenerator bauen um die Wasserpumpe anzutreiben.")
        time.sleep(2)
        return
    
    if Münzen >= Pflanzen_Preise[Fruchtbaum_Name]:
        Münzen -= Pflanzen_Preise[Fruchtbaum_Name]
        globals()[Fruchtbaum_Anzahl] += 1
        Pflanzen +=1
        Energie_verbraucht += 25
        Aktueller_Wasserverbrauch += Wasserverbrauch[Fruchtbaum_Name]
        Ertrag += Ernte_Faktor[Fruchtbaum_Name]
        print(f"Du hast 1 {Fruchtbaum_Name.replace('_', ' ').capitalize()} gepflanzt! 🌳 (Restliche Münzen: {Münzen})")
    else:
        print(f"Nicht genug Münzen! Du brauchst {Pflanzen_Preise[Fruchtbaum_Name] - Münzen} Münzen mehr. ❌")

def Beerenbusch():
    global Münzen, Erdbeerbusch_Anzahl, Himbeerbusch_Anzahl, Blaubeerbusch_Anzahl, Schwarzbeerbusch_Anzahl, Ertrag, Pflanzen, Max_Wasserverbrauch, Aktueller_Wasserverbrauch, Energie_verbraucht
    
    print("\n-----------------------------------------------------------------------")
    Beerenbusch_Wahl = input(f"Welchen Beerenbusch möchtest du anpflanzen?\nDu hast {Münzen} Münzen\n1. Erdbeerbusch 🍓 (60 Münzen)\n2. Himbeerbusch 🍇 (120 Münzen)\n3. Blaubeerbusch 🫐 (240 Münzen)\n4. Schwarzbeerbusch 🖤🍇 (480 Münzen)\n\n").lower().strip()

    if Beerenbusch_Wahl in ["1", "strawberryBusch"]:
        Busch_Name = "erdbeerbusch"
        Busch_Anzahl = "Erdbeerbusch_Anzahl"
    elif Beerenbusch_Wahl in ["2", "Himbeerbusch"]:
        Busch_Name = "himbeerbusch"
        Busch_Anzahl = "Himbeerbusch_Anzahl"
    elif Beerenbusch_Wahl in ["3", "Blaubeerbusch"]:
        Busch_Name = "blaubeerbusch"
        Busch_Anzahl = "Blaubeerbusch_Anzahl"
    elif Beerenbusch_Wahl in ["4", "Schwarzbeerbusch"]:
        Busch_Name = "schwarzbeerbusch"
        Busch_Anzahl = "Schwarzbeerbusch_Anzahl"
    else:
        print("Ungülitge Eingabe. Versuch es nochmal.")
        return

    if Tageszähler < Freischalttag[Busch_Name]:
        print(f"Du musst Tag {Freischalttag[Busch_Name]} erreichen, um {Busch_Name.replace('_', ' ').capitalize()} kaufen zu können.")
        time.sleep(2)
        return
    
    if Max_Wasserverbrauch < Aktueller_Wasserverbrauch + Wasserverbrauch[Busch_Name]:
        print("Du hast nicht genug Wasser, um diese Pflanze pflanzen zu können.")
        time.sleep(2)
        return
    
    if Energie_produziert < Energie_verbraucht + 25:
        print(f"Du musst einen neuen Stromgenerator oder eine neue Wasserpumpe bauen.")
        time.sleep(2)
        return
    
    if Münzen >= Pflanzen_Preise[Busch_Name]:
        Münzen -= Pflanzen_Preise[Busch_Name]
        globals()[Busch_Anzahl] += 1
        Pflanzen +=1
        Energie_verbraucht += 25
        Aktueller_Wasserverbrauch += Wasserverbrauch[Busch_Name]
        Ertrag += Ernte_Faktor[Busch_Name]
        print(f"Du hast 1 {Busch_Name.replace('_', ' ').capitalize()}! 🍇 (Restliche Münzen: {Münzen})") 
    else:
        print(f"Nicht genug Münzen! Du brauchst {Pflanzen_Preise[Busch_Name] - Münzen} Münzen mehr. ❌")

def Pflanzenart():
    print("\n-----------------------------------------------------------------------\nPflanzenart:")
    Pflanzenart_Wahl = input("Was möchtest du pflanzen?\n\n1. 🌾 Feldfrucht\n\n2. 🍎 Fruchtbäume\n\n3. 🍓 Beerenbüsche\n").lower().strip()
    if Pflanzenart_Wahl in ["1", "feldfrucht"]:
        Feldfrucht()
    elif Pflanzenart_Wahl in ["2", "fruchtbaum"]:
        Fruchtbäume()
    elif Pflanzenart_Wahl in ["3", "beerenbusch"]:
        Beerenbusch()

def Ernte():
    global Ertrag, Münzen, Schon_geerntet, Heute_geerntet
    if Schon_geerntet:
        print("Du hast heute schon einmal geerntet. Komm morgen wieder!")
        return
    
    
    Erntegewinn = 0
    Erntegewinn += weizen_Anzahl * Ernte_Faktor["weizen"]
    Erntegewinn += Mais_Anzahl * Ernte_Faktor["mais"]
    Erntegewinn += Kartoffel_Anzahl * Ernte_Faktor["kartoffel"]
    Erntegewinn += Sonnenblumen_Anzahl * Ernte_Faktor["sonnenblume"]
    Erntegewinn += Apfelbaum_Anzahl * Ernte_Faktor["apfelbaum"]
    Erntegewinn += Kirschbaum_Anzahl * Ernte_Faktor["kirschbaum"]
    Erntegewinn += Birnenbaum_Anzahl * Ernte_Faktor["birnenbaum"]
    Erntegewinn += Orangenbaum_Anzahl * Ernte_Faktor["orangenbaum"]
    Erntegewinn += Erdbeerbusch_Anzahl * Ernte_Faktor["erdbeerbusch"]
    Erntegewinn += Himbeerbusch_Anzahl * Ernte_Faktor["himbeerbusch"]
    Erntegewinn += Blaubeerbusch_Anzahl * Ernte_Faktor["blaubeerbusch"]
    Erntegewinn += Schwarzbeerbusch_Anzahl * Ernte_Faktor["schwarzbeerbusch"]

    gewonnene_Münzen = Erntegewinn * 20
    if gewonnene_Münzen == 0:
        print("Du kannst nichts ernten.")
        return
    
    Münzen += gewonnene_Münzen
    Heute_geerntet = gewonnene_Münzen
    
    print(f"Du hast deine Pflanzen geerntet! 🌾 Du hast heute {gewonnene_Münzen} Münzen geerntet! (Total Münzen: {Münzen})")

    Schon_geerntet = True
    
def Infrastruktur():
    global Münzen, Stromgenerator_Anzahl, Wassertank_Anzahl, Energie_produziert
    Antwort_Infrastruktur = input(f"\n\n\n\n\nWas möchtest du kaufen?\nDu hast {Münzen} Münzen.\n1. Stromgenerator (+50W), 50 Münzen⚡\n2. Wassertank(+100L), 300 Münzen💧\n\n\n").lower().strip()
    if Antwort_Infrastruktur in ["1", "Stromgenerator"]:
        Infrastruktur_Name = "Stromgenerator"
        Infrastruktur_Anzahl = "Stromgenerator_Anzahl"
    elif Antwort_Infrastruktur in ["2", "wassertank"]:
        Infrastruktur_Name = "wassertank"
        Infrastruktur_Anzahl = "Wassertank_Anzahl"
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        return

    if Münzen >= Infrastruktur_Preise[Infrastruktur_Name]:
        Münzen -= Infrastruktur_Preise[Infrastruktur_Name]
        globals()[Infrastruktur_Anzahl] += 1
        Energie_produziert = Stromgenerator_Anzahl * 50
        print(f"Du hast 1 {Infrastruktur_Name.replace('_', ' ').capitalize()} gekauft")
    else:
        print(f"Nicht genug Münzen! Du brauchst {Infrastruktur_Preise[Infrastruktur_Name] - Münzen} Münzen mehr.")

def Neuer_Tag():
    global Tageszähler, Schon_geerntet, Ertrag, Heute_geerntet
    
    Heute_geerntet = 0

    Tageszähler += 1
    
    Schon_geerntet = False
    
    print(f"Starte Tag {Tageszähler}... 🌞\n\n\n")
    time.sleep(2)
    Hauptmenü()

def Neuer_Tag_Linie():
    print("-----------------------------------------------------------------------\n\n-----------------------------------------------------------------------")

def zähle_Tage():
    print(f"\n\n\nHeute ist dein {Tageszähler}. Tag.\n\n\n-----------------------------------------------------------------------")

def Hauptmenü():
    Antwort_Hauptmenü = input("\n\n\n\n\nWas möchtest du heute tun?\n1. Stats 📜\n2. Pflanzen 🌱\n3. Infrastruktur ⚡💧\n4. Ernten 🌾\n5. Schlafen 🌙\n6. Verlassen 👋\n\n").lower().strip()
    if Antwort_Hauptmenü in ["1", "stats"]:
        Stats()
    elif Antwort_Hauptmenü in ["2", "pflanzen"]:
        Pflanzenart()
        time.sleep(3)
        Hauptmenü()
    elif Antwort_Hauptmenü in ["3", "infrastruktur"]:
        Infrastruktur()
        time.sleep(3)
        Hauptmenü()
    elif Antwort_Hauptmenü in ["4", "ernten"]:
        Ernte()
        time.sleep(3)
        Hauptmenü()
    elif Antwort_Hauptmenü in ["5", "schlafen"]:
        Schlaf_Animation()
        Neuer_Tag()
        time.sleep(3)
    elif Antwort_Hauptmenü in ["6", "verlassen", "exit"]:
        print("Tschüss, Farmer! 👋")
        pygame.mixer.music.stop()
    else:
        print("Ungültige Aktion. Versuch es nochmal!")
        time.sleep(2)
        Hauptmenü()


Spielstart = False
try:
    Antwort1 = input("Möchtest du ein neues Spiel starten?\n1. Ja\n2. Nein\n   ").strip().lower()

    if Antwort1 in ["1", "ja"]:
        print("Du hast 'Ja' ausgewählt.")
        Spielstart = True
    elif Antwort1 in ["2", "nein"]:
        print("Du hast 'Nein' ausgewählt.")
    else:
        print("Error. Versuch es nochmal.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

if Spielstart:
    Spiele_Musik()
    print("Starte neues Spiel...")
    Neuer_Tag_Linie()
    zähle_Tage()
    time.sleep(2)
    Hauptmenü()
else:
    print("Kein Spiel wurde gestartet.")
