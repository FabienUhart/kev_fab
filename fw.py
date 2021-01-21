import os
import pdb
import time
import json
from collections import Counter

#ouvrir fichier
#parcourir ligne du fichier source
#extraire les infos importantes et stocker dans un fichier temporaire
#puis boucler sur le fichier temporaire pour chercher des infos
#pour chaque ligne
#  si quator de données existe dans fichier destination
#    alors incrémenter le compteur
#  sinon ajouter ligne dans fichier destination/

class Traitement:
    def __init__(self):
        self.f = []
        self.NbLignes = []
        self.compteur = 0
        self.ChaineConcateneeOutput = [] #Utilisée comme stockage temporaire avant comptage des entrées identiques à l'intérieur (couple SrcIP DstIP)

    def OpenFile(self,nom_fichier):
        self.f = open(nom_fichier, "r")
        #clear du fichier temporaire avant ouverture en Rw
        self.ftemp = open("temp-file.txt","r+")
        #self.ftemp.seek(0)                        
        #self.ftemp.truncate()
              
    def ReadLineFromSourceFileAndSendToList(self):
      #Lecture du fichier source principal
      self.NbLignes = self.f.readlines()
      ChaineSpliteeInput = [] #Utilisée pour assembler les valeurs avant envoie dans la liste
      
      #parcours du fichier source principal
      for line in self.NbLignes : 
        #découpe des lignes délimiteur espace par défaut
        ChaineSpliteeInput = line.split()
        #Récupération des valeurs interessantes et concaténation (SrcIP DstIP)
        #Un peu de mise en forme
        if ChaineSpliteeInput[17] == "proto=\"6\"": ChaineSpliteeInput[17] = "TCP"
        ChaineSpliteeInput[10] = str(ChaineSpliteeInput[10]).replace('"',"")
        ChaineSpliteeInput[15] = str(ChaineSpliteeInput[15]).replace('"',"")
        ChaineSpliteeInput[16] = str(ChaineSpliteeInput[16]).replace('"',"")
        ChaineSpliteeInput[23] = str(ChaineSpliteeInput[23]).replace('"',"")
        self.Info_concat= ChaineSpliteeInput[10]+" "+ChaineSpliteeInput[15]+" "+ChaineSpliteeInput[16]+" "+ChaineSpliteeInput[17]+" "+ChaineSpliteeInput[23]
        #Ajout dans la liste de sortie
        self.ChaineConcateneeOutput.append(self.Info_concat)
        #print("ajout lignes dans fichier temp "+self.Info_concat)
        #pour chaque ligne, je regarde si occurence existe dans le 
      #self.ftemp.close()
      #print(self.temp2)
      self.ChaineConcateneeOutput.sort()
      print("\n taille de la liste : "+str(len(self.ChaineConcateneeOutput))+"\n")
      
        
    def FindNumberOffOccurence(self):
      self.c = Counter(self.ChaineConcateneeOutput)
      print( self.c.items() )

    def FormattingOutput(self):
      print (json.dumps(self.c, indent=2))


a = Traitement()
a.OpenFile("import-fw-lite.txt")
a.ReadLineFromSourceFileAndSendToList()
a.FindNumberOffOccurence()
a.FormattingOutput()






