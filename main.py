import time
import pygame #nur für Musik
import random

class Lager:
    def __init__(self, Anzahl, Verkaufswert):
        self.Anzahl = Anzahl
        self.Verkaufswert = Verkaufswert

Lager_Dictionary = {
    "Weizen": Lager(0, 15),
    "Mais": Lager(0, 30),
    "Kartoffel": Lager(0, 40),
    "Sonnenblume": Lager(0, 50),
    "Apfel": Lager(0, 40),
    "Kirsche": Lager(0, 50),
    "Birne": Lager(0, 60),
    "Orange": Lager(0, 70),
    "Erdbeere": Lager(0, 60),
    "Himbeere": Lager(0, 70),
    "Blaubeere": Lager(0, 80),
    "Schwarzbeere": Lager(0, 90),
    "Eier": Lager(0, 20),
    "Kuhmilch": Lager(0, 40),
    "Wolle": Lager(0, 400),
    "Schafsmilch": Lager(0, 40),
    "Ziegenmilch": Lager(0, 40),
    "Honig": Lager(0, 130),
    
    "Mehl": Lager(0, 30),
    "Tierfutter": Lager(0, 40),
    "Zucker": Lager(0, 900),
    "Rahmkäse": Lager(0, 70),
    "Ziegenkäse": Lager(0, 70),
    "Schafskäse": Lager(0, 70),
    "Käseküchlein": Lager(0, 90),
    "Honigkuchen": Lager(0, 180),
    "Apfelkuchen": Lager(0, 140),
    "Birnenkuchen": Lager(0, 160),
    "Kirschenkuchen": Lager(0, 150),
    "Erdbeermarmelade": Lager(0, 160),
    "Himbeermarmelade": Lager(0, 170),
    "Blaubeerkuchen": Lager(0, 180),
    "Schwarzbeerkuchen": Lager(0, 190),
    "Kartoffelgratin": Lager(0, 130),
    "Pommes": Lager(0, 150),
    "Stoff": Lager(0, 170),
    "Fruchtsalat": Lager(0, 240),
    "Joghurt": Lager(0, 210),
    "Orangensaft": Lager(0, 160),
    }

Lager_Feld = ["Weizen", "Mais", "Kartoffel", "Sonnenblume"]
Lager_Baum = ["Apfel", "Kirsche", "Birne", "Orange"]
Lager_Busch = ["Erdbeere", "Himbeere", "Blaubeere", "Schwarzbeere"]
Lager_Tier = ["Eier", "Kuhmilch", "Wolle", "Schafsmilch", "Ziegenmilch", "Honig"]
Lager_Produkte = ["Mehl", "Tierfutter", "Pommes", "Fruchtsalat", "Joghurt", "Stoff", "Zucker", "Rahmkäse", "Ziegenkäse", "Schafskäse", "Käseküchlein", "Honigkuchen", "Apfelkuchen", "Birnenkuchen", "Kirschenkuchen", "Erdbeermarmelade", "Himbeermarmelade", "Blaubeerkuchen", "Schwarzbeerkuchen", "Kartoffelgratin", "Orangensaft"]

class Arbeiter():
    def __init__(self,name, Lohn, Boost, Anzahl, Wert):
        self.name = name
        self.Lohn = Lohn
        self.Boost = Boost
        self.Anzahl = Anzahl
        self.Wert = Wert
    @property
    def Preis(self):
        return round(self.Lohn * (self.Anzahl + 1) ** 1.5)

Arbeiter_Dictionary = {
"Tierarzt" : Arbeiter("tierarzt", 600, 0.5, 0, 2000),
"Gärtner" : Arbeiter("gärtner", 500, 0.5, 0, 2000),
"Touristenführer" : Arbeiter("touristenführer", 800, 1.5, 0, 2000),
"Imker" : Arbeiter("imker", 700, 0.5, 0, 2000),
}


class Pflanzen:
    def __init__(self, Anzahl, Wasserverbrauch, Wert, Ernte_Faktor, Produkt):
        
        self.Anzahl = Anzahl
        self.Wasserverbrauch = Wasserverbrauch
        self.Wert = Wert
        self.Ernte_Faktor = Ernte_Faktor
        self.Produkt = Produkt
    
    @property
    def Preis(self):
        return round(self.Wert * (self.Anzahl + 1) ** 1.5)


Pflanzen_Dictionary = {
    "weizen": Pflanzen(0, 5, 250, 2, "Weizen"),
    "mais": Pflanzen(0, 10, 580, 5, "Mais"),
    "kartoffel": Pflanzen(0, 20, 1100, 10, "Kartoffel"),
    "sonnenblume": Pflanzen(0, 40, 1900, 20, "Sonnenblume"),
    "apfelbaum": Pflanzen(0, 8, 300, 4, "Apfel"),
    "kirschbaum": Pflanzen(0, 16, 800, 9, "Kirsche"),
    "birnenbaum": Pflanzen(0, 32, 1700, 18, "Birne"),
    "orangenbaum": Pflanzen(0, 64, 3100, 27, "Orange"),
    "erdbeerbusch": Pflanzen(0, 12, 600, 6, "Erdbeere"),
    "himbeerbusch": Pflanzen(0, 24, 1400, 15, "Himbeere"),
    "blaubeerbusch": Pflanzen(0, 48, 2600, 31, "Blaubeere"),
    "schwarzbeerbusch": Pflanzen(0, 96, 4500, 55, "Schwarzbeere"),
}



class Tiere:
    def __init__(self, Anzahl, Wasserverbrauch, Tierfutter, Wert, Ernte_Faktor, Produkt):
        self.Anzahl = Anzahl
        self.Wasserverbrauch = Wasserverbrauch
        self.Tierfutter = Tierfutter
        self.Wert = Wert
        self.Ernte_Faktor = Ernte_Faktor
        self.Produkt = Produkt
        
    @property
    def Preis(self):
        return round(self.Wert * (self.Anzahl + 1) ** 1.5)


Tier_Dictionary = {
    "Huhn": Tiere(0, 5, 2, 100, 6, "Eier"),
    "Kuh": Tiere(0, 10, 5, 600, 5, "Kuhmilch"),
    "Schaf": Tiere(0, 20, 10, 1100, 3, ["Wolle", "Schafsmilch"]),
    "Ziege": Tiere(0, 40, 20, 1800, 4, "Ziegenmilch"),
    "Biene": Tiere(0, 5, 2, 500, 1, "Honig")
}





Wochenzähler = 1

Pflanzen_Anzahl = 0
Tier_Anzahl = 0
Arbeiter_Anzahl = 0

class Infrastruktur:
    def __init__(self,name, Anzahl, Wert, Leistung):
        self.Anzahl = Anzahl
        self.Wert = Wert
        self.Leistung = Leistung
        self.name = name
    @property
    def Preis(self):
        return round(self.Wert * (self.Anzahl + 1) ** 1.5)

Infrastruktur_Dictionary = {
    "Stromgenerator": Infrastruktur("Stromgenerator",1,100, 50),
    "Wassertank": Infrastruktur("Wassertank",1, 300, 100)
}
Wasser = 100
Aktueller_Wasserverbrauch = 0
Wasserproduktion = Infrastruktur_Dictionary["Wassertank"].Anzahl * Infrastruktur_Dictionary["Wassertank"].Leistung

Energieproduktion = Infrastruktur_Dictionary["Stromgenerator"].Anzahl * Infrastruktur_Dictionary["Stromgenerator"].Leistung
Energie_verbraucht = 0

Heute_geerntet = 0

Münzen = 1000
Insgesamt_Verdient = 0

class Weather:
    def __init__(self, name, events, WW, FaktorT, FaktorP):
        self.name = name
        self.events = events
        self.WW = WW
        self.FaktorT = FaktorT
        self.FaktorP = FaktorP


Sonne = Weather("Sonne ☀️", [], 0.35, 1.2, 1)
Regen = Weather("Regen 🌦️", ["Heftiger Regen 🌧️"], 0.2, 0.8, 1.2)
Wolken = Weather("Wolken ☁️", ["Donner 🌩️", "Blitz ⚡"], 0.3, 1, 1)
Wind = Weather("Wind 🌪️", ["Sturm ⛈️"], 0.1, 0.9, 0.9)
Nebel = Weather("Nebel 🌫️", [], 0.05, 0.8, 1.1)



Aktueller_Wasserverbrauch = 0
WetterPflanze_Faktor = 1.0
WetterTier_Faktor = 1.0

def zufalls_event_auswahl(events):
    if not events:
        return None
    try:
        return random.choices(events, weights=[1] * len(events), k=1)[0]
    except IndexError:
        return None

def wetter_wechsel():
    global Aktueller_Wasserverbrauch, WetterTier_Faktor, WetterPflanze_Faktor, NW, PrintPflanzenFaktor, PrintTierFaktor

    WetterPflanze_Faktor = 1.0
    WetterTier_Faktor = 1.0
    weathers = [Sonne, Regen, Wolken, Wind, Nebel]
    weights = [weather.WW for weather in weathers]
    NW = random.choices(weathers, weights=weights, k=1)[0]
    FaktorT = NW.FaktorT
    FaktorP = NW.FaktorP

    print(f"\n📡 Wetter für diese Woche: {NW.name}")

    if NW.name == "Sonne ☀️":
        print("Es ist sonnig!☀️")
        Aktueller_Wasserverbrauch *= 1.2
        WetterPflanze_Faktor *= FaktorP
        WetterTier_Faktor *= FaktorT

    elif NW.name == "Regen 🌦️":
        print("Es regnet!🌦️")
        Aktueller_Wasserverbrauch *= 0.8
        Event = zufalls_event_auswahl(NW.events)
        WetterPflanze_Faktor *= FaktorP    
        WetterTier_Faktor *= FaktorT    
        if Event == "Heftiger_Regen 🌧️":
            print("Es gibt heftigen Regen!🌧️")
            Aktueller_Wasserverbrauch *= 0.9
            WetterPflanze_Faktor *= 0.7
            WetterTier_Faktor *= 0.8

    elif NW.name == "Wolken ☁️":
        print("Es ist bewölkt!☁️")
        Event = zufalls_event_auswahl(NW.events)
        WetterPflanze_Faktor *= FaktorP
        WetterTier_Faktor *= FaktorT
        if Event == "Donner 🌩️":
            print("Es gibt Donner!🌩️")
            Aktueller_Wasserverbrauch *= 0.9
            WetterPflanze_Faktor *= 0.9
            WetterTier_Faktor *= 0.8
        if Event == "Blitz ⚡":
            print("Es blitzt! ⚡")
            Aktueller_Wasserverbrauch *= 0.9
            WetterPflanze_Faktor *= 0.9
            WetterTier_Faktor *= 0.8

    elif NW.name == "Wind 🌪️":
        print("Es ist windig!🌪️")
        Event = zufalls_event_auswahl(NW.events)
        WetterPflanze_Faktor *= FaktorP
        WetterTier_Faktor *= FaktorT
        if Event == "Sturm ⛈️":
            print("Es gibt einen Sturm!⛈️")
            Aktueller_Wasserverbrauch *= 0.5
            WetterPflanze_Faktor *= 0.95
            WetterTier_Faktor *= 0.9

    elif NW.name == "Nebel 🌫️":
        print("Es ist neblig!🌫️")
        Aktueller_Wasserverbrauch *= 0.8
        WetterPflanze_Faktor *= FaktorP
        WetterTier_Faktor *= FaktorT

    if WetterPflanze_Faktor < 1.0:
        print(f"Pflanzen Ertrag: -{round((1 - WetterPflanze_Faktor) * 100, 1)}%")
        PrintPflanzenFaktor = f"-{round((1 - WetterPflanze_Faktor) * 100, 1)}%"
    else:
        print(f"Pflanzen Ertrag: +{round((WetterPflanze_Faktor - 1) * 100, 1)}%")
        PrintPflanzenFaktor = f"+{round((WetterPflanze_Faktor - 1) * 100, 1)}%"
    
    if WetterTier_Faktor < 1.0:
        print(f"Tiere Ertrag: -{round((1 - WetterTier_Faktor) * 100, 1)}%")
        PrintTierFaktor = f"-{round((1 - WetterTier_Faktor) * 100, 1)}%"
    else:
        print(f"Tiere Ertrag: +{round((WetterTier_Faktor - 1) * 100, 1)}%")
        PrintTierFaktor = f"+{round((WetterTier_Faktor - 1) * 100, 1)}%"


