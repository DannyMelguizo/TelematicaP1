# **Documentacion TWS Telematica**

*******

**Tabla de Contenido**

1. [Introducción](#introduction)
2. [Desarrollo](#development)
3. [Conclusiones](#conclusion) 
4. [Referencias](#references)<br>

*******

<div id='introduction'/> 

### **1. Introduccion**
En nuestro mundo actual, la transferencia de datos y la comunicación entre dispositivos se realiza a través de diferentes protocolos de red. Siendo  así, el protocolo de internet TCP/IP como uno de los más utilizados, el cual es una arquitectura de red que proporciona una forma estándar de comunicación entre diferentes dispositivos conectados a internet. De esta manera, podemos encontrar dentro de la arquitectura la capa de aplicación, la cual es primordial para la comunicación entre aplicaciones y servicios.

Por lo tanto, el siguiente proyecto tiene como objetivo explorar y enfatizar la aplicación de la capa de aplicación de la arquitectura TCP/IP, específicamente en el estudio del protocolo HTTP desde un punto de vista de programación en red. El protocolo HTTP(Hyper text Transfer Protocol) es el protocolo de comunicación utilizado en la World  Wide Web para la transferencia de datos de un servidor web a un cliente, actuando como un navegador web.

Para lograr este objetivo, se desarrollará e implementará un servidor web llamado Telematics Web Server (TWS), que tendrá como función principal la entrega de recursos web a los clientes que lo soliciten. Estos recursos pueden ser páginas HTML, archivos de estilo, imágenes, entre otros.

Para la implementación de este proyecto, se utilizará la versión del protocolo HTTP/1.1 para el servidor web TWS; el cual es uno de los protocolos más usados en la actualidad para la comunicación entre servidores web y clientes. En resumen, el proyecto TWS es una excelente oportunidad para sumergirse en el mundo de la programación de redes y explorar los diferentes aspectos del protocolo HTTP en un entorno práctico y real.
*******

<div id='development'/> 

### **2. Desarrollo**
Para el desarrollo de este proyecto, utilizamos el lenguaje de programación Python. A continuación se explicará a detalle el explorer del proyecto: 

## Carpeta api 

- **archivo constants.py**

//imagen 

El archivo constants.py contiene algunas constantes que utilizaremos para la configuracion del servidor web. A continuación se explica cada constante:

-> PORT: Esta constante tiene un valor de 8080 y representa el número de puerto en el que se va a ejecutar el servidor o algún otro servicio.

-> ENCONDING_FORMAT: Esta constante tiene un valor de "UTF-8" y representa el formato de codificación de caracteres que se utilizará en el servidor o en algún otro servicio.

-> RECV_BUFFER_SIZE: Esta constante tiene un valor de 4096 y representa el tamaño del búfer de recepción utilizado para recibir datos del cliente en el servidor.

-> IP_SERVER: Esta constante tiene un valor de '172.31.92.75' y representa la dirección IP del servidor.

-> GET: Esta constante tiene un valor de 'GET' y representa el método HTTP utilizado para solicitar recursos del servidor.

-> HEAD: Esta constante tiene un valor de 'HEAD' y representa el método HTTP utilizado para solicitar solo los encabezados de respuesta del servidor.

-> POST: Esta constante tiene un valor de 'POST' y representa el método HTTP utilizado para enviar datos al servidor.

-> QUIT: Esta constante tiene un valor de 'QUIT' y representa el comando utilizado para cerrar una conexión TCP.

-> SERVER: Esta constante tiene un valor de 'Apache/2.4.41 (Ubuntu)' y representa el servidor web utilizado para alojar el sitio web o la aplicación en el servidor.



- **archivo error400.py**

//imagen

El proposito principal del código en el archivo error400.py es definir una función llamada "error" que recibe como parámetro una cadena de texto que representa la ruta de un archivo.Por lo tanto,  esta función se utiliza para gestionar errores 400 que se puedan presentar en nuestro servidor web.

ademas, en el código se empieza por obtener la ruta del archivo, la cual utiliza la función os.getcwd() para obtener la ruta del directorio actual donde se está ejecutando el programa y os.path.join() para unir la ruta del directorio actual con la ruta del archivo. Para despue, abrir el archivo en modo de lectura y que este lea su contenido con el método read().

Posteriormente, se obtienen algunas características del archivo como la fecha y hora de creación (ttime), el tipo de contenido (content_type) y la longitud del contenido (content_length). Para obtener el tipo de contenido utilizamos la librería mimetypes y su método guess_type(), el cual nos devuelve el tipo de contenido a partir de la extensión del archivo.

Finalmente, se crea un diccionario llamado answer que contiene toda la información anteriormente mencionada, incluyendo el contenido del archivo. Este diccionario es lo que se devuelve al llamar la función error(), y se utiliza para generar una respuesta HTTP que indica el error 400; y que contiene toda la información necesaria para que el cliente pueda entender el error y en consecuencia solucionarlo.



- **archivo get.py**

//imagen

El proposito principal del código en el archivo get.py es definir una función llamada "get" que recibe como parámetro una cadena de texto que representa la ruta de un archivo. Esta función se utiliza para manejar solicitudes GET en un servidor web. Lo primero que hacemos es comprobar si la ruta es el directorio raíz "/", en cuyo caso se asume que se está solicitando el archivo "index.html". De no ser este el caso, se elimina la barra inicial del camino para poder trabajar con la ruta del archivo. 

Luego, se obtiene la ruta completa del archivo utilizando las funciones os.getcwd() y os.path.join(). La función try-except se utiliza para intentar abrir el archivo en modo de lectura ("r"), y si esto falla, se intenta abrir el archivo en modo de lectura binaria ("rb"). Obteniendo asi, algunas características del archivo como la fecha y hora de creación (ttime), el tipo de contenido (content_type) y la longitud del contenido (content_length), utilizando los mismos métodos que mencionamos anteriormente en el archivo error400.py.

Finalmente, se crea un diccionario llamado answer que contiene toda la información anteriormente mencionada, incluyendo el contenido del archivo. Este diccionario es lo que se devuelve al llamar la función get(), y se utiliza para generarnos una respuesta HTTP que contiene toda la información necesaria para que el cliente pueda descargar el archivo solicitado.



- **archivo head.py**

//imagen 



*******

<div id='conclusion'/> 

### **3. Conclusiones**
En conclusión, el proyecto de desarrollo e implementación del servidor web Telematics Web Server (TWS) se enfocó en explorar la aplicación de la capa de aplicación de la arquitectura TCP/IP, específicamente en el estudio y programación del protocolo HTTP desde una perspectiva de red. La principal función de un servidor web es la entrega de recursos web a los clientes que lo solicitan, y para ello se utilizamos el protocolo HTTP en su versión 1.1.

Para lograr este proyecto, se llevó a cabo una implementación detallada del servidor web, que incluyó el manejo de solicitudes HTTP GET, HEAD y POST, así como la generación de respuestas correspondientes, incluyendo códigos de estado, descripciones, fechas, tipos de contenido y longitudes. Además, se implementaron errores HTTP, incluyendo el código de estado 400 (solicitud incorrecta), 404 (no encontrado) y 405 (método no permitido).

El servidor web TWS también se diseñó para ser escalable y permitir la conexión de múltiples clientes simultáneamente mediante el uso de hilos de ejecución. Se utilizó la biblioteca estándar de Python, incluyendo los módulos socket y threading, así como otras bibliotecas personalizadas que se crearon para manejar solicitudes y generar respuestas.

En resumen, el proyecto fue un éxito en términos de implementar un servidor web funcional que cumple con los requisitos de HTTP/1.1 y que puede manejar múltiples conexiones de clientes de manera simultánea. Además, el proyecto permitió a los desarrolladores profundizar en el conocimiento de la programación de red y en el uso de la biblioteca estándar de Python para crear aplicaciones de red complejas. Este proyecto también puede servir como una base sólida para proyectos futuros que involucren la programación de aplicaciones de red complejas.
*******

<div id='references'/> 

### **4. Referencias**

*******

