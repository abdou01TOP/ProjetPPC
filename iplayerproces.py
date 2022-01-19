from multiprocessing import Process, Manager, Lock, Pipe
import signal
import os
import time
import threading
import sys

from ProcessMain import Dictionnaire
#import sysv_ipc

#general variables

key = 128
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)


try:
    mq = sysv_ipc.MessageQueue(key)
except ExistentialError:
    print("Cannot connect to message queue", key, ", terminating.")
    sys.exit(1)


a,b = Pipe()
def sendtheplayerid(piddujoueur):#envoie du pid joueur receveur de cartes, c'est le pid présent dans le dictionnaire
    a.send(os.getpid)

#from shared memory take the id of The offre
# déclarer un mutex pour modifier current hand, si 2 process en concurrence sur la meme carte, le premier qui réussiit à chopper le mutex
def receivemessagequeeplayer (player,currenthand):
    #définir le message qui sera envoyé
    #1er envoi, attention erreur
    message = str(value).encode()
    pid=b.recv()
    mq.send(message, type=pid)


    while True:
        message, t = mq.receive(type=pid))
        
        
        if t == b.pid:
            cartesrcv=message.decode()
        else:
            print("exiting.")
        break
    
    currenthand.append(cartesrcv)


def sendmessagequeuetooffer (piddujoueur, currenthand):
    message=str(value).encode()
    mq.send (message,[type=piddujoueur])






    while True:
        message, t = mq.receive()
        value = message.decode()
        
        if t == piddujoueur:
            cartesrcv2=message.decode()
        else:
            print("exiting.")
        break
    
    currenthand.append(cartesrcv2)


def Possiblemodif(currenthand,lst):
        
    if currenthand.count(Dictionnaire[lst[1]])>=int(lst[0]):
        return True
    return False
    

    
    
    
    #compare les cartees de currenthand et l'offre proposée 
    #attention à proteger la shared memory 

    
#Dans type du message queue on envoie le pid du joueur qui veut recevoir en le prenant de la shared memory
#envoyer d'abord un messagequeue ou un pipe pour dire qu'on a accepté une certaine offre
#for both thoe function the messagequeue exchanged are the cards
#modification de Current Hand

#####################################################


def RingThebell(): 
    #raajouter condition de vérification de fin de jeu 
    os.kill(os.getppid(),signal.SIGUSR1)
    #envoyer le pid du joueur gagnant 
    #envoyer signal pour décencher la cloche


#########################################
def ModifCurrentoffer(Modif,Currentoffers, mutex,currenthand):
    lst =list(Modif.replace(" ","").lower())
    if Possiblemodif(currenthand,lst):

        mutex.acquire()
        Currentoffers[os.getpid()]=lst [0]
        mutex.release()
    else :
        print ("Vous n'avez pas assez de Cartes")



def player(Currentoffers, mutex, currenthand)#ajouté current hand 

    while True: #pour qu'il joue tout le temps
        
        
        input(print ("pour le jouer player"+currenthand+" voici vos cartes: ")) #rendre cette étape en Thread
        modif = input("entre une offre")
        if M
            t3 = threading.Thread(target=ModifCurrentoffer, args=(modif,Currentoffers, mutex,currenthand)
            t3.start
            t3.join
        

        Sonner=str(input("Voulez vous sonner la cloche(Y/N)"))
        if Sonner=='Y:
            if currenthand.count(currenthand[0])==5:
                RingThebell()
            else: 
                print("tu n'a pas 5 cartes")

            #Faut la faire en Thread ? 
           #Création de signal avec game pour déclencher gerercloche

        Offre= int(input("Accepteez le numéro de l'offre" )) #pour l'instant c'est le ppid du joueur

        if Offre >= 0:
            pass

        if Offre == 
    
            


            






    
    

