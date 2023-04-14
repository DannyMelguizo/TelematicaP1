import socket
import threading
import constants
import get , head , post, error400

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

    while True:
        data_recevived = client_connection.recv(constants.RECV_BUFFER_SIZE)
        remote_string = str(data_recevived.decode(constants.ENCONDING_FORMAT))
        remote_command = remote_string.split()
        command = remote_command[0]
        print (f'Data received from: {client_address[0]}:{client_address[1]}')
        print(command)

        state = '200'
        description = 'OK'
        date = 0
        server = constants.SERVER
        content_type = 0
        content_length = 0
        file = 0

        request = 0
        
        if (command == constants.HEAD):

            try:
                request = head.head(remote_command[1])
                
            except:
                request = head.head('/error/error404.html')
                state = "404"
                description = 'Not Found'

        elif (command == constants.POST):

            if remote_command[1] != '/confirmacion.html':
                state = '405'
                description = 'Method Not Allowed'
                request = post.post('/error/error405.html')
            else:
                request = post.post(remote_command[1])
            
            file = request['file']

        elif(command == constants.GET):
            
            try:
                request = get.get(remote_command[1])
                
            except:
                request = get.get('/error/error404.html')

                state = "404"
                description = 'Not Found'
            
            file = request['file']

        elif (command == constants.QUIT):

            break

        else:
            state = '400'
            description = 'Bad Request'
            request = error400.error('/error/error400.html')


        date = request['Date']
        content_type = request['Content-Type']
        content_length = request['Content-Length']

        response = f"""\nHTTP/1.1 {state} {description}
                \rDate: {date}
                \rServer: {server}
                \rContent-Type: {content_type}
                \rContent-Length: {content_length}\n\n"""

        if file != 0:
            response = f"""\nHTTP/1.1 {state} {description}
                \rDate: {date}
                \rServer: {server}
                \rContent-Type: {content_type}
                \rContent-Length: {content_length}\n\n
                \r{file}\n\n"""

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