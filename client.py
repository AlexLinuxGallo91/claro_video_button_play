import datetime
import json
import time

from python3_gearman import GearmanClient

from utils.client_gearman_utils import ClientGearmanUtils
from utils.html_utils import HtmlUtils
from utils.json_utils import JsonUtils
from utils.mail_utils import MailUtils

tiempo_de_inicio = time.time()
ip = 'localhost'
port = '4471'
#port = '4730'
gm_client = GearmanClient(['{}:{}'.format(ip, port)])

json_list_errors_result = []

# lista de destinatarios a enviar las notificaciones
email_addresses = ['alexis.araujo@triara.com',
                   'jose.hernandez@triara.com',
                   'gerardo.trevino@triara.com']

# se obtiene la lista de jobs por ejecutar, con sus distintos node_id y filter_id
job_list = ClientGearmanUtils.generate_gearman_job_list(user='', password='')
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

print('\nnumero total de errores obtenidos: {}'.format(len(json_list_errors_result)))

# while len(json_list_errors_result) >= 150:
#     del json_list_errors_result[-1]

# while len(json_list_errors_result) <= 200:
#     list_copy = json_list_errors_result.copy()
#     json_list_errors_result = json_list_errors_result.extend(list_copy)

print('Numero de errores a enviar por medio del debug (se redujo a un numero menor): {}'.
      format(len(json_list_errors_result)))

# verifica que al menos no haya algun error localizado en la lista de errores/validaciones de las vigencias y push
# buttons, en caso contrario, se envia la notificacion por email
if len(json_list_errors_result) > 0:
    HTML = HtmlUtils.generate_html_table_errors_push_buttons(json_list_errors_result)
    subject = HtmlUtils.generate_subject_email_by_list_play_button_errors(json_list_errors_result, region)
    resp = MailUtils.send_email(email_addresses, 'notificacion.itoc@triara.com', subject, HTML)
    print(resp.text)

tiempo_obtenido = time.time() - tiempo_de_inicio
tiempo_obtenido = str(datetime.timedelta(seconds=tiempo_obtenido))
print('tiempo total de finalizacion de ejecucion del script: {}'.format(tiempo_obtenido))