pygame.mixer.init()

Musik = "SalmonLikeTheFish - Zion.mp3"

def Spiele_Musik():
    pygame.mixer.music.load(Musik)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)




class TierfutterClass:
    def __init__(self, Anzahl, Verbrauch, Produktion):
        self.Anzahl = Anzahl
        self.Verbrauch = Verbrauch
        self.Produktion = Produktion


Tierfutter_Dictionary = {
    "Tierfutter": TierfutterClass(0, 0, 0),
}



def Stats():
    global Heute_geerntet, Pflanzen_Dictionary, Münzen, Energie_verbraucht, Energieproduktion, Arbeiter_Anzahl, Aktueller_Wasserverbrauch, Wasserproduktion, Wochenzähler, Insgesamt_Verdient, Pflanzen_Anzahl, Tier_Anzahl
    print("\n-----------------------------------------------------------------------")
    print("Deine Stats:")
    print(f"Woche ☀️:: {Wochenzähler}")
    print(f"Pflanzen 🌱: {Pflanzen_Anzahl}")
    print(f"Tiere 🐄: {Tier_Anzahl}")
    print(f"Wasser 💧: {Arbeiter_Anzahl}L")
    print(f"Münzen 💰: {Münzen}")
    print(f"Insgesamt verdient: {Insgesamt_Verdient} Münzen")
    Stats_Option = input("Um zurück zu gehen, drücke 'Entertaste'.\n")
    if Stats_Option in ["2",]:
        print("\n\n\n\n")      
        for name, pflanze in Pflanzen_Dictionary.items():
            print(f"{name}: {pflanze.Anzahl}")
        Stats_Zurück = input("Um zurück zu gehen, drücke 'Entertaste'.\n")
        if Stats_Zurück in [""]:
            Hauptmenü()
    elif Stats_Option in ["3"]:
        print("\n\n\n\n")
        for name, tier in Tier_Dictionary.items():
            print(f"{name}: {tier.Anzahl}")
        Stats_Zurück = input("Um zurück zu gehen, drücke 'Entertaste'.\n")
        if Stats_Zurück in [""]:
            Hauptmenü()
    if Stats_Option in [""]:
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
    for i in range(2):
        for frame in Schlaf_Animation_Zeilen:
            print(frame, end="\r\n\n\n\n")
            time.sleep(0.5)
    print("\n\n")


Schon_geerntet = False
Ertrag = 0




def Arbeiter_kaufen():

    global Münzen, WahlA

    print("\n-----------------------------------------------------------------------")
    
    WahlA = input(f"Welchen Arbeiter möchtest du anstellen?\nDu hast {Münzen} Münzen\n1. Tierarzt 👨‍⚕ ({Arbeiter_Dictionary["Tierarzt"].Preis} Münzen)\n2. Gärtner 🧑‍🌾 ({Arbeiter_Dictionary["Gärtner"].Preis} Münzen)\n3. Touristenführer 📷 ({Arbeiter_Dictionary["Touristenführer"].Preis} Münzen)\n\n").lower().strip()

    if WahlA in ["1", "tierarzt"]:
        WahlA = "Tierarzt"
        KaufprozessA()
    elif WahlA in ["2", "gärtner"]:
        WahlA = "Gärtner"
        KaufprozessA()
    elif Wahl in ["3"]:
        WahlA = "Touristenführer"
        
    else:
        print("Ungülitge Eingabe. Versuch es nochmal.")
        return


def KaufprozessA():
    global Münzen, Arbeiter_Dictionary, WahlA, Arbeiter_Anzahl

    if Münzen >= int(Arbeiter_Dictionary[WahlA].Lohn):
        Münzen -= Arbeiter_Dictionary[WahlA].Lohn
        Arbeiter_Dictionary[WahlA].Anzahl += 1
        Arbeiter_Anzahl += 1

        print(f" Du hast einen {WahlA.capitalize()} angestellt! 🥳 (Restliche Münzen: {Münzen})")
    
    else:
        print(f"Nicht genug Münzen! Du brauchst {Arbeiter_Dictionary[Wahl].Lohn - Münzen} Münzen mehr. ❌")

def Lohn_ausgabe():
    global Münzen, Arbeiter_Dictionary
    Münzen = Münzen - Arbeiter_Dictionary["Tierarzt"].Lohn * Arbeiter_Dictionary["Tierarzt"].Anzahl
    Münzen = Münzen - Arbeiter_Dictionary["Gärtner"].Lohn * Arbeiter_Dictionary["Gärtner"].Anzahl
    Münzen = Münzen - Arbeiter_Dictionary["Touristenführer"].Lohn * Arbeiter_Dictionary["Touristenführer"].Anzahl

def Tutorial():
    print("\n\n\n\n\n-----------------------------------------------------------------------\n>>> Anleitung <<<\n- Optionen können mit den Zahlentasten ausgewählt werden\n- Ziel ist es, soviel Geld wie möglich zu verdienen\n- Viel Spass!!!")
    Tutorial_Ende = input("\nWenn du alles gelesen hast, drücke die <<Entertaste>>.\n\n\n")
    if Tutorial_Ende == "":
        wetter_wechsel()
        print("\n\n\n")
        time.sleep(3)
        Hauptmenü()
        

class Traktor:
    def __init__(self, Anzahl, Preis, Pflanzenmultiplikator, Tiermultiplikator, Möglich):
        self.Anzahl = Anzahl
        self.Preis = Preis
        self.Pflanzenmultiplikator = Pflanzenmultiplikator
        self.Tiermultiplikator = Tiermultiplikator
        self.Möglich = Möglich


Traktor_Dictionary = {
    "Traktor": Traktor(0, 20000, 3, 3, True),
    "Pflug": Traktor(0, 5000, 1.5, 1, True),
    "Düngerstreuer": Traktor(0, 5000, 2, 1, True),
    "Saatstreuer": Traktor(0, 5000, 1.2, 1, True),
    "Mähwerk": Traktor(0, 5000, 1.1, 1, True),
    "Pestizidspritzer": Traktor(0, 5000, 1.3, 1, True),
    "Transportbox": Traktor(0, 5000, 1.4, 1.5, True),
    "Viehtransportanhänger": Traktor(0, 20000, 1, 5, True)
}

Tiermultiplikator = 1.0
Pflanzenmultiplikator = 1.0

def KaufprozessT():
    global WahlT, Münzen, Traktor_Dictionary, Traktor, Tiermultiplikator, Pflanzenmultiplikator
    if Traktor_Dictionary[WahlT].Möglich == True:
        if Münzen >= Traktor_Dictionary[WahlT].Preis:
            Münzen -= Traktor_Dictionary[WahlT].Preis
            Traktor_Dictionary[WahlT].Anzahl += 1
            Traktor_Dictionary[WahlT].Möglich = False
            Tiermultiplikator = Traktor_Dictionary[WahlT].Tiermultiplikator * Tiermultiplikator
            Pflanzenmultiplikator = Traktor_Dictionary[WahlT].Pflanzenmultiplikator * Pflanzenmultiplikator
            print(f"Du hast 1 {WahlT.capitalize()} gekauft! 🚜 (Restliche Münzen: {Münzen})")
            time.sleep(4)
            Garage()
        else:
            print(f"Nicht genug Münzen! Du brauchst {Traktor_Dictionary[WahlT].Preis - Münzen} Münzen mehr. ❌")
            time.sleep(4)
            Garage()
    else:
        print(f"Du hast bereits 1 {WahlT.capitalize()} gekauft!")
    
    

def Garage():
    global Traktor_Dictionary, Münzen, WahlT, Tiermultiplikator, Pflanzenmultiplikator
    print("\n\n\n\n\n-----------------------------------------------------------------------\n>>> Garage <<<\n- Hier kannst du deinen Traktor kaufen und mit verschiedenen Upgrades versehen")
    if Traktor_Dictionary["Traktor"].Anzahl == 0:
        print("Du hast noch keinen Traktor!")
        print(f"\n\nDu hast {Münzen} Münzen")
        Traktor_Kauf = input(f"\n1. Traktor ({Traktor_Dictionary["Tratkor"].Preis} Münzen.\n\n\nHauptmenü -> 'Entertaste'.\n\n")
        if Traktor_Kauf in ["1"]:
            if Münzen >= 20000:
                Münzen -= 20000
                Traktor_Dictionary["Traktor"].Anzahl += 1
                Tiermultiplikator = Traktor_Dictionary["Traktor"].Tiermultiplikator * Tiermultiplikator
                Pflanzenmultiplikator = Traktor_Dictionary["Traktor"].Pflanzenmultiplikator * Pflanzenmultiplikator
                print("Du hast einen Traktor gekauft! 🚜")
                time.sleep(4)
                Garage()
            else:
                print("Nicht genug Münzen!")
                return
    else:
        print("\n\n\n\n\n-----------------------------------------------------------------------\n>>> Garage <<<\n- Hier kannst du deinen Traktor kaufen und mit verschiedenen Upgrades versehen")
        Upgrade_Wahl = input(f"\n1. Pflug ({Traktor_Dictionary['Pflug'].Preis} Münzen)\n2. Düngerstreuer ({Traktor_Dictionary['Düngerstreuer'].Preis} Münzen)\n3. Saatstreuer ({Traktor_Dictionary['Saatstreuer'].Preis} Münzen)\n4. Mähwerk ({Traktor_Dictionary['Mähwerk'].Preis} Münzen)\n5. Pestizidspritzer ({Traktor_Dictionary['Pestizidspritzer'].Preis} Münzen)\n6. Transportbox ({Traktor_Dictionary['Transportbox'].Preis} Münzen)\n7. Viehtransportanhänger ({Traktor_Dictionary['Viehtransportanhänger'].Preis} Münzen)\n")
        if Upgrade_Wahl in ["1"]:
            WahlT = "Pflug"
            KaufprozessT()
        elif Upgrade_Wahl in ["2"]:
            WahlT = "Düngerstreuer"
            KaufprozessT()
        elif Upgrade_Wahl in ["3"]:
            WahlT = "Saatstreuer"
            KaufprozessT()
        elif Upgrade_Wahl in ["4"]:
            WahlT = "Mähwerk"
            KaufprozessT()
        elif Upgrade_Wahl in ["5"]:
            WahlT = "Pestizidspritzer"
            KaufprozessT()
        elif Upgrade_Wahl in ["6"]:
            WahlT = "Transportbox"
            KaufprozessT()
        elif Upgrade_Wahl in ["7"]:
            WahlT = "Viehtransportanhänger"
            KaufprozessT()
        else:
            print("Ungültige Eingabe. Versuch es nochmal.")
            return


