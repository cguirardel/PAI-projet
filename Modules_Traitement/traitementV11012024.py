"""
    objectif: Première version du traitement du programme/IHM visant à exploiter; traiter
et afficher des résultats sur le dataset suivant:
https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data/

    date: 18/11/2023 dernière mise à jour: 18/11/2023
    auteur: Gabriel Lecarme
"""

import numpy as np
import pandas
import geopandas as gpd

SUMMER = 1
WINTER = 2
ALL_SEASON = 0

olympics = pandas.read_csv("./data/dataset_olympics.csv")
noc = pandas.read_csv("./data/noc_region.csv")
countries = gpd.read_file('./data/map').loc[:,['geometry','ADM0_A3','NAME']]
correspondances = pandas.read_csv('./data/correspondances.csv')

lignes = olympics.index
columns = olympics.columns

def compteMedailles(df, category, start_year, end_year, medal_type = 'All', edition = ALL_SEASON, sort = False):
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

    df = df[~df.Medal.isna()] # Filtrage des lignes avec médaille
    if not(medal_type in ["Gold", "Silver", "Bronze", "All"]):
        raise ValueError('medal_type must be in ["Gold", "Silver", "Bronze", "All"]')
    if not(category in columns):
        raise ValueError('check your category')

    formatdf = df[(df.Year >= start_year) & (df.Year <= end_year)]  # Filtrage par période
    if edition != ALL_SEASON:
        season = ["Summer", "Winter"][edition - 1]
        formatdf = formatdf[df.Season == season] # Edition
    if medal_type != 'All':
        formatdf = formatdf.loc[df.Medal == medal_type] # Type de médaille

    compte = formatdf.loc[: ,[category, "Medal"]]
    dfgroupby = compte.groupby(category)    # Regroupement <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001A7E13A4D50>
    res = dfgroupby.count()   # Comptage
    if sort:
        res = res.sort_values('Medal', ascending = False) # Tri par nombre décroissant de médaille
    return res

def constructionCarte(df, gpd_df, start_year, end_year, edition = ALL_SEASON):
    """

        Parameters
        ----------
        df : TYPE
            DESCRIPTION.
        gpd_df : TYPE
            DESCRIPTION.
        start_year : TYPE
            DESCRIPTION.
        end_year : TYPE
            DESCRIPTION.
        edition : TYPE, optional
            DESCRIPTION. The default is ALL_SEASON.

        Returns
        -------
        None.

    """
    compte = compteMedailles(df, 'NOC', start_year, end_year, medal_type='All', edition = edition, sort = True)
    corres = compte.merge(correspondances, left_index=True, right_on='NOC', how='outer')
    dfgroupby = corres.groupby('ADM0_A3', dropna=False) # groupement par code ADM0 en gardant les pays qui ne font pas de médailles
    res = dfgroupby.sum(numeric_only=True) # somme des médailles et suppression de la colonne NOC
    res = pandas.merge(gpd_df, res, left_on='ADM0_A3', right_index=True, how='left') # Ajout de la colonne au GeoDataFrame
    return res

def main():
    resultat = compteMedailles(olympics, 'NOC', 1996, 2012, medal_type='All', edition = ALL_SEASON, sort = False)
    print(resultat)
    res = constructionCarte(olympics, countries,1994, 2020, edition = ALL_SEASON)
    print(res)

if __name__ == "__main__":
    main()