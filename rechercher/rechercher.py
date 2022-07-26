# -*- coding: utf-8 -*-
"""Créé le Mon Jul 25 12:01:04 2022 par emilejetzer."""

from polygphys.outils.base_de_donnees import BaseTableau

from pathlib import Path

from inventaire import InventaireConfig

import keyring
import getpass

# Obtenir le fichier de configuration
# Un bon endroit où le placer est le répertoire racine de l'utilisateur.
fichier_config = Path('~/inventaire.cfg').expanduser()
config = InventaireConfig(fichier_config)

# Le mot de passe ne devrait pas être gardé dans le fichier de configuration.
# On utilise le module keyring pour le garder dans le trousseau.
# Le mot de passe reste accessible à tous les programmes Python,
# donc il faut faire attention à ce qu'on exécute comme code sur
# l'ordinateur.
nom = config.get('bd', 'nom')
utilisateur = config.get('bd', 'utilisateur')
mdp_id = f'polygphys.inventaire.main.bd.{nom}.{utilisateur}'
mdp = keyring.get_password('system', mdp_id)

if mdp is None:
    mdp = getpass.getpass('mdp>')
    keyring.set_password('system', mdp_id, mdp)


class Inventaire(BaseTableau):

    def rechercher(self, *cond):
        pass