class RandomEvents():
    def __init__(self, name,WW):
        self.name = name
        self.WW = WW    

Nothing = RandomEvents("Nothing",0.79)
Lotto = RandomEvents("Lotto",0.01)
Wirtschaftskrise = RandomEvents("Wirtschaftskrise",0.01)
Wirtschaftsboom = RandomEvents("Wirtschaftsboom",0.01)
Virales_Video = RandomEvents("Virales Video",0.01)
Herrn_Schubert_getroffen = RandomEvents("Herrn Schubert getroffen",0.16)
Biene_Maia_getroffen = RandomEvents("Biene Maia getroffen",0.01)

def Random_event():
    global Ertrag, Ernte_Faktor, Aktueller_Wasserverbrauch, Runden, Wochenzähler, Münzen, Touristen_Anzahl
    Events = [Nothing, Lotto, Wirtschaftskrise, Wirtschaftsboom, Virales_Video, Herrn_Schubert_getroffen]
    weights = [event.WW for event in Events]
    Event = random.choices(Events, weights=weights, k=1)[0]

    if Event.name == "Nothing":
        pass
    elif Event.name == "Lotto":
        print("Du hast im Lotto gewonnen! 🎉")
        Münzen = Münzen + ((Wochenzähler+ 150)*Runden) * 50
    elif Event.name == "Wirtschaftskrise":
        print("Es gibt eine Wirtschaftskrise! 📉")
        Münzen = Münzen * 0.8
        Ernte_Faktor = Ernte_Faktor * 0.5
    elif Event.name == "Wirtschaftsboom":
        print("Es gibt einen Wirtschaftsboom! 📈")
        Münzen = Münzen * 1.2
        Ernte_Faktor = Ernte_Faktor * 1.5
    elif Event.name == "Virales Video":
        print("Ein virales Video über deinen Bauernhof hat viele Aufrufe! 🎥")
        Touristen_Anzahl = Touristen_Anzahl * 2
    elif Event.name == "Herrn Schubert getroffen":
        print("Du hast Herrn Schubert getroffen! Er gibt ein Autogramm! ✍")
        Events.pop(5)
        Nothing.WW = 0.96
    elif Event.name == "Biene Maia getroffen":
        print("Du hast Biene Maia getroffen! Sie gibt dir einen Bonus! 🍯")
        Honig_Produktion = Honig_Produktion * 3




def anzeigen_und_verkaufen(liste):
    global Insgesamt_Verdient
    while True:
        gesamtwert = 0
        for u in liste:
            gesamtwert += Lager_Dictionary[u].Anzahl * Lager_Dictionary[u].Verkaufswert
        print(f"\nGesamtwert deines Lagers: {gesamtwert} Münzen")
        print("\nDein Lagerbestand:")
        for i, name in enumerate(liste, 1):
            item = Lager_Dictionary[name]
            print(f"{i:>2}. {name:<19}  Anzahl: {item.Anzahl:<3}  Wert: {item.Verkaufswert:<3}Münzen")

        print("<<Enter>> Zurück")

        wahl = input("Was möchtest du verkaufen? (Nummer eingeben):\n\n")
        if not wahl.isdigit() and not wahl == "":
            print("Ungültige Eingabe.")
            continue
        if wahl == "":
            Lager_Menü()
        wahl = int(wahl)
        if wahl == len(liste)+1:
            break
        elif 1 <= wahl <= len(liste):
            produkt = liste[wahl-1]
            menge = input(f"Wieviel {produkt} möchtest du verkaufen? ")
            if menge.isdigit():
                menge = int(menge)
                item = Lager_Dictionary[produkt]
                if menge <= item.Anzahl:
                    item.Anzahl -= menge
                    einnahmen = menge * item.Verkaufswert
                    print(f'Du hast {menge}x "{produkt}" für {einnahmen} Münzen verkauft.')
                    Insgesamt_Verdient += einnahmen
                    time.sleep(2)
                else:
                    print("Nicht genug im Lager.")
                    time.sleep(2)
            else:
                print("Ungültige Menge.")
                time.sleep(2)
        else:
            print("Ungültige Auswahl.")
            time.sleep(2)

def Lager_Menü():
    while True:
        print("\n\n\n\n\n--- Lager-Menü ---")
        print("1. Pflanzenprodukte")
        print("2. Tierprodukte")
        print("3. Produkte")
        print("<<Enter>> Hauptmenü\n\n\n")
        wahl = input("Wähle eine Kategorie: ")

        if wahl == "1":
            print("\n--- Pflanzenprodukte ---")
            print("1. Feldfrüchte")
            print("2. Bäume")
            print("3. Büsche")
            print("<<Enter>> Zurück")
            unterwahl = input("Wähle eine Unterkategorie: ")
            if unterwahl == "1":
                anzeigen_und_verkaufen(Lager_Feld)
            elif unterwahl == "2":
                anzeigen_und_verkaufen(Lager_Baum)
            elif unterwahl == "3":
                anzeigen_und_verkaufen(Lager_Busch)
            elif unterwahl == "":
                Lager_Menü()
            else:
                print("Ungültige Eingabe.")
                time.sleep(2)
                Lager_Menü()
        elif wahl == "2":
            anzeigen_und_verkaufen(Lager_Tier)
        elif wahl == "3":
            anzeigen_und_verkaufen(Lager_Produkte)
        elif wahl == "":
            Hauptmenü()
        else:
            print("Ungültige Eingabe.")
            time.sleep(2)

class Maschinen:
    def __init__(self, Name, Preis, Gekauft, Stromverbrauch):
        self.Name = Name
        self.Wert = Preis
        self.Gekauft = Gekauft
        self.Stromverbrauch = Stromverbrauch

Maschinen_Dictionary = {
    "Mühle": Maschinen("Mühle", 0, "❌", 40),
    "Zerkleinerungsmixer": Maschinen("Zerkleinerungsmixer", 0, "❌", 40),
    "Schneidemaschine": Maschinen("Schneidemaschine", 0, "❌", 40),
    "Mixer": Maschinen("Mixer", 0, "❌", 40),
    "Schleudermaschine": Maschinen("Schleudermaschine", 0, "❌", 40),
    "Käsemaschine": Maschinen("Käsemaschine", 0, "❌", 40),
    "Knetmaschine": Maschinen("Knetmaschine", 0, "❌", 40),
    "Backofen": Maschinen("Backofen", 0, "❌", 40),
    "Herd": Maschinen("Herd", 0, "❌", 40),
    "Fritteuse": Maschinen("Fritteuse", 0, "❌", 40),
    "Webstuhl": Maschinen("Webstuhl", 0, "❌", 40),
    "Verpackungsmaschine": Maschinen("Verpackungsmaschine", 0, "❌", 40),
}
Mühle = Maschinen_Dictionary["Mühle"]
Zerkleinerungsmixer = Maschinen_Dictionary["Zerkleinerungsmixer"]
Schneidemaschine = Maschinen_Dictionary["Zerkleinerungsmixer"]
Mixer = Maschinen_Dictionary["Mixer"]
Schleudermaschine = Maschinen_Dictionary["Schleudermaschine"]
Käsemaschine = Maschinen_Dictionary["Käsemaschine"]
Knetmaschine = Maschinen_Dictionary["Knetmaschine"]
Backofen = Maschinen_Dictionary["Backofen"]
Herd = Maschinen_Dictionary["Herd"]
Fritteuse = Maschinen_Dictionary["Fritteuse"]
Webstuhl = Maschinen_Dictionary["Webstuhl"]
Verpackungsmaschine = Maschinen_Dictionary["Verpackungsmaschine"]

Weizen = Lager_Dictionary["Weizen"]
Mais = Lager_Dictionary["Mais"]
Kartoffel = Lager_Dictionary["Kartoffel"]
Sonnenblume = Lager_Dictionary["Sonnenblume"]
Apfel = Lager_Dictionary["Apfel"]
Kirsche = Lager_Dictionary["Kirsche"]
Birne = Lager_Dictionary["Birne"]
Orange = Lager_Dictionary["Orange"]
Erdbeere = Lager_Dictionary["Erdbeere"]
Himbeere = Lager_Dictionary["Himbeere"]
Blaubeere = Lager_Dictionary["Blaubeere"]
Schwarzbeere = Lager_Dictionary["Schwarzbeere"]
Eier = Lager_Dictionary["Eier"]
Kuhmilch = Lager_Dictionary["Kuhmilch"]
Wolle = Lager_Dictionary["Wolle"]
Schafsmilch = Lager_Dictionary["Schafsmilch"]
Ziegenmilch = Lager_Dictionary["Ziegenmilch"]
Honig = Lager_Dictionary["Honig"]
Mehl = Lager_Dictionary["Mehl"]
Tierfutter = Lager_Dictionary["Tierfutter"]
Zucker = Lager_Dictionary["Zucker"]
Rahmkäse = Lager_Dictionary["Rahmkäse"]
Ziegenkäse = Lager_Dictionary["Ziegenkäse"]
Schafskäse = Lager_Dictionary["Schafskäse"]
Käseküchlein = Lager_Dictionary["Käseküchlein"]
Honigkuchen = Lager_Dictionary["Honigkuchen"]
Apfelkuchen = Lager_Dictionary["Apfelkuchen"]
Birnenkuchen = Lager_Dictionary["Birnenkuchen"]
Kirschenkuchen = Lager_Dictionary["Kirschenkuchen"]
Erdbeermarmelade = Lager_Dictionary["Erdbeermarmelade"]
Himbeermarmelade = Lager_Dictionary["Himbeermarmelade"]
Blaubeerkuchen = Lager_Dictionary["Blaubeerkuchen"]
Schwarzbeerkuchen = Lager_Dictionary["Schwarzbeerkuchen"]
Kartoffelgratin = Lager_Dictionary["Kartoffelgratin"]
Pommes = Lager_Dictionary["Pommes"]
Stoff = Lager_Dictionary["Stoff"]
Fruchtsalat = Lager_Dictionary["Fruchtsalat"]
Joghurt = Lager_Dictionary["Joghurt"]
Orange = Lager_Dictionary["Orange"]
Orangensaft = Lager_Dictionary["Orangensaft"]


class Rezepte:
    def __init__(self, Produkt, Dependencies, Zutaten, Automatisch, Ordnungszahl):
        self.Produkt = Produkt
        self.Dependencies = Dependencies
        self.Zutaten = Zutaten
        self.Automatisch = Automatisch
        self.Ordnungszahl = Ordnungszahl
        
