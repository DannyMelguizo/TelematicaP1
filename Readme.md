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

- Carpeta api 
archivo constants.py

//imagen 

El archivo constant.py contiene algunas constantes que utilizaremos para la configuracion del servidor web. A continuación se explica cada constante:

- PORT: Esta constante tiene un valor de 8080 y representa el número de puerto en el que se va a ejecutar el servidor o algún otro servicio.

- ENCONDING_FORMAT: Esta constante tiene un valor de "UTF-8" y representa el formato de codificación de caracteres que se utilizará en el servidor o en algún otro servicio.

- RECV_BUFFER_SIZE: Esta constante tiene un valor de 4096 y representa el tamaño del búfer de recepción utilizado para recibir datos del cliente en el servidor.

- IP_SERVER: Esta constante tiene un valor de '172.31.92.75' y representa la dirección IP del servidor.

- GET: Esta constante tiene un valor de 'GET' y representa el método HTTP utilizado para solicitar recursos del servidor.

- HEAD: Esta constante tiene un valor de 'HEAD' y representa el método HTTP utilizado para solicitar solo los encabezados de respuesta del servidor.

- POST: Esta constante tiene un valor de 'POST' y representa el método HTTP utilizado para enviar datos al servidor.

- QUIT: Esta constante tiene un valor de 'QUIT' y representa el comando utilizado para cerrar una conexión TCP.

- SERVER: Esta constante tiene un valor de 'Apache/2.4.41 (Ubuntu)' y representa el servidor web utilizado para alojar el sitio web o la aplicación en el servidor.

*******

<div id='conclusion'/> 

### **3. Conclusiones**

*******

<div id='references'/> 

### **4. Referencias**

*******

