import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET

# Globale Variable für den aktuellen Speicherort der Textdatei und XML-Datei
current_output_path = ""
current_xml_path = ""

# Funktion zum Extrahieren der Datentypen aus der XML-Datei und Speichern in einer Textdatei
def extract_data_types():
    global current_output_path, current_xml_path  # Zugriff auf die globalen Variablen

    if not current_output_path:
        print("Bitte wählen Sie zuerst einen Speicherort für die Textdatei aus.")
        return

    if not current_xml_path:
        print("Bitte wählen Sie zuerst eine XML-Datei aus.")
        return

    try:
        # Parsen der XML-Datei
        tree = ET.parse(current_xml_path)
        root = tree.getroot()

        # Extrahieren der Datentypen
        data_types = set()
        for element in root.iter():
            data_types.add(element.tag)

        # Speichern der Datentypen in der Textdatei am ausgewählten Speicherort
        with open(current_output_path, "w") as f:
            f.write(" ".join(data_types))

        print(f"Datentypen erfolgreich extrahiert und in {current_output_path} gespeichert.")

    except ET.ParseError:
        print("Fehler beim Parsen der XML-Datei.")
    except Exception as e:
        print(f"Fehler: {e}")

# Funktion zum Ändern des Speicherorts für die Textdatei
def change_output_path():
    global current_output_path
    new_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    if new_path:
        current_output_path = new_path
        print(f"Speicherort für Textdatei geändert: {current_output_path}")

# Funktion zum Auswählen der XML-Datei
def select_xml_file():
    global current_xml_path
    xml_path = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])

    if xml_path:
        current_xml_path = xml_path
        print(f"Ausgewählte XML-Datei: {current_xml_path}")

# GUI erstellen
root = tk.Tk()
root.title("XML Datentypen Extractor")

# Schaltfläche zum Ändern des Speicherorts
change_path_button = tk.Button(root, text="Speicherort ändern", command=change_output_path)
change_path_button.pack(pady=10)

# Schaltfläche zum Auswählen der XML-Datei
select_xml_button = tk.Button(root, text="XML-Datei auswählen", command=select_xml_file)
select_xml_button.pack(pady=10)

# Schaltfläche zum Auswählen der XML-Datei und Extrahieren der Datentypen
extract_button = tk.Button(root, text="Datentypen extrahieren", command=extract_data_types)
extract_button.pack(pady=10)

root.mainloop()