Rezepte_Dictionary = {
    "Mehl": Rezepte("Mehl", [Mühle], ["Weizen"], 0, 1),
    "Tierfutter": Rezepte("Tierfutter", [Zerkleinerungsmixer, Mixer], ["Mais"], 0, 2),
    "Zucker": Rezepte("Zucker", [Mühle], ["Honig"], 0, 3),
    "Rahmkäse": Rezepte("Rahmkäse", [Käsemaschine], ["Kuhmilch"], 0, 4),
    "Ziegenkäse": Rezepte("Ziegenkäse", [Käsemaschine], ["Ziegenmilch"], 0, 5),
    "Schafskäse": Rezepte("Schafskäse", [Käsemaschine], ["Schafsmilch"], 0, 6),
    "Käseküchlein": Rezepte("Käseküchlein", [Knetmaschine, Backofen], [["Rahmkäse", "Ziegenkäse", "Schafskäse"], "Eier", "Mehl"], 0, 7),
    "Honigkuchen": Rezepte("Honigkuchen", [Knetmaschine, Backofen], ["Eier", "Kuhmilch", "Mehl", "Honig"], 0, 8),
    "Apfelkuchen": Rezepte("Apfelkuchen", [Knetmaschine, Backofen, Schneidemaschine], ["Eier", "Kuhmilch", "Mehl", "Zucker", "Apfel"], 0, 9),
    "Birnenkuchen": Rezepte("Birnenkuchen", [Knetmaschine, Backofen, Schneidemaschine], ["Eier", "Kuhmilch", "Mehl", "Zucker", "Birne"], 0, 10),
    "Kirschenkuchen": Rezepte("Kirschenkuchen", [Knetmaschine, Backofen, Schneidemaschine], ["Eier", "Kuhmilch", "Mehl", "Zucker", "Kirsche"], 0, 11),
    "Erdbeermarmelade": Rezepte("Erdbeermarmelade", [Zerkleinerungsmixer, Herd, Verpackungsmaschine], ["Zucker", "Erdbeere"], 0, 12),
    "Himbeermarmelade": Rezepte("Himbeermarmelade", [Zerkleinerungsmixer, Herd, Verpackungsmaschine], ["Zucker", "Himbeere"], 0, 13),
    "Blaubeerkuchen": Rezepte("Blaubeerkuchen", [Knetmaschine, Backofen, Schneidemaschine], ["Eier", "Kuhmilch", "Mehl", "Zucker", "Blaubeere"], 0, 14),
    "Schwarzbeerkuchen": Rezepte("Schwarzbeerkuchen", [Knetmaschine, Backofen, Schneidemaschine], ["Eier", "Kuhmilch", "Mehl", "Zucker", "Schwarzbeere"], 0, 15),
    "Kartoffelgratin": Rezepte("Kartoffelgratin", [Schneidemaschine, Backofen], ["Kartoffel"], 0, 16),
    "Pommes": Rezepte("Pommes", [Schneidemaschine, Fritteuse], ["Kartoffel"], 0, 17),
    "Stoff": Rezepte("Stoff", [Webstuhl], ["Wolle"], 0, 18),
    "Fruchtsalat": Rezepte("Fruchtsalat", [Schneidemaschine, Mixer], ["Apfel", "Birne", "Kirsche", "Orange", "Erdbeere", "Blaubeere"], 0, 19),
    "Joghurt": Rezepte("Joghurt", [Mixer, Verpackungsmaschine], ["Kuhmilch", "Fruchtsalat"], 0, 20),
    "Orangensaft": Rezepte("Orangensaft", [Zerkleinerungsmixer, Mixer], ["Orange"], 0, 21)
}

def Verarbeitung():
    global Pflanzen_Dictionary, Tierfutter_Dictionary, Tier_Dictionary, Arbeiter_Dictionary, Infrastruktur_Dictionary, Münzen, Lager_Dictionary
    print("\n\n\n\n\n-----------------------------------------------------------------------\n>>> Verarbeitung <<<\n- Wähle eine Option.")
    Wahl1 = input(f"\n1. Produktion 🛠️\n2. Maschinen 🖨️\n3. Lager 🛖\n4. Zurück ↩️\n")
    if Wahl1 in ["1"]:
        Produktions_Menü()
    elif Wahl1 in ["2"]:
        Maschinen_Übersicht()
    elif Wahl1 in ["3"]:
        Lager_Menü()
    elif Wahl1 in ["4"]:
        Hauptmenü()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        Verarbeitung()
        
def Produktions_Menü():
    global Produkt_Wahl, Automatisch_Wahl, Automatisch_Änderung, Rezepte_Dictionary
    print("\n\n\n\n\n-----------------------------------------------------------------------\n>>> Produktion 1<<<\n- Hier kannst du deine Produkte verarbeiten.")
    Produkt_Wahl = input(f"""                                                        '?' >> Hilfe
        Was möchtest du Herstellen?                     Automatische Produktion:
            1. Mehl                                      {Rezepte_Dictionary["Mehl"].Automatisch}/Woche
            2. Tierfutter                                {Rezepte_Dictionary["Tierfutter"].Automatisch}/Woche
            3. Zucker                                    {Rezepte_Dictionary["Zucker"].Automatisch}/Woche
            4. Rahmkäse                                  {Rezepte_Dictionary["Rahmkäse"].Automatisch}/Woche
            5. Ziegenkäse                                {Rezepte_Dictionary["Ziegenkäse"].Automatisch}/Woche
            6. Schafskäse                                {Rezepte_Dictionary["Schafskäse"].Automatisch}/Woche
            Seite 1 '>'                                 'Entertaste' >> Zurück\n""").strip().lower()
    if Produkt_Wahl in ["1"]:
        Produkt_Wahl = "Mehl"
        Produktionsprozess()
    elif Produkt_Wahl in ["2"]:
        Produkt_Wahl = "Tierfutter"
        Produktionsprozess()
    elif Produkt_Wahl in ["3"]:
        Produkt_Wahl = "Zucker"
        Produktionsprozess()
    elif Produkt_Wahl in ["4"]:
        Produkt_Wahl = "Rahmkäse"
        Produktionsprozess()
    elif Produkt_Wahl in ["5"]:
        Produkt_Wahl = "Ziegenkäse"
        Produktionsprozess()
    elif Produkt_Wahl in ["6"]:
        Produkt_Wahl = "Schafskäse"
        Produktionsprozess()
    elif Produkt_Wahl in [">"]:
        Produktions_Menü2()
    elif Produkt_Wahl in [""]:
        Hauptmenü()
    elif Produkt_Wahl in ["?", "hilfe"]:
        Produktions_Menü_Hilfe()
    elif Produkt_Wahl[:-1].isdigit() and Produkt_Wahl[-1] in "+-":
        Automatisch_Wahl = Produkt_Wahl[:-1]
        Automatisch_Änderung = Produkt_Wahl[-1]
        Upgrade_Automatische_Produktion()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        time.sleep(2)
        Produktions_Menü()
    
def Produktions_Menü2():
    global Produkt_Wahl, Automatisch_Wahl, Automatisch_Änderung, Rezepte_Dictionary
    print("\n\n\n\n\n-----------------------------------------------------------------------\n>>> Produktion 2<<<\n- Hier kannst du deine Produkte verarbeiten.")
    Produkt_Wahl = input(f"""
        Was möchtest du Herstellen?                      Automatische Produktion:
            7. Käseküchlein                               {Rezepte_Dictionary["Käseküchlein"].Automatisch}/Woche
            8. Honigkuchen                                {Rezepte_Dictionary["Honigkuchen"].Automatisch}/Woche
            9. Apfelkuchen                                {Rezepte_Dictionary["Apfelkuchen"].Automatisch}/Woche
            10. Birnenkuchen                              {Rezepte_Dictionary["Birnenkuchen"].Automatisch}/Woche
            11. Kirschenkuchen                            {Rezepte_Dictionary["Kirschenkuchen"].Automatisch}/Woche
            12. Erdbeermarmelade                          {Rezepte_Dictionary["Erdbeermarmelade"].Automatisch}/Woche
           '<' Seite 2 '>'                               'Entertaste' >> Zurück\n""")
    if Produkt_Wahl in ["7"]:
        Produkt_Wahl = "Käseküchlein"
        Produktionsprozess()
    elif Produkt_Wahl in ["8"]:
        Produkt_Wahl = "Honigkuchen"
        Produktionsprozess()
    elif Produkt_Wahl in ["9"]:
        Produkt_Wahl = "Apfelkuchen"
        Produktionsprozess()
    elif Produkt_Wahl in ["10"]:
        Produkt_Wahl = "Birnenkuchen"
        Produktionsprozess()
    elif Produkt_Wahl in ["11"]:
        Produkt_Wahl = "Kirschenkuchen"
        Produktionsprozess()
    elif Produkt_Wahl in ["12"]:
        Produkt_Wahl = "Erdbeermarmelade"
        Produktionsprozess()
    elif Produkt_Wahl in [">"]:
        Produktions_Menü3()
    elif Produkt_Wahl in ["<"]:
        Produktions_Menü()
    elif Produkt_Wahl in [""]:
        Produktions_Menü()
    elif Produkt_Wahl[:-1].isdigit() and Produkt_Wahl[-1] in "+-":
        Automatisch_Wahl = Produkt_Wahl[:-1]
        Automatisch_Änderung = Produkt_Wahl[-1]
        Upgrade_Automatische_Produktion()
    else:    
        print("Ungültige Eingabe. Versuch es nochmal.")
        time.sleep(2)
        Produktions_Menü2()


      
    
    
def Produktions_Menü3():
    global Produkt_Wahl, Automatisch_Wahl, Automatisch_Änderung, Rezepte_Dictionary
    
    print("\n\n\n\n\n-----------------------------------------------------------------------\n>>> Produktion 3<<<\n- Hier kannst du deine Produkte verarbeiten.")
    Produkt_Wahl = input(f"""
        Was möchtest du Herstellen?                      Automatische Produktion:
            13. Himbeermarmelade                          {Rezepte_Dictionary["Himbeermarmelade"].Automatisch}/Woche
            14. Blaubeerkuchen                            {Rezepte_Dictionary["Blaubeerkuchen"].Automatisch}/Woche
            15. Schwarzbeerkuchen                         {Rezepte_Dictionary["Schwarzbeerkuchen"].Automatisch}/Woche
            16. Kartoffelgratin                           {Rezepte_Dictionary["Kartoffelgratin"].Automatisch}/Woche
            17. Pommes                                    {Rezepte_Dictionary["Pommes"].Automatisch}/Woche
            18. Stoff                                     {Rezepte_Dictionary["Stoff"].Automatisch}/Woche
           '<' Seite 3 '>'                               'Entertaste' >> Zurück\n""")
    if Produkt_Wahl in ["13"]:
        Produkt_Wahl = "Himbeermarmelade"
        Produktionsprozess()
    elif Produkt_Wahl in ["14"]:
        Produkt_Wahl = "Blaubeerkuchen"
        Produktionsprozess()
    elif Produkt_Wahl in ["15"]:
        Produkt_Wahl = "Schwarzbeerkuchen"
        Produktionsprozess()
    elif Produkt_Wahl in ["16"]:
        Produkt_Wahl = "Kartoffelgratin"
        Produktionsprozess()
    elif Produkt_Wahl in ["17"]:
        Produkt_Wahl = "Pommes"
        Produktionsprozess()
    elif Produkt_Wahl in ["18"]:
        Produkt_Wahl = "Stoff"
        Produktionsprozess()
    elif Produkt_Wahl in [">"]:
        Produktions_Menü4()
    elif Produkt_Wahl in ["<"]:
        Produktions_Menü2()
    elif Produkt_Wahl in [""]:
        Produktions_Menü()
    elif Produkt_Wahl[:-1].isdigit() and Produkt_Wahl[-1] in "+-":
        Automatisch_Wahl = Produkt_Wahl[:-1]
        Automatisch_Änderung = Produkt_Wahl[-1]
        Upgrade_Automatische_Produktion()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        time.sleep(2)
        Produktions_Menü3()
    
