import socket
from _thread import *
import time
import datetime
import random
import os
import signal

last_sync = datetime.datetime.now()

server = "192.168.147.1"
port = 5555
chat_cash = []
token = str(random.randint(100, 200))
tokens_recieved = 0

# token expiration should be implemented

connections = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(4)

print(f"Welcome to the 'ShadowCat' chat server.\r\nCurrent time is {str(last_sync)[11:-7]}.\r\nThis particular version supports up to 4 connections\r\n")
print("Server Started! Waiting for connection...")


def threaded_client(conn):
    global last_sync, chat_cash, token, connections, tokens_recieved

    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(1024)
            reply = data.decode("utf-8")

            if '#obey' in reply:
                print(f'Admin says:{reply}')
                if '_exit' in reply:
                    conn.sendall(str.encode('Server is shutting down!'+'000'))
                    for i in ['5', '4', '3', '2', '1', '\r\nGoodnight!']:
                        print(i)
                        time.sleep(1)
                    os.kill(os.getpid(), signal.SIGINT)
                elif '_tickle' in reply:
                    conn.send(str.encode("Tee-hee-hee...\nHey!! >.< I'm trying to work here!"+'666'))
                reply = ''

            if token in reply:
                print(f'{token} delivered.') # confirming delivery
                tokens_recieved += 1
                print(f'{tokens_recieved}/{len(connections)} tokens recieved.')
                reply = reply.replace(token, '') # wiping token from reply
                if tokens_recieved == len(connections): # if all tokens received, wipe message cash on the server side
                    chat_cash = []
                    #print('Message cash wiped.') <- uncomment this to get informed about the message cash getting wiped each timr
                    tokens_recieved = 0
                    token = str(random.randint(100, 200))

            if not data:
                print("Disconnected")
                connections.remove(conn)
                print(f"{len(connections)} user(s) online.")
                break
            elif reply != '':
                #print("Recieved: ", reply) <- Uncomment this to read chat on the server side

                chat_cash.append(reply)

            if chat_cash != [] and int((datetime.datetime.now() - last_sync).seconds) > 0.1:
                for connection in connections:
                    connection.sendall(str.encode(''.join(chat_cash)+token))
                    print("Sending: "+token)
                    last_sync = datetime.datetime.now()

        except:
            break

    print(f"{addr} Disconnected!")
    conn.close()


up = True


while up:
    conn, addr = s.accept()
    print("Connected to:", addr)
    connections.append(conn)
    print(f"{len(connections)} user(s) online.")

    start_new_thread(threaded_client, (conn,))

