import time
import os
import constants
import mimetypes


def post(path):
    
    state = '200 OK'

    if path != '/confirmacion.html':
        path = 'error/error405.html'
        state = '405 Method Not Allowed'
    else:
        path = path[1:]

    rt = os.getcwd() #Ruta del directorio actual
    new_path = os.path.join(str(os.path.dirname(rt)), path)

    file = open(new_path, 'r')
    file = file.read()
    ttime = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    content_type = mimetypes.guess_type(new_path)[0]
    content_length = os.path.getsize(new_path)

    answer = {
        'Date' : ttime,
        'Server' : constants.SERVER,
        'Content-Type' : f'{content_type} ; {constants.ENCONDING_FORMAT}',
        'Content-Length' : content_length,
        'file' : file,
        'state': state
    }

    return answer