def Produktions_Menü4():
    global Produkt_Wahl, Automatisch_Wahl, Automatisch_Änderung, Rezepte_Dictionary
    print("\n\n\n\n\n-----------------------------------------------------------------------\n>>> Produktion 4<<<\n- Hier kannst du deine Produkte verarbeiten.")
    print("\n\n\n\n\n-----------------------------------------------------------------------\n>>> Produktion 4<<<\n- Hier kannst du deine Produkte verarbeiten.")
    Produkt_Wahl = input(f"""
        Was möchtest du Herstellen?                      Automatische Produktion:
            19. Fruchtsalat                               {Rezepte_Dictionary["Fruchtsalat"].Automatisch}/Woche
            20. Joghurt                                   {Rezepte_Dictionary["Joghurt"].Automatisch}/Woche
            21. Orangensaft                               {Rezepte_Dictionary["Orangensaft"].Automatisch}/Woche
           '<' Seite 4                                   'Entertaste' >> Zurück\n""")
    if Produkt_Wahl in ["19"]:
        Produkt_Wahl = "Fruchtsalat"
        Produktionsprozess()
    elif Produkt_Wahl in ["20"]:
        Produkt_Wahl = "Joghurt"
        Produktionsprozess()
    elif Produkt_Wahl in ["21"]:
        Produkt_Wahl = "Orangensaft"
        Produktionsprozess()
    elif Produkt_Wahl in ["<"]:
        Produktions_Menü3()
    elif Produkt_Wahl in [""]:
        Produktions_Menü()
    if Produkt_Wahl[:-1].isdigit() and Produkt_Wahl[-1] in "+-":
        Automatisch_Wahl = Produkt_Wahl[:-1]
        Automatisch_Änderung = Produkt_Wahl[-1]
        Upgrade_Automatische_Produktion()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        Produktions_Menü4()

def Upgrade_Automatische_Produktion():
    global Produkt_Wahl, Automatisch_Wahl, Automatisch_Änderung, Rezepte_Dictionary, Maschinen_Dictionary
    try:
        Produktnamen_Liste = list(Rezepte_Dictionary.keys())
        Produkt_Index = int(Automatisch_Wahl) - 1
        Produkt_Name = Produktnamen_Liste[Produkt_Index]
    except (ValueError, IndexError):
        print("❌ Ungültige Produktauswahl.")
        time.sleep(2)
        Produktions_Menü()
        return

    rezept = Rezepte_Dictionary[Produkt_Name]

    if Automatisch_Änderung == "+":
        fehlende_maschinen = [
            maschine for maschine in rezept.Dependencies
            if Maschinen_Dictionary[maschine.Name].Gekauft != "✅"
        ]
        if fehlende_maschinen:
            print("❌ Upgrade nicht möglich. Fehlende Maschinen:")
            for m in fehlende_maschinen:
                print(f"  - {m.Name}")
            time.sleep(3)
            Produktions_Menü()
            return

        rezept.Automatisch += 1
        print(f"⬆️ Automatische Produktion von {rezept.Produkt} auf Stufe {rezept.Automatisch} erhöht!")

    elif Automatisch_Änderung == "-":
        if rezept.Automatisch > 0:
            rezept.Automatisch -= 1
            print(f"⬇️ Automatische Produktion von {rezept.Produkt} auf Stufe {rezept.Automatisch} gesenkt!")
        else:
            print("❌ Stufe ist bereits bei 0 - kann nicht weiter gesenkt werden.")

    else:
        print("❌ Ungültige Eingabe (weder '+' noch '-')")
    
    time.sleep(2)
    if Automatisch_Wahl in ["8", "9", "10", "11", "12"]:
        Produktions_Menü2()
    elif Automatisch_Wahl in ["13", "14", "15", "16", "17"]:
        Produktions_Menü3()
    elif Automatisch_Wahl in ["19", "20", "21"]:
        Produktions_Menü4()
    else:
        Produktions_Menü()
        
        

def Produktions_Menü_Hilfe():
    print("""\n\n\n\n\n-----------------------------------------------------------------------
    >>> Hilfe <<<
    - Um Produkte herzustellen, wähle die gewünschte Option aus dem Menü.
    - Du kannst nur Produkte herstellen, wenn du die benötigten Maschinen und Zutaten hast.
    - Wenn du nicht genug Zutaten hast, wird eine Fehlermeldung angezeigt.
    - Du kannst die Maschinen im Maschinen-Menü kaufen.
    - Wenn du die Automatische Produktion erhöhen möchtest, drücke die gewünschte Zahl und '+' oder '-' (z.B. '1+' oder '2-').
    - Die Automatische Produktion wird in der nächsten Woche aktualisiert.
    """)
    Zurück = input("\n\nDrücke 'Enter' um zurück zu gehen.")
    if Zurück in [""]:
        Produktions_Menü()
    else:
        print("Ungültige Eingabe.")
        time.sleep(2)
        Produktions_Menü_Hilfe()
    
def get_zutat_name(lager_obj):
    for name, obj in Lager_Dictionary.items():
        if obj == lager_obj:
            return name
    return "Unbekannt"

def Produktionsprozess():
    global Produkt_Wahl, Maschinen_Dictionary, Rezepte_Dictionary, Lager_Dictionary, Lager_Produkte
    rezept = Rezepte_Dictionary[Produkt_Wahl]
    fehlende_maschinen = [m.Name for m in rezept.Dependencies if m.Gekauft != "✅"]

    if fehlende_maschinen:
        print(f"\n❌ Du kannst '{Produkt_Wahl}' noch nicht herstellen.")
        print("Dir fehlen folgende Maschinen:")
        for maschine in fehlende_maschinen:
            print(f" - {maschine}")
        time.sleep(2)
        Verarbeitung()
        

    for zutat in rezept.Zutaten:
        if isinstance(zutat, list):
            if not any(Lager_Dictionary[sub_zutat].Anzahl > 0 for sub_zutat in zutat):
                print("❌ Nicht genug von einer der Zutaten:")
                for sub_zutat in zutat:
                    print(f" - {get_zutat_name(sub_zutat)}: {Lager_Dictionary[sub_zutat].Anzahl}")
                time.sleep(2)
                Verarbeitung()
                
        else:
            if Lager_Dictionary[zutat].Anzahl <= 0:
                print(f"❌ Nicht genug von der Zutat: {get_zutat_name(zutat)} ({Lager_Dictionary[zutat].Anzahl})")
                time.sleep(2)
                Verarbeitung()
                
    for zutat in rezept.Zutaten:
        if isinstance(zutat, list):
            for Lager_Dictionary[sub_zutat] in zutat:
                Lager_Dictionary[sub_zutat].Anzahl -= 1
        else:
            Lager_Dictionary[zutat].Anzahl -= 1
    print(f"\n✅ '{Produkt_Wahl}' wird produziert...")
    print("⏳ Produktion läuft...")
    time.sleep(2)
    print(f"✅ '{Produkt_Wahl}' wurde erfolgreich produziert!")
    time.sleep(2)
    Lager_Dictionary[Produkt_Wahl].Anzahl += 1
        
    
    
    

def Maschinen_Übersicht():
    global Maschinen_Dictionary, Münzen, WahlMÜ
    print("\n\n\n\n\n-----------------------------------------------------------------------\n>>> Maschinen <<<\n")

    WahlMÜ = input("\n\n1. Maschinen kaufen\n\n'Entertaste' um zurück zu gehen.\n")
    if WahlMÜ in ["1"]:
        Maschinen_Menü1()
    elif WahlMÜ in [""]:
        Verarbeitung()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        Maschinen_Übersicht()
    
    
    
    
def Maschinen_Menü1():
    global Maschinen_Dictionary, Münzen, WahlM   
    Gekauft = Maschinen_Dictionary
    print("❌ = nicht gekauft, ✅ = gekauft")
    WahlM = input(f"\n1. Mühle ({Maschinen_Dictionary['Mühle'].Preis} Münzen {Gekauft["Mühle"].Gekauft})\n2. Zerkleinerungsmixer ({Maschinen_Dictionary['Zerkleinerungsmixer'].Preis} Münzen {Gekauft["Zerkleinerungsmixer"].Gekauft})\n3. Schneidemaschine ({Maschinen_Dictionary['Schneidemaschine'].Preis} Münzen {Gekauft["Schneidemaschine"].Gekauft})\n4. Mixer ({Maschinen_Dictionary['Mixer'].Preis} Münzen {Gekauft["Mixer"].Gekauft})\n5. Schleudermaschine ({Maschinen_Dictionary['Schleudermaschine'].Preis} Münzen {Gekauft["Schleudermaschine"].Gekauft})\n6. Käsemaschine ({Maschinen_Dictionary['Käsemaschine'].Preis} Münzen {Gekauft["Käsemaschine"].Gekauft})\n7. Seite 2 >>>\n\nHauptmenü -> 'Entertaste'.\n")
    if WahlM in ["1"]:
        WahlM = "Mühle"
        KaufprozessM()
    elif WahlM in ["2"]:
        WahlM = "Zerkleinerungsmixer"
        KaufprozessM()
    elif WahlM in ["3"]:
        WahlM = "Schneidemaschine"
        KaufprozessM()
    elif WahlM in ["4"]:
        WahlM = "Mixer"
        KaufprozessM()
    elif WahlM in ["5"]:
        WahlM = "Schleudermaschine"
        KaufprozessM()
    elif WahlM in ["6"]:
        WahlM = "Käsemaschine"
        KaufprozessM()
    elif WahlM in ["7"]:
        Maschinen_Menü2()
    elif WahlM in [""]:
        Hauptmenü()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        Maschinen_Menü1()

