import json

from python3_gearman import GearmanClient

import constants.constants as const
from utils.client_gearman_utils import ClientGearmanUtils
from utils.html_utils import HtmlUtils
from utils.json_utils import JsonUtils
from utils.mail_utils import MailUtils

gm_client = GearmanClient(['localhost:4771'])

json_list_errors_result = []

# lista de destinatarios a enviar las notificaciones
email_addresses = ['alexis.araujo@triara.com',
                   'jose.hernandez@triara.com',
                   'gerardo.trevino@triara.com']

# se obtiene la lista de jobs por ejecutar, con sus distintos node_id y filter_id
job_list = ClientGearmanUtils.generate_gearman_job_list()

# se mandan a ejecutar la lista de jobs a los distintos worker
submitted_requests = gm_client.submit_multiple_jobs(job_list, background=False, wait_until_complete=False)

# se espera a que todos los jobs se hayan finalizado, en caso de que un job sobrepase 300 segundos, se omite
completed_jobs = gm_client.wait_until_jobs_completed(submitted_requests, poll_timeout=300)

# bandera para debug
modo_debug = True

for job_finished in completed_jobs:
    try:
        result = job_finished.result
        print(result)
        json_result = json.loads(result)

        if 'result' in json_result:
            list_errors_obtained = JsonUtils.exist_errors_in_play_button_data(json_result, modo_debug)
            json_list_errors_result.extend(list_errors_obtained)

    except ValueError:
        pass
    except TypeError as e:
        pass

# verifica que al menos no haya algun error localizado en la lista de errores/validaciones de las vigencias y push
# buttons, en caso contrario, se envia la notificacion por email
if len(json_list_errors_result) > 0:
    numero_de_errores = len(json_list_errors_result)

    print('numero de errores: {}'.format(numero_de_errores))
    HTML = HtmlUtils.generate_html_table_errors_push_buttons(json_list_errors_result)
    subject = const.SUBJECT_MAIL_INCONSISTENCIA_PLAY_BUTTON
    resp = MailUtils.send_email(email_addresses, 'notificacion.itoc@triara.com', subject, HTML)
    print(resp.text)