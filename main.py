import os
import shutil

# 1. Wo wird was aufgeräumt?
# Findet automatisch Downloads-Ordner (egal ob Mac oder Windows)
download_ordner = os.path.join(os.path.expanduser("~"), "Downloads")

# 2. Dateiendungen zuordnen
erweiterungen = {
    "Bilder": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Excel_Tabellen": [".xlsx", ".xls", ".csv"],
    "PowerPoint": [".pptx", ".ppt"],
    "Textdokumente": [".docx", ".doc", ".pdf", ".txt"],  # PDF passt oft auch gut hier rein
    "Musik": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov", ".mkv"],
    "Archive": [".zip", ".rar", ".tar", ".gz"],
    "Installationen": [".exe", ".msi", ".dmg", ".pkg"],
    "Python_Code": [".py", ".ipynb"],
}

def sortiere_dateien():
    # Hier wird geprüft, ob der Ordner existiert
    if not os.path.exists(download_ordner):
        print(f"Fehler: Der Ordner {download_ordner} wurde nicht gefunden.")
        return

    print(f"Starte Sortierung in: {download_ordner}")
    
    # Zähler der Dateien 
    bewegte_dateien = 0

    # Alle Dateien im Ordner durchgehen
    for dateiname in os.listdir(download_ordner):
        original_pfad = os.path.join(download_ordner, dateiname)

        # Es werden ausschließlich Dateien verschoben
        if os.path.isfile(original_pfad):
            _, endung = os.path.splitext(dateiname)
            endung = endung.lower()

            # Richtigen Platz für die Datei finden
            verschoben = False
            for kategorie, endungen_liste in erweiterungen.items():
                if endung in endungen_liste:
                    ziel_ordner_pfad = os.path.join(download_ordner, kategorie)
                    
                    # Ordner erstellen, falls er nicht existiert
                    os.makedirs(ziel_ordner_pfad, exist_ok=True)

                    ziel_pfad = os.path.join(ziel_ordner_pfad, dateiname)
                    
                    # Verschieben (mit Fehlerbehandlung falls Datei schon existiert)
                    try:
                        shutil.move(original_pfad, ziel_pfad)
                        print(f"Verschoben: {dateiname} -> {kategorie}")
                        bewegte_dateien += 1
                        verschoben = True
                    except shutil.Error:
                        print(f"Datei existiert schon: {dateiname} - überspringe.")
                    
                    break
            
            if not verschoben:
                #Unbekannte Dateien ignorieren oder melden
                pass

    print(f"FERTIG! {bewegte_dateien} Dateien wurden sortiert.")

# Das Skript wird nur ausgeführt, wenn es direkt gestartet wird
if __name__ == "__main__":
    sortiere_dateien()