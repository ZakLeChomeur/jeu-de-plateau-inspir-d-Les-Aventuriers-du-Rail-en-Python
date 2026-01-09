import numpy as np

class Carte:
    def __init__(self):
        self.carte_wagon_init={"blanc":12,"bleu":12,"jaune":12,"vert":12}
        self.choix_wagon=["blanc","bleu","jaune","vert"]
        self.carte_trajet_init={"trajet1":8,"trajet2":9,"trajet3":10,"trajet4":13,"trajet5":8,"trajet6":9,"trajet7":10,"trajet8":13}
        self.choix_trajet=["trajet1","trajet2","trajet3","trajet4","trajet5","trajet6","trajet7","trajet8"]
        
    def piocheWagon(self,number):
        Listepioche=[]
        listeSelection=np.random.choice(len(self.choix_wagon),number)
        for elt in listeSelection:
            if self.carte_wagon_init[self.choix_wagon[elt]] > 0 :
                self.carte_wagon_init[self.choix_wagon[elt]]=self.carte_wagon_init[self.choix_wagon[elt]]-1
                Listepioche.append(self.choix_wagon[elt])
            else:
                return self.piocheWagon(number)
        return Listepioche
    
    def piocheTrajet(self):
        listePioche={}
        if len(self.choix_trajet) > 3:
          listeSelection=np.random.choice(self.choix_trajet,3,replace=False)
        else:
          listeSelection=np.random.choice(self.choix_trajet,len(self.choix_trajet),replace=False)
          
        for elt in listeSelection:
            listePioche[elt]=self.carte_trajet_init[elt]
            del  self.carte_trajet_init[elt]
            self.choix_trajet.remove(elt)
        return listePioche
        
class joueur:
    def __init__(self):
      self.carte_wagon_joueur={"blanc":0,"bleu":0,"jaune":0,"vert":0}
      self.carte_trajet_joueur={}
      self.score=0
    
    def recolteWagon(self,wagon):
        for elt in wagon:
            self.carte_wagon_joueur[elt]=self.carte_wagon_joueur[elt]+1
    
    def recolteTrajet(self,trajet):
        self.carte_trajet_joueur.update(trajet)
    
    def recoltePoint(self):
        print("compte")
       
class graphe:
    def __init__():
        print("faire des graphe et des chemins")
    
   
    
class jeu:
   def __init__(self):
       self.carte=Carte()
       self.nombre2tour=10
       print("pour selectionner une action choisir un numero:")
       print("joueur contre joueur - 1")
       print("joueur contre ordinateur - 2")
       choix = int(input("entrez le numero "))
       if choix == 1:
           joueur1=joueur()
           joueur2=joueur()
           self.joueurs=[joueur1,joueur2]
           for elt in self.joueurs:
               elt.recolteWagon(self.carte.piocheWagon(4))
               elt.recolteTrajet(self.carte.piocheTrajet())
           print("carte visible :")
           self.wagon=self.carte.piocheWagon(5)
           print(self.wagon)
           self.partieEnCourspvp(self.nombre2tour)
       elif choix == 2:
           self.partieEnCourspvo(self.nombre2tour)
       else:
           self.__init__()
   
   def action1(self,joueur):
       listePioche=[]
       stockage=[]
       nombredecarteVisible=0
       print(self.wagon)
       print("choisir 2 carte differente dans les visible ou la pioche")
       i=1
       for elt in self.wagon:
           print("pour", elt, " selectionner -",i)
           i=i+1
       print("pour prendre une carte aleatoire selectionner -",i)
       choix=int(input("votre choix 1 ?"))
       if 1 <= choix <= len(self.wagon):
          listePioche.append(self.wagon[choix - 1])
          nombredecarteVisible=nombredecarteVisible+1
          stockage.append(self.wagon[choix - 1])
       elif choix == i: 
          carte=self.carte.piocheWagon(1)
          listePioche.append(carte[0])
       else:
          self.action1(joueur)
          
       choix=int(input("votre choix 2 ?"))
       if 1 <= choix <= len(self.wagon):
          listePioche.append(self.wagon[choix - 1])
          nombredecarteVisible=nombredecarteVisible+1
          stockage.append(self.wagon[choix - 1])
       elif choix == i: 
           carte=self.carte.piocheWagon(1)
           listePioche.append(carte[0])
       else:
          self.action1(joueur)
          
       for elt in range(nombredecarteVisible):
          self.wagon.remove(stockage[elt])
          carte=self.carte.piocheWagon(1)
          self.wagon.append(carte[0])
       joueur.recolteWagon(listePioche)
       print("Nouvelle carte Visible",self.wagon)
       print("Nouvelle carte dans votre main",joueur.carte_wagon_joueur)
       
        
       
   def action2(self,joueur):
       pioche=self.carte.piocheTrajet()
       print(pioche)
       print("pour garder 1 carte Trajets - 1")
       print("pour enlever 1 carte Trajets - 2")
       print("pour garder toutes les cartes Trajets - 3")
       choix = int(input("combien voulez vous garder de carte Trajet ?"))
       if choix == 3:
           joueur.recolteTrajet(pioche)
       elif choix == 2:
           print("celle que vous ne voulez pas garder?")
           i=0
           liste=[]
           for elt in pioche.keys():
               liste.append(elt)
               print(elt,"selectionner -",i+1)
               i=i+1
           choix2=int(input("?"))
           self.carte.carte_trajet_init.update({liste[choix2-1] : pioche[liste[choix2-1]]})
           del pioche[liste[choix2-1]]
           joueur.recolteTrajet(pioche)
       elif choix == 1 :
           print("celle que vous voulez garder?")
           i=0
           liste=[]
           for elt in pioche.keys():
               liste.append(elt)
               print(elt,"selectionner -",i+1)
               i=i+1
           choix2=int(input("?"))

           joueur.recolteTrajet({liste[choix2-1] : pioche[liste[choix2-1]]})
           del pioche[liste[choix2-1]]
           self.carte.carte_trajet_init.update(pioche)
       else:
           self.action2(joueur)
       print("votre main carte trajet", joueur.carte_trajet_joueur)
       
   def action3(self,joueur):
       print(joueur)
   
   def actionParTour(self,joueur):
       print("prendre des cartes Wagons - 1")
       print("piocher des cartes Trajets - 2")
       print("prendre possession des routes(en formation) - 3")
       choix=int(input("choisir une action:"))
       if choix == 1:
         self.action1(joueur)
       elif choix == 2:
         self.action2(joueur)
       elif choix == 3:
         self.action3(joueur)
       else: 
         self.partieEnCourspvp(joueur)
       print("un truc qui compte les cartes pour savoir si ca finis")
       
   def finDeGame(self):
     print("Fin de la partie et comptons les points")  
         
   def partieEnCourspvp(self,tour):
       for elt in range(tour):
           print("tour du joueur",elt%2+1)
           self.actionParTour(self.joueurs[elt%2])
       self.finDeGame()
       
        
   def partieEnCourspvo(self,tour):
        print("non")

jeu()






           
        
