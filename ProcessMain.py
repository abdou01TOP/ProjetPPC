from concurrent.futures import process
from multiprocessing import Process, Manager, Lock
import multiprocessing 
import multiprocessing.connection
from nis import match
import os
import signal
import sys
import threading
import time

global listdemoyens 
global bol
Dictionnaire= {'b':'Bicyclette','a':'Avion','t':'Train','p':'Pied','v':'Voiture'}# normalement création d'une liste d'objet 
#revoir l'ordre de l'affichage

def gereroffre(Currentoffers,mutex):
    bol=True
    while bol:
        #publication du dictionnaire; voir si meilleure mméthode
        
        print(Currentoffers,end="\r")
        time.sleep(0,5)
        #affichage sur le terminal
        

compteur=0
  
def handler(sig,frame): #un handler le meme
    if sig==signal.SIGUSR1:
         #signal d'un process qu'il a terminé 
        for i in processes:
            os.kill(i.pid,signal.SIGKILL)#enlever sigkill
        
        os.kill(os.getppid(),signal.SIGTERM)

    if sig==signal.SIGTERM:
        mq.remove()#remove the message queuee
        print("The Game has finished") 
        for i in processes:
            i.join()
        bol = False
        Thread.join()


#actuellement programmé sur 3
def GenerateHand(): #Générateur de hand avec les objets carte
#en fonction du nombre de joueurs génerer des objets 
    Hand1= ['Voiture','Avion','Train','Voiture','Voiture']
    Hand2= ['Avion','Avion','Voiture','Train','Train']
    Hand3=['Voiture','Avion','Avion','Train','Train']
     
    Currenthand = [Hand1,Hand2,Hand3]
    return Currenthand

   


if __name__ == 'main':
    nbjoueurs=int(input ('entrez un nombre de joueurs entre 3 et 5'))#réduire le nombre d'éléments ensuite de la liste à 3
    processes= list() 
    nbjoueurs


    with Manager() as manager:
         Currentoffers=manager.dict()
         mutex = Lock ()
         #remplir le dictionnaire
         Currenthand= GenerateHand()


         for i in nbjoueurs:
             processes.append(Process (target=playerprocess, args=(Currentoffers,mutex,Currenthand[i])))
             processes[i].start()
             Currentoffers[process[i].pid]=0
        
    Thread= threading.Thread (target= gereroffre, args=(Currentoffers, mutex))
    Thread.start()

             



class Carte:
  def __init__(self, type):
        self.type = type

  def __str__(self):
        return self.type


  
       
    






    




  
            


# en quittant la with on libère la shared memory
    



         




        


