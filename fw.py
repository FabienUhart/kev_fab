import os
import pdb
import time

#ouvrir fichier
#parcourir ligne du fichier source
#pour chaque ligne
#  si quator de données existe dans fichier destination
#    alors incrémenter le compteur
#  sinon ajouter ligne dans fichier destination/

class Traitement:
    def __init__(self):
        self.f = []
        self.teub = []
        self.NbLignes = []

    def OpenFile(self,nom_fichier):
        self.f = open(nom_fichier, "r")
        
    def ReadLine(self):
      self.NbLignes = self.f.readlines()
      n = 1
      temp = []
      for line in self.NbLignes : 
        n+=1
        temp = line.split("srcip=\"")
        print(temp[1].split("\"",1))

        for elt in temp :
          print(elt)
      self.PrintN(n)
    
    def PrintN(self,N):
      print(N)

  


a = Traitement()
a.OpenFile("import-fw.txt")
a.ReadLine()
a.PrintN(42)





