import socket
import threading
import constants
import get , head , post

# Defining a socket object...
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = constants.IP_SERVER

def main():
    print("***********************************")
    print("Server is running...")
    print("Dir IP:",server_address )
    print("Port:", constants.PORT)
    server_execution()
    
# Handler for manage incomming clients conections...

def handler_client_connection(client_connection,client_address):
    print(f'New incomming connection is coming from: {client_address[0]}:{client_address[1]}')
    is_connected = True
    while is_connected:
        data_recevived = client_connection.recv(constants.RECV_BUFFER_SIZE)
        remote_string = str(data_recevived.decode(constants.ENCONDING_FORMAT))
        remote_command = remote_string.split()
        command = remote_command[0]
        print (f'Data received from: {client_address[0]}:{client_address[1]}')
        print(command)
        
        if (command == constants.HEAD):
            request = head.head(remote_command[1])
            response = f"""\n{remote_command[2]} 200 OK
                        \rDate: {request['Date']}
                        \rServer: {request['Server']}
                        \rContent-Type: {request['Content-Type']}
                        \rContent-Length: {request['Content-Length']}\n\n"""
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))

        elif (command == constants.POST):
            request = post.post(remote_command[1])
            response = f"""\n{remote_command[2]} 200 OK
                        \rDate: {request['Date']}
                        \rServer: {request['Server']}
                        \rContent-Type: {request['Content-Type']}
                        \rContent-Length: {request['Content-Length']}\n\n
                        \r{request['file']}\n"""
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))

        elif(command == constants.GET):
            request = get.get(remote_command[1])
            response = f"""\n{remote_command[2]} 200 OK
                        \rDate: {request['Date']}
                        \rServer: {request['Server']}
                        \rContent-Type: {request['Content-Type']}
                        \rContent-Length: {request['Content-Length']}\n\n
                        \r{request['file']}\n"""
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))

        elif (command == constants.QUIT):
            response = '200 OK\n'
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
            is_connected = False

        else:
            response = '400 OK\n\rCommand-Description: Bad Request\n\r'
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
    
    print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...')
    client_connection.close()

#Function to start server process...
def server_execution():
    tuple_connection = (server_address,constants.PORT)
    server_socket.bind(tuple_connection)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print ('Socket is bind to address and port...')
    server_socket.listen(5)
    print('Socket is listening...')
    while True:
        client_connection, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handler_client_connection, args=(client_connection,client_address))
        client_thread.start()
    print('Socket is closed...')
    server_socket.close()

if __name__ == "__main__":
    main()