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
    response_error = {
        'hubo_error': False,
        'msg_error': ''
    }

    arg = gearman_job.data

    # valida que el texto sea un json
    try:
        json_arg = json.loads(arg)
    except ValueError:
        response_error['msg_error'] = 'El argumento no es un json valido, favor de establecer el argumento ' \
                                      'correctamente.'
        response_error['hubo_error'] = True

    # valida que se encuentre la regios y el nodo establecido
    if response_error['hubo_error'] is False and const.ARG_USER not in json_arg:
        response_error['msg_error'] = 'Favor de establecer el parametro user dentro del JSON.'
        response_error['hubo_error'] = True

    elif response_error['hubo_error'] is False and const.ARG_PASSWORD not in json_arg:
        response_error['msg_error'] = 'Favor de establecer el parametro password dentro del JSON.'
        response_error['hubo_error'] = True

    elif response_error['hubo_error'] is False and const.ARG_REGION not in json_arg:
        response_error['msg_error'] = 'Favor de establecer el parametro region dentro del JSON.'
        response_error['hubo_error'] = True

    elif response_error['hubo_error'] is False and const.ARG_FILTER_ID not in json_arg:
        response_error['msg_error'] = 'Favor de establecer el parametro filter_id dentro del JSON.'
        response_error['hubo_error'] = True

    elif response_error['hubo_error'] is False and const.ARG_NODE_ID not in json_arg:
        response_error['msg_error'] = 'Favor de establecer el parametro node_id dentro del JSON.'
        response_error['hubo_error'] = True

    if response_error['hubo_error']:
        return json.dumps(response_error, indent=4)

    try:
        response = main_with_json_param(json_arg)
        response = json.dumps(response, indent=4)

    except Exception as e:
        response_error['msg_error'] = 'Sucedio un error en la ejecucion del worker: {}.'.format(e)
        response_error['hubo_error'] = True
        return json.dumps(response_error, indent=4)

    # en caso de que la ejecucion sea exitosa, se regresa el resultado en formato JSON
    return response


worker.register_task('test_claro_video_play_button', test_claro_video_play_button)
worker.work()
