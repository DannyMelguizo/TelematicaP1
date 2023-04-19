import time
import os
import constants
import mimetypes

def get(path):

    #Se busca el archivo en ruta especificada por la petición
    #Si es / se establecera index.html por defecto
    if path == '/':
        path = 'index.html'

    else:
        path = path[1:]

    rt = os.getcwd()
    new_path = os.path.join(str(os.path.dirname(rt)), path)

    #Se intenta abrir el archivo y se leera normalmente, en caso de haber error, lo leera como bytes
    try:
        file = open(new_path, 'r')
        file = file.read()
    except:
        file = open(new_path, 'rb')
        file = file.read()

    file_stat = os.stat(new_path)

    #Se determinan las diferentes cualidades del archivo y se establece la fecha de la petición
    ttime = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    content_type = mimetypes.guess_type(new_path)[0]
    content_length = file_stat.st_size
    last_modified = file_stat.st_mtime

    etag_str = str(last_modified) + str(content_length)
    etag_str = hash(etag_str)

    etag = hex(etag_str)[2:]
    last_modified = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(last_modified))


    #respuesta a la petición
    answer = {
        'Date' : ttime,
        'Content-Type' : f'{content_type} ; {constants.ENCONDING_FORMAT}',
        'Content-Length' : content_length,
        'file' : file,
        'ETag' : etag,
        'Last-Modified' : last_modified
    }

    return answer