def Maschinen_Menü2():
    global Maschinen_Dictionary, Münzen, WahlM
    Gekauft = Maschinen_Dictionary
    print("❌ = nicht gekauft, ✅ = gekauft")
    WahlM = input(f"\n1. Knetmaschine ({Maschinen_Dictionary['Knetmaschine'].Preis} Münzen) {Gekauft["Knetmaschine"].Gekauft}\n2. Backofen ({Maschinen_Dictionary['Backofen'].Preis} Münzen {Gekauft["Backofen"].Gekauft})\n3. Herd ({Maschinen_Dictionary['Herd'].Preis} Münzen {Gekauft["Herd"].Gekauft})\n4. Fritteuse ({Maschinen_Dictionary['Fritteuse'].Preis} Münzen {Gekauft["Fritteuse"].Gekauft})\n5. Webstuhl ({Maschinen_Dictionary['Webstuhl'].Preis} Münzen {Gekauft["Webstuhl"].Gekauft})\n6. Verpackungsmaschine ({Maschinen_Dictionary['Verpackungsmaschine'].Preis} Münzen {Gekauft["Verpackungsmaschine"].Gekauft})\n\nHauptmenü -> 'Entertaste'.\n")
    if WahlM in ["1"]:
        WahlM = "Knetmaschine"
        KaufprozessM()
    elif WahlM in ["2"]:
        WahlM = "Backofen"
        KaufprozessM()
    elif WahlM in ["3"]:
        WahlM = "Herd"
        KaufprozessM()
    elif WahlM in ["4"]:
        WahlM = "Fritteuse"
        KaufprozessM()
    elif WahlM in ["5"]:
        WahlM = "Webstuhl"
        KaufprozessM()
    elif WahlM in ["6"]:
        WahlM = "Verpackungsmaschine"
        KaufprozessM()
    elif WahlM in [""]:
        Hauptmenü()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        Maschinen_Menü2()

def KaufprozessM():
    global Münzen, Maschinen_Dictionary, WahlM, Energie_verbraucht, Energieproduktion
    if Maschinen_Dictionary[WahlM].Gekauft == "❌":
        if Maschinen_Dictionary[WahlM].Stromverbrauch + Energie_verbraucht > Energieproduktion:
            print(f"\n\nDu musst einen neuen Stromgenerator bauen, um die Maschine anzutreiben.\n\n")
            time.sleep(2)
            Maschinen_Übersicht()
        if Münzen >= Maschinen_Dictionary[WahlM].Preis:
            Münzen -= Maschinen_Dictionary[WahlM].Preis
            Maschinen_Dictionary[WahlM].Gekauft = "✅"
            Energie_verbraucht += Maschinen_Dictionary[WahlM].Stromverbrauch
            print(f"Du hast 1 {WahlM.capitalize()} gekauft! 🚜 (Restliche Münzen: {Münzen})")
            time.sleep(3)
            Maschinen_Übersicht()
        else:
            print(f"Nicht genug Münzen! Du brauchst {Maschinen_Dictionary[WahlM].Preis - Münzen} Münzen mehr. ❌")
            time.sleep(3)
            Maschinen_Übersicht()
    else:
        print(f"Du hast bereits 1 {WahlM.capitalize()} gekauft!")
        time.sleep(3)
        Maschinen_Übersicht()


def KaufprozessP():
    global Münzen, Ertrag, Pflanzen, Aktueller_Wasserverbrauch, Energie_verbraucht, Wahl, Pflanzen_Anzahl
    if Energieproduktion < Energie_verbraucht + 10:
        print(f"Du musst einen neuen Stromgenerator bauen, um die Wasserpumpe anzutreiben.")
        time.sleep(2)
        return

    if Münzen >= int(Pflanzen_Dictionary[Wahl].Preis):
        Münzen -= Pflanzen_Dictionary[Wahl].Preis
        Pflanzen_Dictionary[Wahl].Anzahl += 1
        Pflanzen_Anzahl +=1
        Energie_verbraucht += 10
        Aktueller_Wasserverbrauch += Pflanzen_Dictionary[Wahl].Wasserverbrauch
        Ertrag += Pflanzen_Dictionary[Wahl].Ernte_Faktor
        
        print(f"Du hast 1 {Wahl.capitalize()} angepflanzt! 🌱 (Restliche Münzen: {Münzen})")
    else:
        print(f"Nicht genug Münzen! Du brauchst {Pflanzen_Dictionary[Wahl].Preis - Münzen} Münzen mehr. ❌")



def Feldfrucht():
    global Münzen, Wahl
    
    print("\n-----------------------------------------------------------------------")
    Wahl = input(f"Welche Feldfrucht möchtest du anplanzen?\nDu hast {Münzen} Münzen\n\n1. Weizen 🌾 ({Pflanzen_Dictionary["weizen"].Preis} Münzen)\n\n2. Mais 🌽 ({Pflanzen_Dictionary["mais"].Preis} Münzen)\n\n3. Kartoffel 🥔 ({Pflanzen_Dictionary["kartoffel"].Preis} Münzen)\n\n4. Sonnenblume 🌻 ({Pflanzen_Dictionary["sonnenblume"].Preis} Münzen)                                                'Entertaste' -> Hauptmenü\n\n").lower().strip()

    if Wahl in ["1", "weizen"]:    
        Wahl = "weizen"
        KaufprozessP()
    elif Wahl in ["2", "mais"]:
        Wahl = "mais"
        KaufprozessP()
    elif Wahl in ["3", "kartoffel"]:
        Wahl = "kartoffel"
        KaufprozessP()
    elif Wahl in ["4", "sonnenblume"]:
        Wahl = "sonnenblume"
        KaufprozessP()
    elif Wahl in [""]:
        Hauptmenü()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        return


def Fruchtbäume():
    global Münzen, Wahl
    
    print("\n-----------------------------------------------------------------------")
    Wahl = input(f"Welchen Fruchtbaum möchtest du anpflanzen?\nDu hast {Münzen} Münzen\n\n1. Apfelbaum 🍏 ({Pflanzen_Dictionary["apfelbaum"].Preis} Münzen)\n\n2. Kirschbaum 🍒 ({Pflanzen_Dictionary["kirschbaum"].Preis} Münzen)\n\n3. Birnenbaum 🍐 ({Pflanzen_Dictionary["birnenbaum"].Preis} Münzen) \n\n4. Orangenbaum 🍊 ({Pflanzen_Dictionary["orangenbaum"].Preis} Münzen)                                             'Entertaste' -> Hauptmenü\n\n").lower().strip()

    if Wahl in ["1", "apfelbaum"]:   
        Wahl = "apfelbaum"
        KaufprozessP()
    elif Wahl in ["2", "kirschbaum"]:
        Wahl = "kirschbaum"
        KaufprozessP()
    elif Wahl in ["3", "birnenbaum"]:
        Wahl = "birnenbaum"
        KaufprozessP()
    elif Wahl in ["4", "orangenbaum"]:
        Wahl = "orangenbaum"
        KaufprozessP()
    elif Wahl in [""]:
        Hauptmenü()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        return

    
def Beerenbusch():
    global Münzen, Wahl
    
    print("\n-----------------------------------------------------------------------")
    Wahl = input(f"Welchen Beerenbusch möchtest du anpflanzen?\nDu hast {Münzen} Münzen\n\n1. Erdbeerbusch 🍓 ({Pflanzen_Dictionary["erdbeerbusch"].Preis} Münzen)\n\n2. Himbeerbusch 🍇 ({Pflanzen_Dictionary["himbeerbusch"].Preis} Münzen)\n\n3. Blaubeerbusch 🫐 ({Pflanzen_Dictionary["blaubeerbusch"].Preis} Münzen)\n\n4. Schwarzbeerbusch 🖤🍇 ({Pflanzen_Dictionary["schwarzbeerbusch"].Preis} Münzen)                                                  'Entertaste' -> Hauptmenü\n\n").lower().strip()

    if Wahl in ["1", "erdbeerbusch"]:
        Wahl = "erdbeerbusch"
        KaufprozessP()
    elif Wahl in ["2", "himbeerbusch"]:
        Wahl = "himbeerbusch"
        KaufprozessP()
    elif Wahl in ["3", "blaubeerbusch"]:
        Wahl = "blaubeerbusch"
        KaufprozessP()
    elif Wahl in ["4", "schwarzbeerbusch"]:
        Wahl = "schwarzbeerbusch"
        KaufprozessP()
    elif Wahl in [""]:
        Hauptmenü()
    else:
        print("Ungülitge Eingabe. Versuch es nochmal.")
        Beerenbusch()

    
def Pflanzenart():
    print("\n-----------------------------------------------------------------------\nPflanzenart:")
    Pflanzenart_Wahl = input("Was möchtest du pflanzen?\n\n1. 🌾 Feldfrucht\n\n2. 🍎 Fruchtbäume\n\n3. 🍓 Beerenbüsche\n").lower().strip()
    if Pflanzenart_Wahl in ["1", "feldfrucht"]:
        Feldfrucht()
    elif Pflanzenart_Wahl in ["2", "fruchtbaum"]:
        Fruchtbäume()
    elif Pflanzenart_Wahl in ["3", "beerenbusch"]:
        Beerenbusch()
        
    
def KaufprozessTiere():
    global WahlTiere, Münzen, Tierfutter_Dictionary, Tier_Dictionary, Aktueller_Wasserverbrauch, Tier_Anzahl, Plural
    print(f"\n\n\n\n\n\nWie viele {Plural} möchtest du kaufen?")
    KaufAnzahl = input("")
    if KaufAnzahl.isdigit():
        KaufAnzahl = int(KaufAnzahl)
    else:
        print("Ungültige Eingabe.")
        time.sleep(2)
        Tier_Menü()
    if Münzen >= Tier_Dictionary[WahlTiere].Preis * KaufAnzahl:
        Münzen -= Tier_Dictionary[WahlTiere].Preis * KaufAnzahl
        Tier_Dictionary[WahlTiere].Anzahl += 1 * KaufAnzahl
        Aktueller_Wasserverbrauch += Tier_Dictionary[WahlTiere].Wasserverbrauch * KaufAnzahl
        Tierfutter_Dictionary["Tierfutter"].Verbrauch += Tier_Dictionary[WahlTiere].Tierfutter * KaufAnzahl
        if KaufAnzahl > 1:
            print(f"Du hast {KaufAnzahl} {Plural.capitalize()} gekauft! (Restliche Münzen: {Münzen})")
        else:
            print(f"Du hast {KaufAnzahl} {WahlTiere.capitalize()} gekauft! (Restliche Münzen: {Münzen})")
            Tier_Anzahl += KaufAnzahl
        time.sleep(3)
        Tier_Menü()
    else:
        print("Du hast nicht genug Münzen!")
        print(f"Du brauchst {Tier_Dictionary[WahlTiere].Preis * KaufAnzahl - Münzen} Münzen mehr.")
        time.sleep(3)
        Tier_Menü()
    
  
  
  
  
def Tier_Menü():
    global Münzen, WahlTiere, Tier_Dictionary, Plural
    
    print("\n-----------------------------------------------------------------------")
    WahlTiere = input(f"Welches Tier möchtest du kaufen?\nDu hast {Münzen} Münzen\n1. Hühner 🐔 ({Tier_Dictionary["Huhn"].Preis} Münzen)\n2. Kühe 🐄 ({Tier_Dictionary["Kuh"].Preis} Münzen)\n3. Schafe 🐑 ({Tier_Dictionary["Schaf"].Preis} Münzen)\n4. Ziegen 🐐 ({Tier_Dictionary["Ziege"].Preis} Münzen)\n5. Zurück ↩️\n").lower().strip()

    if WahlTiere in ["1", "huhn"]:    
        WahlTiere = "Huhn"
        Plural = "Hühner"
        KaufprozessTiere()
    elif WahlTiere in ["2", "kuh"]:
        WahlTiere = "Kuh"
        Plural = "Kühe"
        KaufprozessTiere()
    elif WahlTiere in ["3", "schaf"]:
        WahlTiere = "Schaf"
        Plural = "Schafe"
        KaufprozessTiere()
    elif WahlTiere in ["4", "ziege"]:
        WahlTiere = "Ziege"
        Plural = "Ziegen"
        KaufprozessTiere()
    elif WahlTiere in ["5", "zurück"]:
        Hauptmenü()

    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        time.sleep(2)
        Tier_Menü()


