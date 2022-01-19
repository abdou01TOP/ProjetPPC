from multiprocessing import Process, Manager, Lock, Pipe
from multiprocessing.shared_memory import SharedMemory
import signal
import os
import time
import threading
import sys
import sysv_ipc

Dictionnaire={('v',555):'voiture', 'p':'pied'}
dic = {18222 : ['nomdujouur', 1], 18223 : ['nomdujouur2', 2]}
key = 128
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)

#value=[2,'v']
#value2 = [3,'p']

def sendercartes(pipe): #send cartes est en thread
    myhand = ['voiture','voiture']
    value = "2v"
    try:
        mq = sysv_ipc.MessageQueue(key)
    except ExistentialError:
        print("Cannot connect to message queue", key, ", terminating.")
        sys.exit(1)#value est un string
    for _ in range(int(list(value)[0])) : myhand.remove(Dictionnaire[list(value)[1]])
    print(myhand,"ok")
    message = str(value).encode()
    pid=pipe.recv()
    print(pid)
    mq.send(message, type=pid)
 # des que proposition offre, lancer ce Thread qui va rester en attente jusqu'à l'acceptation 
   

            
    message, _ = mq.receive(type=50)
    valuereceived = list(message.decode())
    for _ in range(int(valuereceived[0])): myhand.append(Dictionnaire[valuereceived[1]])
    print(myhand,"ok")

    


def sendmessagequeuetooffer (pipe): #pid qui se trouve dans la SharedMemory
    myhand = ['pied', 'pied']
    value = "2p"
    try:
        mq = sysv_ipc.MessageQueue(key)
    except ExistentialError:
        print("Cannot connect to message queue", key, ", terminating.")
        sys.exit(1)
    pipe.send(os.getpid())
    message=str(value).encode()
    for _ in range(int(list(value)[0])) : myhand.remove(Dictionnaire[list(value)[1]])
    print(myhand,"okok")
    mq.send(message,type=50)
    
    
    message, _ = mq.receive(type=os.getpid())
    valuereceived = list(message.decode())    
    for _ in range(int(valuereceived[0])): myhand.append(Dictionnaire[valuereceived[1]]) 
    print(myhand,"okok")
# si une offre t'interesse lancer ca ne appel de fonction avec le pid du joueur qui 
    
       
if __name__ == "__main__":
    print(Dictionnaire[('v',555)])
    a,b = Pipe()
    count = 1
    x = []# list des pid avec qui tu pourrais echanger 
    for i in dic:
        print(i)
        if dic[i][1] != 0:
            print(f"{count}. {dic[i][0]} a une offre")
            x.append(i)
            count += 1
    ans = "0"
    y = [i for i in range(1, count)]
    print(y)
    while int(ans) not in y:
        ans = input("avec qui tu veux échanger ? ")
    print(f"le pid du joueur avec qui tu vas échanger est {x[int(ans)-1]}")
    
    """p1 = Process(target=sendercartes, args = (a,))
    p2 = Process(target=sendmessagequeuetooffer, args=(b,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()"""
    