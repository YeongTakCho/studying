import socket 
from _thread import * 
import settings
import pickle
from player import Player

server= settings.ip 
port = 5555

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)
    
s.listen(2)
print("waitng for connection, Server Started")


players= [Player(0,0,100,100,(0,255,0)), Player(100,100,100,100,(255,0,0))]

def threaded_client(conn :socket, player_num):
    conn.send(pickle.dumps(players[player_num]))
    reply= ''
    while True:
        try:
            # print('start receiving') # test how socket works
            # data= conn.recv(2048) # recv:  waiting conn send the data but if conn end, it finish and return none
            # print('receive compeleted') # test how socket works
            p_data= pickle.loads(conn.recv(2048))
            if not p_data:
                break

            else:
                players[player_num] = p_data
                
                if player_num ==0:
                    reply = players[1]
                else:
                    reply = players[0]
                    
            conn.sendall(pickle.dumps(reply))
            
        except:
            break
        
    print('Lost connection')
    conn.close()
    


current_player =0
while True:
    conn,addr = s.accept() # waiting the accept
    print("Connected to: ", addr)
    
    start_new_thread(threaded_client, (conn, current_player))
    current_player +=1