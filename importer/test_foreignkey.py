# -*- coding: utf-8 -*-
"""Créé le Tue Jul  5 11:31:38 2022 par emilejetzer."""

import sqlalchemy as sqla
import pandas as pd
import numpy as np

from polygphys.outils.base_de_donnees import BaseTableau

nom, mdp = tuple(map(str.strip, open('nom.txt').read().strip().split('\n')))
adresse = 'mysql+pymysql://{nom}:{mdp}@132.207.44.77:3306/inventaire2022'
adresse = adresse.format(nom=nom, mdp=mdp)

table = BaseTableau(adresse, 'equipement', 'idequipement')
db = table.db

# equipement = db.table('equipement')
# compagnies = db.table('compagnies')
# references = db.table('references')

# # Version 1: .join
# with table.begin() as connexion:
#     énoncé = sqla.select(equipement, compagnies, references)\
#                  .join(compagnies,
#                        compagnies.c.idcompagnies == equipement.c.fournisseur)\
#                  .join(references,
#                        references.c.itemID == equipement.c.reference)
#     résultat = pd.read_sql(énoncé, connexion)

# print(résultat.head())

# test = résultat.loc[:, ['fournisseur', 'idcompagnies']]
# print(test)

# Version 2: via pandas?
equipement = table
compagnies = BaseTableau(db, 'compagnies', 'idcompagnies')
references = BaseTableau(db, 'references', 'itemID')

cond_fournisseurs = equipement.db.table(
    'equipement').c.fournisseur == compagnies.db.table('compagnies').c.idcompagnies
cond_fabricants = equipement.db.table(
    'equipement').c.fabricant == compagnies.db.table('compagnies').c.idcompagnies
fournisseurs = compagnies.select(where=[cond_fournisseurs])
fabricants = compagnies.select(where=[cond_fabricants])

cond_references = equipement.db.table(
    'equipement').c.reference == references.db.table('references').c.itemID
references = references.select(where=[cond_references])

df = equipement.loc(['nom', 'fournisseur', 'no_fournisseur', 'reference', 'quantite'])[:, :]
df.loc[:, 'idequipement'] = df.index

cond = df.loc[~df.fournisseur.isna(), 'fournisseur']
fournisseurs = fournisseurs.loc[cond, ['nom']].rename(columns={'nom': 'nom_fournisseur'})

cond = df.loc[~df.reference.isna(), 'reference']
references = references.loc[cond, ['lien']]

df = df.set_index('fournisseur')\
       .join(fournisseurs)\
       .set_index('reference')\
       .join(references)\
       .set_index('idequipement')

df.to_excel('res.xlsx')