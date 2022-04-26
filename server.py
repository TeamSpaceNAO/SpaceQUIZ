from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
import webbrowser
import os
#import pyautogui
import numpy as np
import matplotlib.pyplot as plt
import cv2
import socket

domanda = 1
change = 1
risposteGiuste = ['A','C','A','A'] 
run = False

database = {'1':[],'2':[],'3':[]} #possibilità di creare un for per più squadre
#database = {'1':[],'2':[]}


def naoTcp_winner(vincitore):
    s = socket.socket()
    s.connect(('192.168.1.122',20000))
    s.send(str(vincitore).encode())



def change_page(n):
    global database
    if n <= 4:
        webbrowser.open('file:///'+str(os.getcwd())+'/domande/domanda'+str(n)+'.html')
        print('\nApertura pagina domanda '+str(n))
    elif n == 5: 
        #webbrowser.open('file:///'+str(os.getcwd())+"/domande/risultati.html")
        print("\nGioco finito!")
        print(database)
        ris = []
        for a in database:
            b = 0
            for i in database[a]:
                if i == 'giusto':
                    b+=1
            ris.append(b)
        ris = np.array(ris)
        #m, h) = max((v,h) for v,h in enumerate(ris))
        #rint(str(m)+' '+str(h))
        #naoTcp_winner(database[i])
        #print(database[h])
        maxV = max(ris)
        ind = [i for i, j in enumerate(ris) if j == maxV]
        c = int(str(ind)[1])+1
        naoTcp_winner("Squadra "+str(c))
        plt.bar(range(len(database)), ris, tick_label=list(database.keys()))
        plt.xlabel('Squadre')
        plt.ylabel('Risposte corrette')
        plt.savefig('risultati.jpg')
        while True:
            img = cv2.imread('risultati.jpg')
            cv2.namedWindow('risultati', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('risultati', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('risultati', img)
            if cv2.waitKey(0) == 27:
                break


class S(BaseHTTPRequestHandler):

    def do_POST(self):
        global domanda, run, risposteGiuste, change, database 

        post_data = self.rfile.read(int(self.headers['Content-Length'])) 
        data = str(post_data.decode('utf-8'))
        #self._set_response()

        if data == "inizia" and change ==1: #richiesta di nao per le risposte
            run = True
            change_page(1)
        if run and data!="inizia":    
            if data[0]!='N' and change<=len(database)*4:
                telecomando = data[0]
                risposta = data[2]
            if risposta == risposteGiuste[domanda-1] and len(database[telecomando])==domanda-1:
                database[telecomando].append('giusto')
                print("Risposta giusta")
            elif risposta != risposteGiuste[domanda-1] and len(database[telecomando])==domanda-1:
                database[telecomando].append('sbagliato')
                print("Risposta sbagliata")
            else:
                change -= 1

            if change%len(database) == 0:
                domanda+=1
                change_page(domanda)
            if change <= len(database)*4:
                change += 1



def runHTTP(server_class=HTTPServer, handler_class=S, port=8081):
    httpd = server_class(('',port), handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()



#pyautogui.hotkey("fn","f11")
httpThread = Thread(target=runHTTP())
    
if __name__ == "__main__":
    httpThread.run()
