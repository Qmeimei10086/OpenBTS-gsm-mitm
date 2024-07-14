import socket
import threading
import sys
import os

RAND = "aaaabbbbccccddddeeeeffffgggghhhh"
SRES = ""
TMSIS = []

def send_AuthenticationRequest(imsi):
    cmd = "./OpenBTSDo \"sendsms " +imsi+" . " + "10086 \""
    print("excute cmd: "+cmd)
    os.system(cmd)

def print_tmsis():
    if TMSIS == []:
        print("TMSIS_Table is empty!")
        return False
    
    print("IMSI                    IMEI")
    for mobile in TMSIS:
        print(mobile["IMSI"]+"         "+mobile["IMEI"])
    return True

def set_RAND(rand):
    global RAND
    RAND = rand
    print("set RAND -> ",RAND)

def set_SRES(sres):
    global SRES
    SRES = sres
    print("set SRES -> ",SRES)

def start_server():
    # 创建一个TCP/IP socket
    global RAND
    global SRES
    global TMSIS

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 6666)
    
    # 绑定socket到端口
    server_socket.bind(server_address)
    
    # 监听端口
    server_socket.listen(1)
    print("\nServer has already started ,waiting for connection......")

    while True:
        # 等待连接
        connection, client_address = server_socket.accept()
        try:
            print("\nconnected from ",client_address)
            
            # 发送消息
            
            connection.sendall(RAND.encode())
            print("sending RAND: ",RAND)
            
            data = connection.recv(1024)
            if data:
                print("receive message from ",client_address)
                if ";" in data.decode():
                    receieve_data = data.decode().split(";")
                    SRES = receieve_data[2]
                    TMSIS.append({"IMEI":receieve_data[0],"IMSI":receieve_data[1]})
                    print("receive IMEI: ",receieve_data[0])
                    print("receive IMSI: ",receieve_data[1])
                    print("receive SRES: ",receieve_data[2])
                else:
                    SRES = data.decode()
                    print("receive SRES: ",data.decode())
        finally:
            connection.close()

def main():
    server = threading.Thread(target=start_server)
    server.start()
    while True:
        command = input("Server>")
        if command == "exit" or command == "quit":
            sys.exit(0)
        elif command == "tmsis":
            print_tmsis()
        elif command == "show rand":
            print(RAND)
        elif command == "show sres":
            print(SRES)
        elif "set rand" in command:
            if len(command.split()[2]) != 32:
                print("rand is wrong!Please enter 32-bit rand")
            else:
                set_RAND(command.split()[2])
        elif "set sres" in command:
            set_SRES(command.split()[2])
        elif "auth " in command:
            send_AuthenticationRequest(command.split()[1])
        elif command == "":
            continue
        else:
            print("unknown command")

if __name__ == "__main__":
    main()
