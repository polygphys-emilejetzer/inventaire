#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pathlib

from sqlalchemy import MetaData

from polygphys.outils.base_de_donnees import BaseDeDonnées, BaseTableau

class ZoteroItems:

    def __init__(zotero: str, sortie: str):
        self.items = BaseTableau(zotero, 'items', 'itemID')
        #self.itemData = BaseTableau(self.zotero, 'itemData')
        #self.itemDataValues = BaseTableau(self.zotero, 'itemDataValues')
        #self.fieldsCombined = BaseTableau(self.zotero, 'fieldsCombined')
        #self.groups = BaseTableau(self.zotero, 'groups')

        self.sortie = BaseTableau(sortie, 'references')

    def test(self):
        items = self.items.select()
        items = items.loc[:, ['libraryID', 'key']
