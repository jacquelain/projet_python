__author__ = 'KENLEN'
from django.contrib import admin
from  acceuil.models import Titre_cours, Professeurs, Code_cours, Descriptif_Cours

admin.site.register(Titre_cours)
admin.site.register(Professeurs)
admin.site.register(Code_cours)
admin.site.register(Descriptif_Cours)

