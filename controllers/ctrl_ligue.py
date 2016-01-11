# -*- coding: utf-8 -*-


def index(): 
    '''Retourne la liste des ligues (nom, adresseRue, ville, URLSiteWeb) '''
    rowsLigues = db(db.ligue.idDiscipline==db.discipline.id).select(db.ligue.nom,db.ligue.URLSiteWeb,db.discipline.libelle)
    return locals()
