import socket
import random
serv1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv1.bind(('localhost', 1000))
serv1.listen(5)
def fun():
    while True:
        global b
        conn1, addr = serv1.accept()
        b=random.randint(1,9999)
        conn1.send(str(b).encode())
        conn1.close()
        break
fun()
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('localhost', b))
serv.listen(5)

users=['oles:pass','mtt:user']

login=False
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:  
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode()
        if from_client =='LOGIN':
            conn.send(b'Type login:')
            logindata = conn.recv(4096)
            conn.send(b'Type pass:')
            passdata = conn.recv(4096)
            al=logindata.decode()+":"+passdata.decode()
            for k in users:
                if k ==al:
                    conn.send(b'Welcome,to see secret info,type SECRET,to close connect type CLOSE')
                    login=True
            if login==False:
                conn.send(b'wrong pass or login')
        elif from_client =='SECRET':
            if login==True:
                conn.send(b'This is Secret!')
            if login==False:
                conn.send(b'wrong command')
        elif from_client=='CLOSE':
                conn.send(b'stopconnect')
                conn.close()
                break
        elif from_client=='HELP':
            conn.send(b'COMMANDS:LOGIN,CLOSE,HELP')
        else:
            conn.send(b'wrong command')
        from_client = ''
