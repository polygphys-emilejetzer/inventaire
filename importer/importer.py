# -*- coding: utf-8 -*-
"""Créé le Tue Jul  5 10:52:58 2022 par emilejetzer."""

from pathlib import Path

import numpy as np
import pandas as pd

from polygphys.outils.config import FichierConfig
from polygphys.outils.base_de_donnees import BaseTableau


class ImporterConfig(FichierConfig):

    def default(self):
        return (Path(__file__).parent / 'default.cfg').open().read()


class VueInventaire:
    noms_tables = (('bris', 'idbris'),
                   ('commande', 'idcommande'),
                   ('commandes_ouvertes', 'idcommande_ouverte'),
                   ('compagnies', 'idcompagnies'),
                   ('emprunt', 'idemprunt'),
                   ('equipement', 'idequipement'),
                   ('etageres', 'idetageres'),
                   ('locaux', 'idlocaux'),
                   ('personnes', 'idpersonnes'),
                   ('rangement', 'idrangement'),
                   ('references', 'itemID'),
                   ('responsables', 'idresponsables'))

    def __init__(self, adresse):
        self.tableaux, self.db = [], None

        for t, ind in self.noms_tables:
            if self.db is None:
                t = BaseTableau(adresse, t, ind)
                self.db = t.db
            else:
                t = BaseTableau(self.db, t, ind)

            self.tableaux.append(t)

    def charger(self, fichier: Path):
        df = pd.read_excel(fichier)
        pass

    def télécharger(self, fichier: Path):
        with ExcelWriter(fichier) as f:
            pass
