"""Gestion de la persistance des données"""

import json
import os
import typing import List, Dict

def loadTaches(filename: str ="data/taches.json") -> List[Dict] :
    """Charge les tâches depuis un fichier JSON."""
    try :
        if os.path.exists(filename) :
            with open(filename, 'r', encoding='utf-8') as f :
                return json.load(f)
    except (json.JSONDecodeError, IOError) :
        print("❌ Erreur lors du chargement des tâches.")
    return []

def sauvegarderTaches(taches: List[Dict], filename: str ="data/taches.json") -> bool :
    """Sauvegarde les tâches dans un fichier JSON."""
    try :
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f :
            json.dump(taches, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e :
        print(f"❌ Erreur lors de la sauvegarde des tâches : {e}")
        return False

def exporterTachesCSV(taches: List[Dict], filename: str ="data/taches_export.csv") -> bool :
    """Exporte les tâches dans un fichier CSV."""
    try :
        import csv
        with open(filename, 'w', newline='', encoding='utf-8') as f :
            if taches :
                writer = csv.DictWriter(f, fieldnames=taches[0].keys())
                writer.writeheader()
                writer.writerows(taches)
        return True
    except IOError as e :
        print(f"❌ Erreur lors de l'exportation CSV des tâches : {e}")
        return False
