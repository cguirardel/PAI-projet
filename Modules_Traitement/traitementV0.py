"""
    objectif: Première version du traitement du programme/IHM visant à exploiter; traiter 
et afficher des résultats sur le dataset suivant: 
https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data/
    
    date: 18/11/2023 dernière mise à jour: 18/11/2023
    auteur: Gabriel Lecarme
"""
    
import numpy as np
import pandas

olympics = pandas.read_csv("./data/dataset_olympics.csv")
noc = pandas.read_csv("./data/noc_region.csv")

lignes = olympics.index
columns = olympics.columns

def compteMedailles(csv, start_year, end_year, medal_type = 'All', edition = 0):
    """_summary_

    Args:
        csv (_type_): _description_
        start_year (_type_): _description_
        end_year (_type_): _description_
        medal_type (str, optional): _description_. Defaults to 'All'.
        edition (int, optional): _description_. Defaults to 0.

    Raises:
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if not(medal_type in ["Gold", "Silver", "Bronze", "All"]):
        raise ValueError('medal_type must be in ["Gold", "Silver", "Bronze", "All"]')
    if not(edition in [0, 1, 2]):
        raise ValueError('edition must be an int = 0; 1 or 2')
    if medal_type == 'All':
        gold = compteMedailles(csv, start_year, end_year, 'Gold', edition)
        silver = compteMedailles(csv, start_year, end_year, medal_type = 'Silver', edition = edition)
        bronze = compteMedailles(csv, start_year, end_year, medal_type = 'Bronze', edition = edition)
        compte = gold + silver + bronze
    else:
        formatdf = csv.astype({'NOC' : 'category'}) # Permet de conserver les 'NOC' avec 0 médaille d'or
        formatdf = formatdf[(csv.Year >= start_year) & (csv.Year <= end_year)]  # Filtrage par période
        if edition != 0:
            season = ["Summer", "Winter"][edition - 1]
            formatdf = formatdf[csv.Season == season]
        compte = formatdf.loc[csv.Medal == medal_type, ["NOC", "Medal"]]   # Filtrage par médaille
        dfgroupby = compte.groupby('NOC')    # Regroupement <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001A7E13A4D50>
        compte = dfgroupby.count()   # Comptage
    compte = compte.sort_values('Medal', ascending = False) # Tri
    return compte

"""def compteMedaillesAR(csv, start_year, end_year, edition = 0):
    formatdf = csv.astype({'NOC' : 'category'})
    formatdf = formatdf[(csv.Year >= start_year) & (csv.Year <= end_year)]
    silver = formatdf.loc[csv.Medal == 'Silver', ['NOC', 'Medal']].groupby('NOC').count().sort_values('Medal', ascending = False)
    return silver"""

def main():
    res = compteMedailles(olympics, 2010, 2010, medal_type='Bronze', edition=2)    
    print(res.loc['GER'])
    
if __name__ == "__main__":
    main()
