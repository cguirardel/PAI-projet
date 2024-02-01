"""
Fichier contenant tous les tests du projet avec les exigences correspondantes
Modules testés: 
"""
from Modules_Traitement.traitementV11012024 import olympics, countries, correspondances, WINTER, SUMMER, ALL_SEASON
import Modules_Traitement.traitementV11012024

def main():
    print('Groupe de tests organisés selon la table des spécifications\n')
    
    print('Exigence 1.1: Comptage du nombre de médaille par pays sur la carte:')
    res = Modules_Traitement.traitementV11012024.constructionCarte(olympics, countries, 1994, 2020, edition = ALL_SEASON)
    print(res)
    print('Exigence 1.1: La carte s\'affiche bien dans la fenêtre dédiée et se met à jour')
    print('Exigence 1.2: Extraction d\'un tableau DataFrame des médailles du dataset:')
    resultat = Modules_Traitement.traitementV11012024.compteMedailles(olympics, 'NOC', 1996, 2012, medal_type='All', edition = ALL_SEASON, sort = False)
    print(resultat)
    
    print('\nExigence 2.2: Extraction d\'un sous DataFrame correspondant à la recherche passée en argument')
    data = Modules_Traitement.traitementV11012024.recherche(olympics, 1994, 2020, edition = ALL_SEASON, nameValue='B.lt', sportValue='Athl')
    print(data)
    
    print('\nExigence 3.2: Extraction d\'un DataFrame du nombre de médailles par âge:')
    resultat = Modules_Traitement.traitementV11012024.compteMedailles(olympics, 'Age', 1996, 2012, medal_type='All', edition = ALL_SEASON, sort = False)
    print(resultat)

    print('\nGroupe d\'exigences 4 test: faire tourner l\'affichage')
    
if __name__=="__main__":
    main()