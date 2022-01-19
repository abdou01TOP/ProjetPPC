from multiprocessing import Process, Manager, Lock, Pipe, process
import signal
import os
import time
import threading

# pour le problème writers un reaer: penser à une variable global consflag 
def gereroffre(Currentoffers,mutex):
while True:
  #publication du dictionnaire; voir simeilleure mméthode
  mutex.aquire()
  print(Currentoffers)#  pas intelligent parceque dans ce cas réenvoyé un pipe au main pour afficher dans le terminal
  mutex.release()

    
#handler de signal 
#producteur de signal 

def gerercloche(bell):
    
    if( bell== 'Allumer cloche'):
        #Fermeture du jeu 
        
    

def game(Currentoffers,mutex, readermutex,writermutex):
    


    t1 = threading.Thread(target=gerercloche, args=())
    t2 = threading.Thread(target=gereroffre, args=(Currentoffers,mutex, readermutex,writermutex))
    t1.start()
    t2.start()
    