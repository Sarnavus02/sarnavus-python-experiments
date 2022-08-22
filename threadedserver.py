from ipaddress import ip_address
from multiprocessing import connection
import socket
import threading, time

local_ip = "127.0.0.1"
port_number = 1234

THREADS = []
CMD_INPUT = []  
CMD_OUTPUT = []

def handle_connection(connection, address):
    msg = connection.recv(1024).decode()
    while msg!="quit":
        print(msg)
        connection.send(msg.encode())
        msg = connection.recv(1024).decode()
    close_connection(connection)

def close_connection(connection):
    connection.close()

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((local_ip, port_number))

while True:    
    ss.listen(5)
    connection, address = ss.accept()
    t = threading.Thread(target =handle_connection,args=(connection,address))    
    THREADS.append(t)
    t.start()

