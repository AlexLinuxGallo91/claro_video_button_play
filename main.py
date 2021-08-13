import copy
import json
import datetime
import requests
import time
from id_group_data.id_group_api_data import IdGroupApi
from login_claro_video.claro_video_login import LoginClaroVideo
from utils.iterable_utils import IterableUtils
from utils.multithreading_utils import MultithreadingUtils
import constants.constants as const
from utils.json_utils import JsonUtils
from utils.html_utils import HtmlUtils
from utils.mail_utils import MailUtils
from utils.xlsx_utils import XlsxUtils


def main_with_json_param(json_arg: dict):
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
    nodo_obtained = json_arg['node_name']

    print('nodo obtenido: {}'.format(nodo_obtained))
    """
    Se realiza la obtencion de la lista de IdGroup de cada una de las series por la region, filter_id y node_id 
    definidos
    """
    id_group_json = IdGroupApi().main(script_arg_node_id, script_arg_filter_id, script_arg_region)

    group_id_list = id_group_json['idgrups']

    print('id groups obtenidos: {}'.format(len(group_id_list)))

    """
    Se genera la llave hks con un string alfanumerico aleatorio de 26 caracteres
    """
    hks = LoginClaroVideo.generate_hks()

    """
    Se obtiene la llave authpt por medio de webscrapping de la pagina principal de claro video
    """
    authpt = LoginClaroVideo.get_authpt(session)

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


def main_test_with_each_node(user_login_claro_video: str, password_login_claro_video: str, debug_mode: bool,
                             path_dir_save_file_xlsx: str, gmail_account: str, gmail_password: str):
    tiempo_de_inicio = time.time()
    list_nodos = []
    list_errors_final_result = []

    email_addresses = ['alexis.araujo@triara.com',
                       'jose.hernandez@triara.com',
                       'gerardo.trevino@triara.com']

    param_dict = {
        "user": user_login_claro_video,
        "password": password_login_claro_video,
        "region": "mexico",
        "filter_id": "",
        "node_id": "",
        "node_name": ""
    }

    for nodo in const.DICT_NODOS:
        dict_copy = copy.deepcopy(param_dict)
        dict_copy['filter_id'] = nodo['filter_id']
        dict_copy['node_id'] = nodo['node_id']
        dict_copy['node_name'] = nodo['node_name']
        list_nodos.append(dict_copy)

    for json_data_nodo in list_nodos:

        region = json_data_nodo['region']
        node_name = json_data_nodo['node_name']
        print('nodo en revision: {} de la region {}'.format(node_name, region))

        text_json_result = main_with_json_param(json_data_nodo)
        json_result = json.loads(text_json_result)

        if 'result' in json_result:
            print('\n\nNumero de group_id\'s con inconsistencias localizados: {}'.format(len(json_result['result'])))
            list_errors = JsonUtils.exist_errors_in_play_button_data(json_result, debug_mode)
            list_errors_final_result.extend(list_errors)

    # verifica que al menos no haya algun error localizado en la lista de errores/validaciones de las vigencias y push
    # buttons, en caso contrario, se envia la notificacion por email
    errors_count = len(list_errors_final_result)

    # # debug
    # if 0 < errors_count < 100:
    #     while errors_count < 500:
    #         copy_list_errors = list_errors_final_result[:]
    #         list_errors_final_result.extend(copy_list_errors)
    #         errors_count = len(list_errors_final_result)

    if errors_count >= 100:
        date_now_xlsx_file = datetime.datetime.now().strftime('%m_%d_%Y__%H_%M_%S')
        xlsx_filename = 'play_button_result_{}.xlsx'.format(date_now_xlsx_file)
        path_xlsx_file = '{}/{}'.format(path_dir_save_file_xlsx, xlsx_filename)
        XlsxUtils.create_xlsx_file_from_list_errors(list_errors_final_result, path_xlsx_file)

        subject = HtmlUtils.generate_subject_email_by_list_play_button_errors(list_errors_final_result, region)
        MailUtils.send_email_with_google_account_and_file_attach(
            gmail_account, gmail_password, path_xlsx_file, subject, email_addresses)

    elif 0 < errors_count < 100:
        html_body_message = HtmlUtils.generate_html_table_errors_push_buttons(list_errors_final_result)
        subject = HtmlUtils.generate_subject_email_by_list_play_button_errors(list_errors_final_result, region)
        resp = MailUtils.send_email(email_addresses, 'notificacion.itoc@triara.com', subject, html_body_message)
        print(resp.text)

    tiempo_obtenido = time.time() - tiempo_de_inicio
    tiempo_obtenido = str(datetime.timedelta(seconds=tiempo_obtenido))
    print('tiempo total de finalizacion de ejecucion del script: {}'.format(tiempo_obtenido))


if __name__ == '__main__':
    main_test_with_each_node('clarovideomty01@gmail.com', 'C14r0.V1de0.12', True, './xlsx_data_generated',
                             'devagallo91y@gmail.com', 'pythonlove91')
