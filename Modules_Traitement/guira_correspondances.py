import geopandas as gpd
import pandas as pd

from numpy import NaN, sort



countries = gpd.read_file('./data/map').loc[:,['geometry','ADM0_A3','NAME']]

noc_region = pd.read_csv('./data/noc_region.csv')


# Remplir données manquantes :
noc_region.loc[168,'reg'] = 'Refugee Olympic Team'
noc_region.loc[208,'reg'] = 'Tuvalu'
noc_region.loc[213,'reg'] = 'Unknown'

# Initialisation
correspondances = pd.DataFrame(columns = ['noc','ADM0_A3'])

## correspondance directe : NOC == ADM0_A3

missing1 = []

for noc in noc_region.noc_region.values :
    if not noc in countries.ADM0_A3.values :
        missing1.append(noc)
    else :
        ADM0 = countries[countries.ADM0_A3 == noc].ADM0_A3.values[0]
        correspondances.loc[len(correspondances.index)] = [noc,ADM0]


## correspondance par les noms

missing2 = []

for noc in missing1:
    name = noc_region.reg[noc_region.noc_region==noc].values[0]
    if not name in countries.NAME.values :
        missing2.append(noc)
    else :
        ADM0 = countries[countries.NAME == name].ADM0_A3.values[0]
        correspondances.loc[len(correspondances.index)] = [noc,ADM0]


## mise en correspondance 'à la main' pour les pays restants

for noc in missing2:
    name = noc_region.reg[noc_region.noc_region==noc].values[0]
    print(name)

print(sort(countries.NAME.unique()))

equivalent_names = {'Individual Olympic Athletes' : NaN
                    'Refugee Olympic Team' : NaN
                    'Unknown' : NaN
                    'Czech Republic' : 'Czechia'
                    'Republic of Congo' : 'Dem. Rep. Congo'
                    'South Sudan' : 'S. Sudan'
                    }



# """
#
# Curacao
# Andorra
# Antigua
# Aruba
# American Samoa
# Barbados
# Bermuda
#
# Cayman Islands
#
# Cook Island
# Comoros
# Cape Verde
# Dominica
# Micronesia
# Equatorial Guinea
# Grenada
# Guam
#
# Virgin Islands, US
# Virgin Islands, British
# Kiribati
# Saint Lucia
# Liechtenstein
# Maldives
# Marshall Islands
# Malta
# Monaco
# Mauritius
# Nauru
# Palau
#
# Samoa
# Seychelles
# Singapore
# Saint Kitts
# San Marino
#
# Sao Tome and Principe
# Czech Republic
# Tonga
# Tuvalu
#
# Saint Vincent
# Trinidad
# """
