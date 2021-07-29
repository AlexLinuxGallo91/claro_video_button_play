import json

import requests

from id_group_data.id_group_api_data import IdGroupApi
from login_claro_video.claro_video_login import LoginClaroVideo
from utils.iterable_utils import IterableUtils
from utils.multithreading_utils import MultithreadingUtils
from utils.arguments_utils import ArgumentsUtils
from utils.json_utils import JsonUtils
import sys


def main_with_json_param(json_arg: dict):


    # DEBUG
    sys.stderr.write('ESTOY ENTRANDO EN MODO DEBUG!!!!!!!\n\n')


    session = requests.Session()
    group_id_list = None
    result_purchase_button_list = []

    """
    se obtienen las variables y valores necesarios del argumento JSON
    """
    script_arg_user = json_arg['user']
    script_arg_password = json_arg['password']
    script_arg_region = json_arg['region']
    script_arg_filter_id = json_arg['filter_id']
    script_arg_node_id = json_arg['node_id']

    """
    se obtiene el nodo por medio del filter id y el node id
    """
    nodo_obtained = JsonUtils.verify_node_by_filter_and_node_id(
        ArgumentsUtils.convert_string_to_int(script_arg_node_id),
        ArgumentsUtils.convert_string_to_int(script_arg_filter_id)
    )

    print('nodo obtenido: {}'.format(nodo_obtained))
    """
    Se realiza la obtencion de la lista de IdGroup de cada una de las series por la region, filter_id y node_id definidos
    """
    id_group_json = IdGroupApi().main(script_arg_node_id, script_arg_filter_id, script_arg_region)
    group_id_list = id_group_json['idgrups']

    """
    Se genera la llave hks con un string alfanumerico aleatorio de 26 caracteres
    """
    hks = LoginClaroVideo.generate_hks()
    """
    Se obtiene la llave authpt por medio de webscrapping de la pagina principal de claro video
    """
    authpt = LoginClaroVideo.get_authpt(session)

    # acquired_resp_data = LoginClaroVideo.get_starter_header_info(authpt, hks, session)
    """
    Se realiza una peticion a la api con las credenciales del usuario y se inicia sesion en la plataforma, obteniendo
    los tokens requeridos
    """
    acquired_resp_data = LoginClaroVideo.login_portal(
        script_arg_user, script_arg_password, session, authpt, hks, script_arg_region)

    """
    Se realiza una peticion a la url de push session, este paso es necesario para poder ingresar correctamente a la 
    plataforma y tener acceso a la informacion de los play button en la peticiones web posteriores
    """
    acquired_resp_data = LoginClaroVideo.push_session(acquired_resp_data, session, script_arg_region)

    """
    se itera por grupos/pedazos de 49 ids y se realiza las peticiones de manera paralela para obtener la informacion
    del play button y la fecha de vigencia.
    """
    for chunk_id in IterableUtils.chunker(group_id_list, 49):
        result_purchase_button_list.extend(
            MultithreadingUtils.process_data_id_group_requests(
                chunk_id, session, acquired_resp_data, json_arg['region'], nodo_obtained))

    """
    Se convierte el array y dictionario final en una cadena en formato JSON y se imprime en consola
    """
    result_purchase_button_list = {'result': result_purchase_button_list}
    json_string = json.dumps(result_purchase_button_list)
    session.close()

    return json_string

#
# if __name__ == '__main__':
#     main()