def Ernte():
    global Ertrag, Münzen, Pflanzen_Dictionary, Tier_Dictionary, Lager_Dictionary, Arbeiter_Dictionary, Tiermultiplikator, Pflanzenmultiplikator, WetterPflanze_Faktor, WetterTier_Faktor, Rezepte_Dictionary


    gärtner = Arbeiter_Dictionary["Gärtner"]
    boost = 1 + gärtner.Boost * gärtner.Anzahl

    for pflanze in Pflanzen_Dictionary.values():
        ertrag = pflanze.Ernte_Faktor * pflanze.Anzahl * Pflanzenmultiplikator * WetterPflanze_Faktor * boost
        Lager_Dictionary[pflanze.Produkt].Anzahl += round(ertrag)



    Autoproduktion = [
        produkt for produkt, items in Rezepte_Dictionary.items()
        if items.Automatisch > 0
    ]

    if Autoproduktion:
        for produkt in Autoproduktion:
            rezept = Rezepte_Dictionary[produkt]
            anzahl = rezept.Automatisch

            print(f"🛠️ {produkt} ({anzahl}x)\n")

            zutaten_verfügbar = True
            zutaten_zum_abziehen = []


            
            for zutat in rezept.Zutaten:
                if isinstance(zutat, list):
                    gefunden = False
                    for alternative in zutat:
                        if alternative in Lager_Dictionary and Lager_Dictionary[alternative].Anzahl >= anzahl:
                            zutaten_zum_abziehen.append((alternative, anzahl))
                            gefunden = True
                            break
                    if not gefunden:
                        zutaten_verfügbar = False
                        break
                else:
                    
                    if zutat in Lager_Dictionary and Lager_Dictionary[zutat].Anzahl >= anzahl:
                        
                        zutaten_zum_abziehen.append((zutat, anzahl))
                    else:
                        zutaten_verfügbar = False
                        break

            if zutaten_verfügbar:
                for name, menge in zutaten_zum_abziehen:
                    print(name, menge)
                    Lager_Dictionary[name].Anzahl -= menge
                    Lager_Dictionary[produkt].Anzahl += anzahl
                print(f"{produkt} produziert: {anzahl}x.")
                
            else:
                print(f"{produkt} übersprungen - Zutaten fehlen.")
        time.sleep(3)


        


    for tier in Tier_Dictionary.values():
        ertrag = tier.Ernte_Faktor * tier.Anzahl * Tiermultiplikator * WetterTier_Faktor
        if isinstance(tier.Produkt, list):
            for produkt in tier.Produkt:
                Lager_Dictionary[produkt].Anzahl += round(ertrag / len(tier.Produkt))
        else:
            Lager_Dictionary[tier.Produkt].Anzahl += round(ertrag)



    
class Upgrade():
    def __init__(self,nameUP,Upgrade,TourF,Wert):
        self.nameUP = nameUP
        self.Upgrade = Upgrade
        self.TourF = TourF
        self.Wert = Wert
    @property
    def price(self):
        return round(self.Wert * (self.Upgrade + 1) ** 1.5)

class Anlagen(Upgrade):
    def __init__(self, name, Wert, anzahl, upgrade: Upgrade):
        self.name = name
        self.Wert = Wert
        self.anzahl = anzahl
        self.upgrade = upgrade
    @property
    def price(self):
        return round(self.Wert * (self.anzahl + 1) ** 1.5)

Upgrade_Dic0 = {
    0 : Upgrade("Base",0,1.0,0),
    1 : Upgrade("Easy",1,1.2,0),
    2 : Upgrade("Beginner",2,1.4,0),
    3 : Upgrade("Intermediate",3,1.6,0),
    4 : Upgrade("Hardcore",4,1.8,0),
    5 : Upgrade("Fallen",5,2,0)
}
Upgrade_Dic1 = {
    0 : Upgrade("Base",0,1,0),
    1 : Upgrade("Easy",1,1.2,0),
    2 : Upgrade("Beginner",2,1.4,0),
    3 : Upgrade("Intermediate",3,1.6,0),
    4 : Upgrade("Hardcore",4,1.8,0),
    5 : Upgrade("Fallen",5,2,0)
}

Upgrade_Dic2 = {
    0 : Upgrade("Base",0,1,0),
    1 : Upgrade("Easy",1,1.2,0),
    2 : Upgrade("Beginner",2,1.4,0),
    3 : Upgrade("Intermediate",3,1.6,0),
    4 : Upgrade("Hardcore",4,1.8,0),
    5 : Upgrade("Fallen",5,2,0)
}

Anlagen_Dic = {
    "Streichelzoo" : Anlagen("Streichelzoo",0,0,Upgrade_Dic0[0]),
    "Restaurant" : Anlagen("Restaurant",0,0,Upgrade_Dic1[0]),
    "Souvenir_Laden" : Anlagen("Souvenir_Laden",0,0,Upgrade_Dic2[0])
}

ListAnlagen = []
ListName = [Anlagen_Dic["Streichelzoo"].name,Anlagen_Dic["Restaurant"].name,Anlagen_Dic["Souvenir_Laden"].name]


def Anlagen_f():
    if len(ListAnlagen)!=0:
        print(f"Du hast bereits die Anlagen freigeschaltet:{'\n '.join(map(str, ListAnlagen))}")
    An_input = input("\n\n\n\n\n\n\n\n\n\nWas möchtest du machen?\n\n1. Ansehen\n\n2. Kaufen\n\n3. Hauptmenü\n").lower().strip()
    if An_input in ["1", "ansehen"]:
        Ansehen()
    elif An_input in ["2", "kaufen"]:
        KaufenMenü()
    elif An_input in ["3", "hauptmenü"]:
        Hauptmenü()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        time.sleep(2)
        Anlagen_f()
ChoiceAn : str = ""

def kaufenAnlagen():
    global ListAnlagen, ListName
    Anlagen_Dic[ChoiceAn].anzahl += 1
    ListAnlagen.append(Anlagen_Dic[ChoiceAn].name)
    print(f"\n Du hast die Anlage gekauft : {Anlagen_Dic[ChoiceAn].name} 🎆")
    time.sleep(2)
    Anlagen_f()

def KaufenMenü():
    print("\n----------------- Anlagen kaufen --------------\n")
    global ListAnlagen, ListName
    
    if len(ListName) == len(ListAnlagen):
        print("Du hast alle möglichen Anlagen bereits gekauft. \n\n<<Enter>> um zurück zu gehen.")
        if input() == "":
            Anlagen_f()
        else:
            print("Ungültige Eingabe.")
            time.sleep(2)
            KaufenMenü()
    else:
        inputAn()

def upgrade(choice, upgrade_dict):
    global Münzen
    if choice not in Anlagen_Dic:
        print(f"Invalid choice: {choice}")
        return

    # Get the current upgrade level and upgrade object
    current_upgrade = Anlagen_Dic[choice].upgrade
    current_level = current_upgrade.Upgrade

    # Check if there is a next level in the upgrade dictionary
    if current_level + 1 not in upgrade_dict:
        print("No further upgrades available!")
        return

    next_upgrade = upgrade_dict[current_level + 1]

    # Check if the user has enough Münzen
    if Münzen < next_upgrade.price:
        print(f"Du hast nicht genug Münzen (es fehlen {next_upgrade.price - Münzen} Münzen)")
        return

    # Apply the upgrade and deduct Münzen
    Anlagen_Dic[choice].upgrade = next_upgrade
    Münzen -= next_upgrade.price

    print(f"\nDein momentanes Upgrade Level ist {next_upgrade.Upgrade} : {next_upgrade.nameUP}")
    print(f"\nDu hast das Upgrade {next_upgrade.nameUP} gekauft für {next_upgrade.price} Münzen")

    time.sleep(3)
    Hauptmenü()



def upgrade0():
    upgrade("Streichelzoo", Upgrade_Dic0)

def upgrade1():
    upgrade("Restaurant", Upgrade_Dic1)

def upgrade2():
    upgrade("Souvenir_Laden", Upgrade_Dic2)
    

def ChoiceInput(): 
    global ChoiceAn
    if Anlagen_Dic[ChoiceAn].anzahl == 1:
            print("Du hast diese Anlange bereits gekauft.")
            inputQ = input("\n\nWas möchtest du tun\n\n1. Upgrade\n\n2. Zurück\n").lower().strip()
            if inputQ in ["1", "upgrade"]:
                if ChoiceAn == "Streichelzoo":
                    print("ChoiceAn:", ChoiceAn)     
                    upgrade0()
                    
                if ChoiceAn == "Restaurant":
                    upgrade1()
                    
                    
                if ChoiceAn == "Souvenir_Laden":
                    upgrade2()
                    
            if inputQ in ["2", "zurück"]:
                inputAn()
            else:
                time.sleep(2)
                Hauptmenü()
    else:
        kaufenAnlagen()

def inputAn():
    global ChoiceAn, ListName
    u_input = input(f"Was möchtest du kaufen?\n\n1. Streichelzoo ({Anlagen_Dic['Streichelzoo'].price} Münzen)🐐\n\n2. Restaurant ({Anlagen_Dic['Restaurant'].price} Münzen)🍴\n\n3. Souvenir_Laden ({Anlagen_Dic['Souvenir_Laden'].price} Münzen)🛍️\n\n4. Hauptmenü \n").lower().strip()
    if u_input in ["1", "streichelzoo"]:
        ChoiceAn = "Streichelzoo"
        ChoiceInput()
    elif u_input in ["2", "restaurant"]:
        ChoiceAn = "Restaurant"
        ChoiceInput()
    elif u_input in ["3", "souvenir_laden"]:
        ChoiceAn = "Souvenir_Laden"
        ChoiceInput()
    elif u_input in ["4", "hauptmenü"]:
        Hauptmenü()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        time.sleep(2)
        inputAn()

    
def Ansehen():
    print("\n\n\n\n\n\n\n\n\n\n\n---------------- Liste Anlagen ---------------\n\n\n")

    print("Du hast folgende Anlagen gekauft:")
    for i, name in enumerate(ListAnlagen, 1):
        item = Anlagen_Dic[name]
        print(f"{i}. {name} : Preis: {item.price} Münzen")
        print(f"Upgrade Level: {item.upgrade.Upgrade} : {item.upgrade.nameUP}")
        print(f"Touristenfaktor: {item.upgrade.TourF}")
    if input() == "":
        Anlagen_f()   
    
    
    
    
    

