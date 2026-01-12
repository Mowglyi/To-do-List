"""
Gestion de l'affichage dans la console.
"""

from typing import List, Dict

def afficherTaches(taches: List[Dict], titre: str ="Mes tâches") :
    """Affiche une liste de tâches formatée dans la console."""
    if not taches :
        print(f"\n 📭 {titre}")
        print(" Aucune tâche à afficher.\n")
        return
    print(f"\n 📋 {titre} :")
    print("=" * 50)

    for tache in taches :
        statut = "✓" if tache['terminee'] else "✗"
        priorite = tache.get("priorite", "🟢 Basse")
        print(f"[{statut}] {tache['description']} ({priorite})")
        print(f"    ID: {tache['id']} | Ajoutée le: {tache['date_ajout'][:10]}")
        if tache['terminee'] :
            print(f"   ✓ Terminée le: {tache.get('terminee_a','')[0:10]}")
    print()

def afficherMenu() :
    """Affiche le menu principal dans la console."""
    menu = """
╔══════════════════════════════════════╗
║          📝 TO-DO LIST MANAGER       ║
╠══════════════════════════════════════╣
║ 1. Voir toutes les tâches           ║
║ 2. Ajouter une tâche                ║
║ 3. Terminer une tâche               ║
║ 4. Supprimer une tâche              ║
║ 5. Voir les tâches actives          ║
║ 6. Voir les tâches terminées        ║
║ 7. Trier les tâches                 ║
║ 8. Exporter en CSV                  ║
║ 9. Quitter                          ║
╚══════════════════════════════════════╝
"""
    print(menu)