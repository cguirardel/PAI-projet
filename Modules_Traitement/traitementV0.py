"""
    objectif: Première version du traitement du programme/IHM visant à exploiter; traiter 
et afficher des résultats sur le dataset suivant: 
https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data/
    
    date: 18/11/2023 dernière mise à jour: 18/11/2023
    auteur: Gabriel Lecarme
"""
    
import numpy as np
import pandas

SUMMER = 1
WINTER = 2
ALL_SEASON = 0

olympics = pandas.read_csv("./data/dataset_olympics.csv")
noc = pandas.read_csv("./data/noc_region.csv")

lignes = olympics.index
columns = olympics.columns

def compteMedaillesPays(df, start_year, end_year, medal_type = 'All', edition = ALL_SEASON):
    """_summary_

    Args:
        df (_type_): _description_
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

    # df = df[~df.Medal.isnan()]

    if not(medal_type in ["Gold", "Silver", "Bronze", "All"]):
        raise ValueError('medal_type must be in ["Gold", "Silver", "Bronze", "All"]')
    if medal_type == 'All':
        gold = compteMedaillesPays(df, start_year, end_year, 'Gold', edition)
        silver = compteMedaillesPays(df, start_year, end_year, medal_type = 'Silver', edition = edition)
        bronze = compteMedaillesPays(df, start_year, end_year, medal_type = 'Bronze', edition = edition)
        compte = gold + silver + bronze
    else:
        formatdf = df.astype({'NOC' : 'category'}) # Permet de conserver les 'NOC' avec 0 médaille d'or
        formatdf = formatdf[(df.Year >= start_year) & (df.Year <= end_year)]  # Filtrage par période
        if edition != ALL_SEASON:
            season = ["Summer", "Winter"][edition - 1]
            formatdf = formatdf[df.Season == season]
        compte = formatdf.loc[df.Medal == medal_type, ["NOC", "Medal"]]   # Filtrage par médaille
        dfgroupby = compte.groupby('NOC')    # Regroupement <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001A7E13A4D50>
        compte = dfgroupby.count()   # Comptage
    compte = compte.sort_values('Medal', ascending = False) # Tri
    return compte

"""def compteMedaillesAR(csv, start_year, end_year, edition = 0):
    formatdf = csv.astype({'NOC' : 'category'})
    formatdf = formatdf[(csv.Year >= start_year) & (csv.Year <= end_year)]
    silver = formatdf.loc[csv.Medal == 'Silver', ['NOC', 'Medal']].groupby('NOC').count().sort_values('Medal', ascending = False)
    return silver"""
    
def compteMedaillesAge(df, start_year, end_year, medal_type = 'All', edition = ALL_SEASON):
    if not(medal_type in ["Gold", "Silver", "Bronze", "All"]):
        raise ValueError('medal_type must be in ["Gold", "Silver", "Bronze", "All"]')
    if medal_type == 'All':
        gold = compteMedaillesAge(df, start_year, end_year, 'Gold', edition)
        silver = compteMedaillesAge(df, start_year, end_year, medal_type = 'Silver', edition = edition)
        bronze = compteMedaillesAge(df, start_year, end_year, medal_type = 'Bronze', edition = edition)
        compte = gold + silver + bronze
    else:
        formatdf = df[(df.Year >= start_year) & (df.Year <= end_year)]
        if edition != ALL_SEASON:
            season = ["Summer", "Winter"][edition - 1]
            formatdf = formatdf[df.Season == season]
        compte = formatdf.loc[df.Medal == medal_type, ["Age", "Medal"]]
        dfgroupby = compte.groupby('Age')
        compte = dfgroupby.count()
    return compte

def main():
    res = compteMedaillesAge(olympics, 1896, 2010, edition = SUMMER)
    print(res)
    
if __name__ == "__main__":
    main()