def Infrastruktur():
    global Münzen, Energieproduktion, Infrastruktur_Dictionary, Wasserproduktion
    Antwort_Infrastruktur = input(f"\n\n\n\n\nWas möchtest du kaufen?\nDu hast {Münzen} Münzen.\n1. Stromgenerator (+{Infrastruktur_Dictionary["Stromgenerator"].Leistung}W, {Infrastruktur_Dictionary["Stromgenerator"].Preis} Münzen)⚡\n2. Wassertank (+{Infrastruktur_Dictionary["Wassertank"].Leistung}L, {Infrastruktur_Dictionary["Wassertank"].Preis}Münzen)💧\n3. Arbeiter 👨‍🌾\n\n").lower().strip()
    if Antwort_Infrastruktur in ["1", "Stromgenerator"]:
        Infrastruktur_Name = "Stromgenerator"
    elif Antwort_Infrastruktur in ["2", "wassertank"]:
        Infrastruktur_Name = "Wassertank"
    elif Antwort_Infrastruktur in ["3", "arbeiter"]:
        Arbeiter_kaufen()
        time.sleep(3)
        Hauptmenü()
    else:
        print("Ungültige Eingabe. Versuch es nochmal.")
        return

    if Münzen >= Infrastruktur_Dictionary[Infrastruktur_Name].Preis:
        Münzen -= Infrastruktur_Dictionary[Infrastruktur_Name].Preis
        Infrastruktur_Dictionary[Infrastruktur_Name].Anzahl += 1
        Energieproduktion = Infrastruktur_Dictionary["Stromgenerator"].Anzahl * 50
        Wasserproduktion = Infrastruktur_Dictionary["Wassertank"].Anzahl * 100
        print(f"Du hast 1 {Infrastruktur_Name.replace('_', ' ').capitalize()} gekauft")
    else:
        print(f"Nicht genug Münzen! Du brauchst {Infrastruktur_Dictionary[Infrastruktur_Name].Preis - Münzen} Münzen mehr.")




def Runden_wählen():
    global Runden
    while True:
        try:
            Runden = int(input("\n\n\n\n\n\nWie viele Runden möchtest du spielen?\n\n\n\n\n\n"))
            if Runden > 0:
                time.sleep(1)
                print("\n\n\n\nSpiel Beginnt...\n\n\n\n\n\n")
                time.sleep(2)
                break
            else:
                raise ValueError("Die Anzahl der Runden muss größer als 0 sein.")
        except ValueError as e:
            print(f"Ungültige Eingabe: {e}. Bitte eine positive ganze Zahl eingeben.")

def gespielte_Runden():
    global Runden, Wochenzähler
    while True:
        Rundenzähler = 1
        if Wochenzähler == 50:
            print("Die Runde ist vorbei!")
            Runden -= 1
            if Runden == 0:
                print("Das Spiel ist vorbei!\n\nDanke fürs Spielen!\n\nViel Glück beim nächsten Mal! 🍀")
                break
            else:
                Rundenzähler += 1
                print(f"Runde {Rundenzähler} beginnt... 🌃")
                time.sleep(5)
                break
        else:
            break




def Neue_Woche():
    global Wochenzähler, Schon_geerntet, Ertrag, Heute_geerntet, Wasser, Wasserproduktion, Aktueller_Wasserverbrauch, Tier_Dictionary, Pflanzen_Dictionary, Tierfutter_Dictionary, Lager_Dictionary, Infrastruktur_Dictionary, Energieproduktion, Energie_verbraucht, Aktueller_Wasserverbrauch, Ernte_Faktor, WetterPflanze_Faktor, WetterTier_Faktor, Runden, Ernte_Faktor, Arbeiter_Dictionary
    Ernte()
    gespielte_Runden()
    Wochenzähler += 1
    if Wasser <= 0:
        print("Du hast zu wenig Wasser! 💧\nBau einen neuen Wassertank! 🫙")

        while Aktueller_Wasserverbrauch > Wasserproduktion:

            pflanzen_mit_anzahl = [p for p in Pflanzen_Dictionary if Pflanzen_Dictionary[p].Anzahl > 0]

            if pflanzen_mit_anzahl:
                zufällige_pflanze = random.choice(pflanzen_mit_anzahl)
                pflanze = Pflanzen_Dictionary[zufällige_pflanze]
                pflanze.Anzahl -= 1
                Aktueller_Wasserverbrauch -= pflanze.Wasserverbrauch
                print(f"1 {zufällige_pflanze} ist deshalb abgestorben.")
            else:
                tiere_mit_anzahl = [t for t in Tier_Dictionary if Tier_Dictionary[t].Anzahl > 0]

                if tiere_mit_anzahl:
                    zufälliges_tier = random.choice(tiere_mit_anzahl)
                    tier = Tier_Dictionary[zufälliges_tier]
                    tier.Anzahl -= 1
                    Aktueller_Wasserverbrauch -= tier.Wasserverbrauch
                    print(f"1 {zufälliges_tier} ist deshalb gestorben.")
                else:
                    print("Du hast keine Pflanzen oder Tiere die sterben können.")
                    break
        time.sleep(2)
    
    if Lager_Dictionary["Tierfutter"].Anzahl <= 0 and Tierfutter_Dictionary["Tierfutter"].Verbrauch > 0:
        
        print("Du hast kein Tierfutter mehr! 🐄\nStelle mehr Tierfutter her! 🛠️")
        Futterverbrauch = Tierfutter_Dictionary["Tierfutter"].Verbrauch
        Futterproduktion = Tierfutter_Dictionary["Tierfutter"].Produktion

        gestorbene_tiere = {}

        while Futterverbrauch > Futterproduktion:
            tiere_mit_anzahl = [t for t in Tier_Dictionary if Tier_Dictionary[t].Anzahl > 0]
        
            if tiere_mit_anzahl:
                zufälliges_tier = random.choice(tiere_mit_anzahl)
                tier = Tier_Dictionary[zufälliges_tier]
                tier.Anzahl -= 1
                Aktueller_Wasserverbrauch -= tier.Wasserverbrauch
                Futterverbrauch -= tier.Tierfutter


                if zufälliges_tier in gestorbene_tiere:
                    gestorbene_tiere[zufälliges_tier] += 1
                else:
                    gestorbene_tiere[zufälliges_tier] = 1

            else:
                print("Alle Tiere sind verhungert... 😢")
                break


        if gestorbene_tiere:
            print("Folgende Tiere sind gestorben:")
            for tiername, anzahl in gestorbene_tiere.items():
                print(f"- {anzahl} {tiername}{'n' if anzahl > 1 else ''}")
            time.sleep(2)
            
        

        
    Lohn_ausgabe()
    print(f"Starte Woche {Wochenzähler}... 🌞\n\n\n")
    time.sleep(3)
    wetter_wechsel()
    Random_event()
    print("\n\n")
    time.sleep(4)
    Hauptmenü()



def zähle_Woche():
    print(f"\n\n\nHeute ist dein {Wochenzähler}. Woche.\n\n\n-----------------------------------------------------------------------")

def Hauptmenü():
    global Münzen, WetterPflanze_Faktor, WetterTier_Faktor, NW, Energie_verbraucht, Energieproduktion, Wasserproduktion, Wasser, Tierfutter, Tierfutter_Dictionary
    print(f"\n\n\n\n\n>>>>>> Hauptmenü <<<<<<".ljust(36) + f"Wetter für diese Woche: {NW.name}")
    print(f"1. Stats 📜".ljust(30) + f"Pflanzenfaktor: {PrintPflanzenFaktor}")
    print(f"2. Pflanzen 🌱".ljust(30) + f"Tierfaktor: {PrintTierFaktor}")
    print(f"3. Tiere 🐎\n4. Infrastruktur ⚡💧\n5. Verarbeitung 🛠️\n6. Sonntagsschlaf 🌙\n7. Garage 🚜")
    print(f"8. Lager 🛖".ljust(60) +     f"|Stromverbrauch:      {Energie_verbraucht}/{Energieproduktion}W")
    print(f"9. Anlagen 🏭".ljust(59) +   f"|Wasserproduktion:    {Wasserproduktion}L/Woche  (Total: {Wasser}L)")
    print(f"0. Verlassen 👋".ljust(59) + f"|Tierfutterverbrauch: {Tierfutter_Dictionary["Tierfutter"].Verbrauch}/{Tierfutter_Dictionary['Tierfutter'].Produktion}  (Total: {Tierfutter.Anzahl})")
    Antwort_Hauptmenü = input("").strip().lower()
    if Antwort_Hauptmenü in ["1", "stats"]:
        Stats()
    elif Antwort_Hauptmenü in ["2", "pflanzen"]:
        Pflanzenart()
        time.sleep(3)
        Hauptmenü()
    elif Antwort_Hauptmenü in ["3", "tiere"]:
        Tier_Menü()
        time.sleep(3)
        Hauptmenü()
    elif Antwort_Hauptmenü in ["4", "infrastruktur"]:
        Infrastruktur()
        time.sleep(3)
        Hauptmenü()
    elif Antwort_Hauptmenü in ["5", "verarbeitung"]:
        Verarbeitung()
        time.sleep(3)
        Hauptmenü()
    elif Antwort_Hauptmenü in ["6", "schlafen"]:
        Schlaf_Animation()
        Neue_Woche()
        time.sleep(3)
    elif Antwort_Hauptmenü in ["7", "garage"]:
        Garage()
        time.sleep(3)
        Hauptmenü()
    elif Antwort_Hauptmenü in ["8", "lager"]:
        Lager_Menü()
        time.sleep(3)
        Hauptmenü()
        
    elif Antwort_Hauptmenü.startswith("/give player coins"):
        teile = Antwort_Hauptmenü.split()
        if len(teile) == 4:
            try:
                betrag = int(teile[3])
                Münzen += betrag
                print(f"{betrag} Münzen gegeben. Neuer Stand: {Münzen}")
            except ValueError:
                print("Ungültiger Betrag!")
        Hauptmenü()
    
    elif Antwort_Hauptmenü in ["9", "anlagen"]:
        Anlagen_f()
        time.sleep(3)
        Hauptmenü

    
    elif Antwort_Hauptmenü in ["0", "verlassen", "exit"]:
        print("Tschüss, Farmer! 👋")
        pygame.mixer.music.stop()

    
    else:
        print("Ungültige Aktion. Versuch es nochmal!")
        time.sleep(2)
        Hauptmenü()


Spielstart = False
try:
    Antwort1 = input("\n\n\n\n\nMöchtest du ein neues Spiel starten?\n1. Ja\n2. Nein\n\n\n\n").strip().lower()

    if Antwort1 in ["1", "ja"]:
        print("Du hast 'Ja' ausgewählt.\n\n\n\n\n\n\n\n\n Herzlich Willkommen bei 'Solo Leveling My Farm'!\n\n\n")
        time.sleep(5)
        Spielstart = True
    elif Antwort1 in ["2", "nein"]:
        print("Du hast 'Nein' ausgewählt.")
    else:
        print("Error. Versuch es nochmal.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

if Spielstart:
    Spiele_Musik()
    print("\n\n\n\n\n\n\nStarte neues Spiel...\n\n\n\n\n\n\n")
    time.sleep(2)
    Runden_wählen()
    Tutorial()
else:
    print("Kein Spiel wurde gestartet.")

