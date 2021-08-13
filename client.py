import datetime
import json
import time

from python3_gearman import GearmanClient

from utils.client_gearman_utils import ClientGearmanUtils
from utils.html_utils import HtmlUtils
from utils.json_utils import JsonUtils
from utils.mail_utils import MailUtils
from utils.xlsx_utils import XlsxUtils

begin_time = time.time()
ip = 'localhost'
# port = '4471'
port = '4730'
gm_client = GearmanClient(['{}:{}'.format(ip, port)])
path_dir_save_file_xlsx = './xlsx_play_button_reports'
gmail_account = ''
gmail_password = ''
claro_video_account = ''
claro_video_pass_account = ''

json_list_errors_result = []

# lista de destinatarios a enviar las notificaciones
email_addresses = ['alexis.araujo@triara.com',
                   'jose.hernandez@triara.com',
                   'gerardo.trevino@triara.com']

# se obtiene la lista de jobs por ejecutar, con sus distintos node_id y filter_id
job_list = ClientGearmanUtils.generate_gearman_job_list(user=claro_video_account, password=claro_video_pass_account)
region = ''

# bandera para debug
modo_debug = False

for job_task_arg in job_list:
    json_args = json.loads(job_task_arg['data'])
    region = json_args['region']
    print('nodo en revision: {} de la region {}'.format(json_args['node_name'], region))

    submitted_job = gm_client.submit_job(job_task_arg['task'], job_task_arg['data'], poll_timeout=3600)
    text_result_job = submitted_job.result

    try:
        json_result = json.loads(text_result_job)

        if 'result' in json_result:
            list_errors_obtained = JsonUtils.exist_errors_in_play_button_data(json_result, modo_debug)
            json_list_errors_result.extend(list_errors_obtained)

    except ValueError as e:
        print('Sucedio un error ValueError al momento de convertir el resultado string del job a json: {}.\n '
              'resultado obtenido: {}'.format(e, text_result_job))

    except TypeError as e:
        print('Sucedio un error TypeError al momento de convertir el resultado string del job a json: {}.\n '
              'resultado obtenido: {}'.format(e, text_result_job))

    # verifica que al menos no haya algun error localizado en la lista de errores/validaciones de las vigencias y push
    # buttons, en caso contrario, se envia la notificacion por email
    errors_count = len(json_list_errors_result)

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
        XlsxUtils.create_xlsx_file_from_list_errors(json_list_errors_result, path_xlsx_file)

        subject = HtmlUtils.generate_subject_email_by_list_play_button_errors(json_list_errors_result, region)
        MailUtils.send_email_with_google_account_and_file_attach(
            gmail_account, gmail_password, path_xlsx_file, subject, email_addresses)

    elif 0 < errors_count < 100:
        html_body_message = HtmlUtils.generate_html_table_errors_push_buttons(json_list_errors_result)
        subject = HtmlUtils.generate_subject_email_by_list_play_button_errors(json_list_errors_result, region)
        resp = MailUtils.send_email(email_addresses, 'notificacion.itoc@triara.com', subject, html_body_message)
        print(resp.text)

    else:
        print('No se encontraron de manera exitosa, inconsistencias en los nodos.')

    tiempo_obtenido = time.time() - begin_time
    tiempo_obtenido = str(datetime.timedelta(seconds=tiempo_obtenido))
    print('tiempo total de finalizacion de ejecucion del script: {}'.format(tiempo_obtenido))
