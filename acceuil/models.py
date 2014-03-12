#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Titre_cours (models.Model):
    Domaine = models.CharField(choices=[('E&G','Economie et Gestion'),('S&T','Sciences et Technologiques')],max_length=20)
    Mention = models.CharField(choices=[('E&G','Economie et Gestion'),('S&I','Sciences informatiques')],max_length=20)
    Specialite = models.CharField(choices=[('TEL','Telecommunications'),('BDD','Base de donnees'),('ONE','Organisation de la net Economie'),('NOSP','NOSP'),('SdE','Sciences entreprise'),('SC','Sciences Comptables')],max_length=50)
    Type_Cours = models.CharField(choices=[('OPT','Optionnel'),('OBL','Obligatoire')],max_length=20)
    Langues = models.CharField(choices=[('EN','Anglais'),('FR','Francais'),('ES','Espagnol'),('CR','Creole')],max_length=20)
    def __unicode__(self):
        return u'%s-%s-%s-%s-%s' % (self.Domaine,self.Mention,self.Specialite,self.Type_Cours,self.Langues)


class Code_cours (models.Model):
    Programme = models.ForeignKey('Titre_cours')
    Etablissement = models.CharField(max_length=10)
    Grade = models.CharField(choices=[('PROP','Propédeutique'),('L1','Premiere'),('L2','Deuxieme'),('L3','Licence'),('M1','Master1'),('M2','Master2')],max_length=10)
    Semestre = models.CharField(choices=[('Y','All_Year'),('S1','Premier_Semestre'),('S2','Deuxieme_Semestre')],max_length=30)
    Nom_Cours = models.CharField(max_length=20)
    def __unicode__(self):
        return u'%s-%s-%s-%s-%s' % (self.Programme,self.Etablissement,self.Grade,self.Semestre,self.Nom_Cours)


class Professeurs (models.Model):
    Nom = models.CharField(max_length=40)
    Prenom = models.CharField(max_length=20)
    Telephone = models.CharField(max_length=15)
    Email = models.EmailField(max_length=30)
    Adresse = models.CharField(max_length=50)
    Nif = models.CharField(max_length=25)
    Date_de_Naissance=models.DateField()
    Niveau_Etude = models.CharField(choices=[('Licence','Licence'),('Master','Master'),('Doctorat','Doctorat')],max_length=10)
    Evaluation = models.CharField(max_length=500)
    Reference = models.CharField(max_length=400)

    def __unicode__(self):
        return u'%s'% (self.Nom)

class Descriptif_Cours (models.Model):
     Code_cour = models.ForeignKey('Code_Cours')
     Professeurs = models.ManyToManyField('Professeurs')
     Code_Cours = models.CharField(max_length=50)
     Nom_Cours = models.ForeignKey('Titre_cours')
     Credit_ECTS = models.IntegerField(max_length=10)
     Etablissement = models.CharField(max_length=20)
     Public_Cibles = models.CharField(max_length=20)
     Pre_Requis = models.CharField(max_length=100)
     Objectif = models.CharField(max_length=100)
     Description = models.CharField(max_length=50)
     PlanCours = models.CharField(max_length=200)
     Format = models.CharField(max_length=50)
     Ressource = models.CharField(max_length=50)
     Evalution = models.CharField(max_length=50)
     def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.Code_cour,self.Professeurs,self.Code_Cours,self.Nom_Cours,self.Credit_ECTS,self.Etablissement,self.Public_Cibles,self.Pre_Requis,self.Objectif,self.Description,self.PlanCours,self.Format,self.Ressource,self.Evalution)


