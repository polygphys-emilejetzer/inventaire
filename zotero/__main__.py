#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import schedule
import time
import traceback

from pathlib import Path

from . import MigrationConfig, ZoteroItems

journal = Path('~/zotero_a_inventaire.log').expanduser()
chemin = Path('~/zotero_a_inventaire.cfg').expanduser()
config = MigrationConfig(chemin)

zotero = config.get('zotero', 'adresse')
inventaire2022 = config.get('inventaire2022', 'adresse')
nom = config.get('inventaire2022', 'nom')
mdp = config.get('inventaire2022', 'mdp')

inventaire2022 = inventaire2022.format(nom=nom, mdp=mdp)

bd = ZoteroItems(zotero, inventaire2022)


def enveloppe():
    try:
        bd.charger()
    except Exception:
        with journal.open() as f:
            traceback.print_exc(file=f)


schedule.every(10).minutes.do(enveloppe)
while True:
    schedule.run_pending()
    time.sleep(10)
