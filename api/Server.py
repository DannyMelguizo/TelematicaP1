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

    #Se mantiene la conexión hasta que el usuario envie la peticion QUIT
    while True:
        data_recevived = client_connection.recv(constants.RECV_BUFFER_SIZE) #Recibe la peticion del usuario
        remote_string = str(data_recevived.decode(constants.ENCONDING_FORMAT))
        remote_command = remote_string.split()  #Parte la peticion para un mejor manejo
        command = remote_command[0] #Determina que exactamente esta pidiendo el usuario

        print (f'Data received from: {client_address[0]}:{client_address[1]}')
        print(command) #Se imprime en la consola del servidor que peticion se realizo

        #state: int, estado a retornar sobre la peticion del usuario
        #description: string, descripcion acerca del estado de la peticion del usuario
        #date: string, almacena la fecha en la que se realizo la peticion con base al GMT
        #server: string, servidor que respondio a la peticion
        #content_type: string, informacion acerca del tipo del archivo y como esta codificado
        #content_length: int, tama;o del archivo de la respuesta
        #file: string, archivo a mostrar, puede estar codificado en bytes
        #request: dict, diccionario que contiene las variables anteriores

        state = '200'
        description = 'OK'
        date = 0
        server = constants.SERVER
        content_type = 0
        content_length = 0
        file = 0

        request = 0
        
        if (command == constants.HEAD):

            #Se intenta realizar una peticion HEAD con la ruta especificada
            #En caso de no existir o encontrar un archivo, retorna el error 404
            try:
                request = head.head(remote_command[1])
                
            except:
                request = head.head('/error/error404.html')
                state = "404"
                description = 'Not Found'

        elif (command == constants.POST):

            #La peticion POST solamente funciona para la ruta /confirmacion.html
            #En caso de no ser dicha ruta, retorna el error 405
            if remote_command[1] != '/confirmacion.html':
                state = '405'
                description = 'Method Not Allowed'
                request = post.post('/error/error405.html')
            else:
                request = post.post(remote_command[1])
            
            file = request['file']

        elif(command == constants.GET):
            
            #Se intenta realizar una peticion GET con la ruta especificada
            #En caso de no existir o encontrar un archivo, retorna el error 404
            try:
                request = get.get(remote_command[1])
                
            except:
                request = get.get('/error/error404.html')

                state = "404"
                description = 'Not Found'
            
            file = request['file']

        elif (command == constants.QUIT):

            #Si la peticion es QUIT, sale del ciclo y cierra la conexión
            break

        else:
            #Si la peticion es diferente de POST, GET, HEAD o QUIT retorna error el 400
            state = '400'
            description = 'Bad Request'
            request = error400.error('/error/error400.html')
            file = request['file']

        #Asigna las variables del diccionario request, a sus respectivas variables
        date = request['Date']
        content_type = request['Content-Type']
        content_length = request['Content-Length']

        #response: string, contiene la informacion que sera entregada al usuario
        response = f"""\nHTTP/1.1 {state} {description}
                \rDate: {date}
                \rServer: {server}
                \rContent-Type: {content_type}
                \rContent-Length: {content_length}\n\n"""

        #Si la peticion contiene un archivo, se le agrega a la variable response
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
    #Se almacenan los datos del servidor y se ejecuta el servidor
    tuple_connection = (server_address,constants.PORT)
    server_socket.bind(tuple_connection)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print ('Socket is bind to address and port...') 
    server_socket.listen(5)
    print('Socket is listening...')

    #El servidor se mantiene en estado de ejecucion
    while True:
        client_connection, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handler_client_connection, args=(client_connection,client_address))
        client_thread.start()

if __name__ == "__main__":
    main()