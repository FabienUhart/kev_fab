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
        #clear du fichier temporaire avant ouverture en Rw
        self.ftemp = open("temp-file.txt","r+")
        #self.ftemp.seek(0)                        
        #self.ftemp.truncate()
        
        
    def ReadLine(self):
      self.NbLignes = self.f.readlines()
      n = 1
      temp = []

      #parcours du fichier source principal
      for line in self.NbLignes : 
        n+=1
        #découpe des lignes délimiteur espace par défaut
        temp = line.split()

        print("ligne37 "+temp[15])

        #écrire infos interessantes dans fichier temporaire
        self.Info_concat=temp[15]+" "+temp[16]+ "\n"
        self.ftemp.write(self.Info_concat)
        #pour chaque ligne, je regarde si occurence existe dans le fichier temporaire
        
        lines = self.ftemp.readlines()
        print(lines)
        for line in lines :
          if line == self.Info_concat:
            print("ok")
        

        if temp[15] == "srcip=\"10.110.0.23\"" :
            print("ok")
        #for elt in temp :
         # print(" salut " + elt)
      self.PrintN(n)
      lines = self.ftemp.readlines()
      for linet in lines:
        print(linet.strip())
    
    def PrintN(self,N):
      print(N)

  


a = Traitement()
a.OpenFile("import-fw-lite.txt")
a.ReadLine()
a.PrintN(42)





