import json

from python3_gearman import GearmanWorker

import constants.constants as const
from main import main_with_json_param

######################################################################################
##                        WORKER PYTHON GEARMAN CLARO VIDEO                         ##
##                                  PUSH BUTTON                                     ##
##                                                                                  ##
##  Modulo/Worker en python el cual realiza el test de los play buttton             ##
##  en la plataforma de Claro Video                                                 ##
######################################################################################

# se define el worker, host y puerto al que estara a la escucha de cada peticion
# para realizar un nuevo Job
host = '127.0.0.1'
puerto = '4770'
worker = GearmanWorker(['{}:{}'.format(host, puerto)])


# funcion encarga de comunicarse al modulo de experiencia de usuario OWA
# el cual como resultado se obtiene una cadena en formato JSON
def test_claro_video_play_button(gearman_worker, gearman_job):
    hubo_error = False
    msg_error = ''
    arg = gearman_job.data

    """debug"""
    print('entrando al worker: {}'.format(arg))

    # valida que el texto sea un json
    try:
        print('intentando convertir el json')
        json_arg = json.loads(arg)
    except ValueError:
        msg_error = 'El argumento no es un json valido, favor de establecer el argumento correctamente.'
        hubo_error = True
        print('oopsie')

    # valida que se encuentre la regios y el nodo establecido
    if const.ARG_USER not in json_arg:
        msg_error = 'Favor de establecer el parametro user dentro del JSON'
        hubo_error = True
    elif const.ARG_PASSWORD not in json_arg:
        msg_error = 'Favor de establecer el parametro password dentro del JSON'
        hubo_error = True
    elif const.ARG_REGION not in json_arg:
        msg_error = 'Favor de establecer el parametro region dentro del JSON'
        hubo_error = True
    elif const.ARG_FILTER_ID not in json_arg:
        msg_error = 'Favor de establecer el parametro filter_id dentro del JSON'
        hubo_error = True
    elif const.ARG_NODE_ID not in json_arg:
        msg_error = 'Favor de establecer el parametro node_id dentro del JSON'
        hubo_error = True

    try:
        response = main_with_json_param(json_arg)
    except Exception as e:
        hubo_error = True
        msg_error = 'Sucedio un error dentro de la ejecucion princial del Script: {}'.format(e)

    if hubo_error:
        print('valio :(')
        response_error = {}
        response_error['msg'] = msg_error
        response_error['error'] = hubo_error
        return json.dumps(response_error)
    else:
        return response


worker.register_task('test_claro_video_play_button', test_claro_video_play_button)
worker.work()
