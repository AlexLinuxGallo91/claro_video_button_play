import datetime
import json
import time
import logging

from python3_gearman import GearmanClient
from python3_gearman.errors import ServerUnavailable

from utils.client_gearman_utils import ClientGearmanUtils
from utils.html_utils import HtmlUtils
from utils.json_utils import JsonUtils
from utils.mail_utils import MailUtils
from utils.xlsx_utils import XlsxUtils
from utils.file_utils import FileUtils

begin_time = time.time()
ip = 'localhost'
port = '4771'
gm_client = GearmanClient(['{}:{}'.format(ip, port)])
path_dir_save_file_xlsx = './xlsx_play_button_reports'
gmail_account = ''
gmail_password = ''
claro_video_account = ''
claro_video_pass_account = ''
time_wait_in_seconds = 7200  # 2 hrs
json_list_errors_result = []
debug_mode = False  # Bandera para entrar en modo Debug
filename_log = './claro_video_play_button.log'

# inicializa el logger
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    filename=filename_log
)

# Bandera para generar mas de 100 errores y enviar el correo con el reporte xlsx adjunto
debug_mode_send_email_with_report_xlsx = False

# lista de destinatarios a enviar las notificaciones
email_addresses = [
    'alexis.araujo@triara.com',
    # 'jose.hernandez@triara.com',
    # 'gerardo.trevino@triara.com',
    # 'noc.operaciones@triara.com',
    # 'angel.galindo@triara.com'
]

logging.info('Inicializando ejecucion del script.')

# se obtiene la lista de jobs por ejecutar, con sus distintos node_id y filter_id
job_list = ClientGearmanUtils.generate_gearman_job_list(
    user=claro_video_account, password=claro_video_pass_account)

for job_task_arg in job_list:
    json_args = json.loads(job_task_arg['data'])
    region = json_args['region']
    logging.info('nodo en revision: {} de la region {}'.format(json_args['node_name'], region))

    try:
        submitted_job = gm_client.submit_job(
            job_task_arg['task'], job_task_arg['data'], poll_timeout=time_wait_in_seconds)

        text_result_job = submitted_job.result
    except ServerUnavailable as e:
        logging.info('Sucedio un error al intentar enviar el Job al Worker, worker no disponible: {}'.format(e))
        continue

    try:
        json_result = json.loads(text_result_job)

        if 'result' in json_result:
            list_errors_obtained = JsonUtils.exist_errors_in_play_button_data(json_result, debug_mode)
            logging.info('Numero de errores obtenidos en el nodo {}: {}'.format(
                json_args['node_name'], len(list_errors_obtained)))
            json_list_errors_result.extend(list_errors_obtained)

    except ValueError as e:
        logging.info('Sucedio un error ValueError al momento de convertir el resultado string del job a json: {}.\n '
                     'resultado obtenido: {}'.format(e, text_result_job))

    except TypeError as e:
        logging.info('Sucedio un error TypeError al momento de convertir el resultado string del job a json: {}.\n '
                     'resultado obtenido: {}'.format(e, text_result_job))

# verifica que al menos no haya algun error localizado en la lista de errores/validaciones de las vigencias y push
# buttons, en caso contrario, se envia la notificacion por email
errors_count = len(json_list_errors_result)

# modo debug para enviar el correo con mas de 100 errores simulados
if 0 < errors_count < 100 and debug_mode_send_email_with_report_xlsx:
    while errors_count < 200:
        copy_list_errors = json_list_errors_result[:]
        json_list_errors_result.extend(copy_list_errors)
        errors_count = len(json_list_errors_result)

logging.info('Numero de incidencias encontradas en total: {}'.format(errors_count))

if errors_count >= 100:
    # verifica que el folder de los reportes exista, de lo contrario intenta crearlo. Se crea el nuevo reporte xlsx
    FileUtils.check_folder_reports_exists(path_dir_save_file_xlsx)
    path_report_xlsx_to_create = XlsxUtils.generate_report_xlsx_path_str(path_dir_save_file_xlsx)
    XlsxUtils.create_xlsx_file_from_list_json_data_errors(json_list_errors_result, path_report_xlsx_to_create)

    # se envia correo con el reporte adjunto por medio de una cuenta de correo de gmail
    subject = HtmlUtils.generate_subject_email_by_list_play_button_errors(json_list_errors_result, region)
    MailUtils.send_email_with_google_account_and_file_attach(
        gmail_account, gmail_password, path_report_xlsx_to_create, subject, email_addresses)

    # por ultimo para no ocupar tanto espacio en el disco, se elmimina el reporte generado en el path del server
    FileUtils.remove_file_from_path_str(path_report_xlsx_to_create)

    logging.info('Se envio el correo con archivo excel adjunto: {}'.format(path_report_xlsx_to_create))

# si son menos de 100 errores encontrados, se envia el correo sin generar un reporte xlsx, por medio de la api de
# correo y en texto HTML
elif 0 < errors_count < 100:
    html_body_message = HtmlUtils.generate_html_table_errors_push_buttons(json_list_errors_result)
    subject = HtmlUtils.generate_subject_email_by_list_play_button_errors(json_list_errors_result, region)
    resp = MailUtils.send_email(email_addresses, 'notificacion.itoc@triara.com', subject, html_body_message)
    logging.info(resp.text)

else:
    logging.info('Analisis exitoso, no se encontraron inconsistencias en los nodos verificados.')

time_obtained = time.time() - begin_time
time_obtained = str(datetime.timedelta(seconds=time_obtained))
logging.info('tiempo total de finalizacion de ejecucion del script: {}'.format(time_obtained))
