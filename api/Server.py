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

    #variables locales que se establecen por defecto una vez se realice una conexion

    #keep_alive_timeout: int, tiempo que el servidor espera antes de cerrar la conexion con el usuario
    #si esta en 0, se entiende que la conexion se quedara establecida a menos que se indique lo contrario
    #connection_standar: string, establece si luego de la peticion se cerrara la conexion o se quedara abierta
    keep_alive_timeout = 0
    connection_standar = 'Keep-Alive'

    #Se mantiene la conexión hasta que el usuario envie la peticion QUIT, o que se cierre la conexion
    while True:

        #las variables se iran modificando a lo largo de la ejecucion del programa
        keep_alive = keep_alive_timeout
        connection = connection_standar

        try:
            data_recevived = client_connection.recv(constants.RECV_BUFFER_SIZE) #Recibe la peticion del usuario
            remote_string = str(data_recevived.decode(constants.ENCONDING_FORMAT))
            remote_command = remote_string.split()  #Parte la peticion para un mejor manejo

            #Se almacenan los diferentes headers que el usuario envia en la peticion al servidor
            while True:
                #Se almacena el antiguo comando, esto para verificar si el antiguo es igual al actual
                #Es decir, envio un \n
                new_str = remote_command

                #A;ade a la antigua peticion, la peticion o header actual
                data_recevived += client_connection.recv(constants.RECV_BUFFER_SIZE) #Recibe la peticion del usuario
                remote_string = str(data_recevived.decode(constants.ENCONDING_FORMAT))
                remote_command = remote_string.split()  #Parte la peticion para un mejor manejo

                #Se comprueba si envio un \n
                if new_str == remote_command:
                    break

            command = remote_command[0] #Determina que exactamente esta pidiendo el usuario

            print (f'Data received from: {client_address[0]}:{client_address[1]}')
            print(command) #Se imprime en la consola del servidor que peticion se realizo

            #Comprueba que en la peticion la version especificada del HTTP, sea la 1.1
            #Genera error si no cumple tener 3 posiciones, en tal caso, se asume que fue un error del usuario
            #Y no especifico la version o envio una peticion incorrecta
            try:
                if remote_command[2] != 'HTTP/1.1':
                    response = 'We only work with \'HTTP/1.1\' version\n\n'

                    client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
                    continue
            except:
                None
            
            #Si la peticion tiene mas de 3 datos, es por que hay headers incluidos, llama la funcion header
            #Para implementarlos
            if len(remote_command) > 2:
                for i in range(3, len(remote_command)):
                    keep_alive_timeout, connection_standar = headers(remote_command, i, keep_alive_timeout, connection_standar)
                
            #state: int, estado a retornar sobre la peticion del usuario
            #description: string, descripcion acerca del estado de la peticion del usuario
            #server: string, servidor que respondio a la peticion
            #date: string, almacena la fecha en la que se realizo la peticion con base al GMT
            #content_type: string, informacion acerca del tipo del archivo y como esta codificado
            #content_length: int, tama;o del archivo de la respuesta
            #file: string, archivo a mostrar, puede estar codificado en bytes
            #last_modified: string, almacena la fecha en la que fue la ultima modificacion del archivo
            #etag: string, archivo codificado en hexa, posee una llave unica
            #accept_ranges: string, no se admite la solicitud de contenido parcial
            #request: dict, diccionario que contiene las variables anteriores
            
            state = '200'
            description = 'OK'
            server = constants.SERVER
            date = content_type = content_length = file = last_modified = etag = 0
            accept_ranges = 'none'
            
            #Se reasignan las variables, en caso de que se hubiesen modificado al usar la funcion headers
            keep_alive = keep_alive_timeout
            connection = connection_standar

            request = 0
            
            if (command == constants.HEAD):

                #Se intenta realizar una peticion HEAD con la ruta especificada
                #En caso de no existir o encontrar un archivo, retorna el error 404
                try:
                    request = head.head(remote_command[1])
                    
                except:
                    request = head.head(constants.E404)
                    state = "404"
                    description = 'Not Found'

                date = request['Date']
                content_type = request['Content-Type']
                content_length = request['Content-Length']

                #Da una respuesta dependiendo de si el usuario cambio los datos estandares
                if keep_alive != 0 and connection == 'Keep-Alive':
                    response = f"""\nHTTP/1.1 {state} {description}
                        \rDate: {date}
                        \rServer: {server}
                        \rKeep-Alive: timeout={keep_alive}
                        \rContent-Type: {content_type}
                        \rContent-Length: {content_length}
                        \rConnection: {connection}\n\n"""
                else:
                    response = f"""\nHTTP/1.1 {state} {description}
                        \rDate: {date}
                        \rServer: {server}
                        \rContent-Type: {content_type}
                        \rContent-Length: {content_length}
                        \rConnection: {connection}\n\n"""

                client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
                #Comprueba si hay que tener un timeout o si se hay que cerrar la conexion
                if keep_alive != 0:
                    client_connection.settimeout(keep_alive)
                elif connection != 'Keep-Alive':
                    break
                continue

            elif (command == constants.POST):

                #La peticion POST solamente funciona para la ruta /confirmacion.html
                #En caso de no ser dicha ruta, retorna el error 405
                if remote_command[1] == '/confirmacion.html':
                    request = post.post(remote_command[1])   

                else:
                    try:
                        request = post.post(remote_command[1])

                        state = '405'
                        description = 'Method Not Allowed'
                        request = post.post(constants.E405)

                    except:
                        state = '404'
                        description = 'Not Found'
                        request = post.post(constants.E404)

            elif(command == constants.GET):
                
                #Se intenta realizar una peticion GET con la ruta especificada
                #En caso de no existir o encontrar un archivo, retorna el error 404
                try:
                    request = get.get(remote_command[1])
                    
                except:
                    request = get.get(constants.E404)

                    state = "404"
                    description = 'Not Found'

            elif (command == constants.QUIT):

                #Si la peticion es QUIT, sale del ciclo y cierra la conexión
                break

            else:
                #Si la peticion es diferente de POST, GET, HEAD o QUIT retorna error el 400
                state = '400'
                description = 'Bad Request'
                request = error400.error(constants.E400)
                date = request['Date']
                file = request['file']

                #Da una respuesta dependiendo de si el usuario cambio los datos estandares
                if keep_alive != 0 and connection == 'Keep-Alive':
                    response = f"""\nHTTP/1.1 {state} {description}
                        \rDate: {date}
                        \rServer: {server}
                        \rAllow: GET, HEAD, POST, QUIT
                        \rKeep-Alive: timeout={keep_alive}
                        \rConnection: {connection}\n\n"""
                else: 
                    response = f"""\nHTTP/1.1 {state} {description}
                        \rDate: {date}
                        \rServer: {server}
                        \rAllow: GET, HEAD, POST, QUIT
                        \rConnection: {connection}\n\n"""

                client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
                if keep_alive != 0:
                    client_connection.settimeout(keep_alive)
                elif connection != 'Keep-Alive':
                    break
                continue

            #Asigna las variables del diccionario request, a sus respectivas variables
            date = request['Date']
            content_type = request['Content-Type']
            content_length = request['Content-Length']
            last_modified = request['Last-Modified']
            etag = request['ETag']
            file = request['file']

            response= ''

            #response: string, contiene la informacion que sera entregada al usuario
            if keep_alive != 0 and connection == 'Keep-Alive':
                response = f"""\nHTTP/1.1 {state} {description}
                        \rDate: {date}
                        \rServer: {server}
                        \rLast-Modified: {last_modified}
                        \rETag: {etag}
                        \rAccept-Ranges: {accept_ranges}
                        \rContent-Type: {content_type}
                        \rContent-Length: {content_length}
                        \rKeep-Alive: timeout={keep_alive}
                        \rConnection: {connection}\n\n
                        \r{file}\n\n"""
            else:
                response = f"""\nHTTP/1.1 {state} {description}
                        \rDate: {date}
                        \rServer: {server}
                        \rLast-Modified: {last_modified}
                        \rETag: {etag}
                        \rAccept-Ranges: {accept_ranges}
                        \rContent-Type: {content_type}
                        \rContent-Length: {content_length}
                        \rConnection: {connection}\n\n
                        \r{file}\n\n"""
                
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
        except:
            break

        #Comprueba si hay que tener un timeout o si se hay que cerrar la conexion
        if keep_alive != 0:
            client_connection.settimeout(keep_alive)
        elif connection != 'Keep-Alive':
            break
        else:
            continue

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

