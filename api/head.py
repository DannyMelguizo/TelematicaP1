import time
import os
import constants
import type


def head(path):

    #Se busca el archivo en ruta especificada por la petición
    #Si es / se establecera index.html por defecto
    if path == '/':
        path = 'index.html'

    else:
        path = path[1:]

    rt = os.getcwd()
    new_path = os.path.join(str(os.path.dirname(rt)), path)
    file_stat = os.stat(new_path)

    #Se determinan las diferentes cualidades del archivo y se establece la fecha de la petición
    ttime = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    content_type = type.mimetype(new_path)
    content_length = file_stat.st_size

    #Respuesta a la petición
    answer = {
        'Date' : ttime,
        'Content-Type' : f'{content_type} ; {constants.ENCONDING_FORMAT}',
        'Content-Length' : content_length,
    }

    return answer