from datetime import datetime
from typing import List, Dict

def creer_tache(description : str, priorite : int=3) -> Dict:
    """Crée une nouvelle tâche avec la description, la priorité et la date actuelle."""
    priority_map = {1: "🔴 Haute", 2: "🟡 Moyenne", 3: "🟢 Basse"}

    return {
        'id': int(datetime.now().timestamp()),  # ID basé sur le timestamp actuel en millisecondes
        'description': description,
        'priorite': priority_map.get(priorite, "🟢 Basse"),
        'terminee': False,
        'date_ajout': datetime.now().isoformat()
        'terminee_a' : None
    }

def ajouterTache(taches : List[Dict], description : str, priorite : int=3) -> List[Dict]:
    """Ajoute une nouvelle tâche à la liste des tâches."""
    nouvelle_tache = creer_tache(description, priorite)
    taches.append(nouvelle_tache)
    return taches

def supprimerTache(taches : List[Dict], id_tache : int) -> List[Dict]:
    """Supprime une tâche de la liste en fonction de son ID."""
    taches = [tache for tache in taches if tache['id'] != id_tache]
    return taches

def terminerTache(taches : List[Dict], id_tache : int) -> List[Dict]:
    """Marque une tâche comme terminée en fonction de son ID."""
    for tache in taches:
        if tache['id'] == id_tache:
            tache['terminee'] = True
            tache['terminee_a'] = datetime.now().isoformat()
    return taches

def filtreTache(taches : List[Dict], show_completed : bool=False) -> List[Dict]:
    """Filtre les tâches en fonction de leur statut (terminée ou non)."""
    if show_completed:
        return [tache for tache in taches if tache['terminee']]
    return [tache for tache in taches if not tache['terminee']]

def trierTaches(taches : List[Dict], par : str = 'date', reverse: bool = False) -> List[Dict]:
    """Trie les tâches en fonction du critère spécifié (priorité ou date de création)."""
    if par == "priorite" :
        ordre_priorite = {"🔴 Haute": 1, "🟡 Moyenne": 2, "🟢 Basse": 3}
        return sorted(taches, key=lambda x:ordre_priorite.get(x['priorite"],4'], reverse))
    elif par == "date" : 
        return sorted(taches, key=lambda x: x['date_ajout'], reverse)
    return taches