def headers(command, n, keep, conn):

    #Gramatica implementada para los headers, en este caso solo reconoce Connection, y Keep-Alive
    gramar = {
        'Connection:' : 'close',
        'Keep-Alive:' : 'timeout'
    }
    #keep: int, corresponde al timeout estandar que tiene la conexion
    #conn: string, corresponde al tipo de conexion estandar que tiene la conexion
    keep_alive_ = keep
    connection_ = conn

    #token: string, variable que contiene la instruccion enviada por el usuario, sera evaluada luego
    #para ver si corresponde a la gramatica
    token = command[n]

    if token in gramar:

        #se aumenta el valor de la posicion actual, para conocer que se le esta asignando a la gramatica
        n += 1
        option = gramar[token]

        #
        description = command[n]

        if token == 'Keep-Alive:':
            #Verifica que este bien estructurada la peticion, es decir, si no se le asigna
            #ningun valor se deja por defecto
            try:
                description = description.split('=')
                #Se le asigna a la variable keep_alive_ lo que el usuario quizo asignar
                if description[0] == option:
                    keep_alive_ = int(description[1])
            except: 
                None

        elif token == 'Connection:':
            #Verifica que este bien estructurada la peticion
            #Se le asigna a la variable connection_ lo que el usuario quizo asignar
            if description == option:
                connection_ = description
    
    #Retorna las variables, son reasignadas a en la funcion handler_client
    return keep_alive_, connection_

if __name__ == "__main__":
    main()