import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.task_manager import *
from src.file_handler import *
from src.display import *

def main() :

    taches = loadTaches()

    while True :
        afficherMenu()

        choix = input("Choisissez une option (1-9): ").strip()

        if choix == '1' :
            afficherTaches(taches,"📋 Toutes les tâches")

        elif choix == '2' :
            description = input("Description de la tâche : ").strip()
            if description : 
                priorite_entree = input("Priorité (1-basse, 2-moyenne, 3-haute) : ").strip()
                priorite = int(priorite_entree) if priorite_entree.isdigit() else 3
                taches = ajouterTache(taches, description, priorite)
                sauvegarderTaches(taches)
                print("✅ Tâche ajoutée avec succès.")
                
        elif choix == '3' :
            afficherTaches(taches,"Sélectionner une tâche à marquer comme terminée")
            try : 
                id_tache = int(input("ID de la tâche à marquer comme terminée : "))
                taches = terminerTache(taches, id_tache)
                sauvegarderTaches(taches)
                print("✅ Tâche marquée comme terminée.")
            except ValueError :
                print("❌ ID invalide. Veuillez entrer un numéro de tâche valide.")
                
        elif choix == '4' :
            afficherTaches(taches,"Sélectionner une tâche à supprimer")
            try :
                id_tache = int(input("ID de la tâche à supprimer : "))
                taches = supprimerTache(taches, id_tache)
                sauvegarderTaches(taches)
                print("✅ Tâche supprimée avec succès.")
            except ValueError :
                print("❌ ID invalide. Veuillez entrer un numéro de tâche valide.")

        elif choix == '5' :
            taches_actives = filtreTache(taches, show_completed=False)
            afficherTaches(taches_actives,"📌 Tâches actives")

        elif choix == '6' :
            taches_terminees = filtreTache(taches, show_completed=True)
            afficherTaches(taches_terminees,"✅ Tâches terminées")

        elif choix == '7' :
            print("\n Trier par : ")
            print("  1. Priorité (haute -> basse)")
            print("  2. Priorité (basse -> haute)")
            print("  3. Date d'ajout (récentes -> anciennes)")
            print("  4. Date d'ajout (anciennes -> récentes)")
            choix = input("Chosissez une option (1-4): ")

            if choix == '1' :
                taches = trierTaches(taches, critere='priorite', reverse=True)
            elif choix == '2' :
                taches = trierTaches(taches, critere='priorite', reverse=False)
            elif choix == '3' :
                taches = trierTaches(taches, critere='date', reverse=True)
            elif choix == '4' :
                taches = trierTaches(taches, critere='date', reverse=False)
            else :
                print("Option invalide, veuillez réessayer.")
                continue
            sauvegarderTaches(taches)
            print("✅ Tâches triées avec succès.")

        elif choix == '8' :
            if exporterTachesCsv(taches) :
                print("✅ Tâches exportées avec succès !")
            else :
                print("❌ Échec de l'exportation des tâches.")

        elif choix == '9' :
            print("Au revoir ! 👋")
            break
        else :
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__" :
    main()