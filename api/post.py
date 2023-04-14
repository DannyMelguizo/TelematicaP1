import time
import os
import constants
import mimetypes


def post(path):

    #Se busca el archivo en ruta especificada por la petición
    path = path[1:]
    rt = os.getcwd()
    new_path = os.path.join(str(os.path.dirname(rt)), path)


    file = open(new_path, 'r')
    file = file.read()

    #Se determinan las diferentes cualidades del archivo y se establece la fecha de la petición
    ttime = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    content_type = mimetypes.guess_type(new_path)[0]
    content_length = os.path.getsize(new_path)

    #Respuesta a la petición
    answer = {
        'Date' : ttime,
        'Content-Type' : f'{content_type} ; {constants.ENCONDING_FORMAT}',
        'Content-Length' : content_length,
        'file' : file
    }

    return answer