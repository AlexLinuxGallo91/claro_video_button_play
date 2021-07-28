import json

from python3_gearman import GearmanClient
import sys
from utils.client_gearman_utils import ClientGearmanUtils

gm_client = GearmanClient(['localhost:4770'])

lista_correos_destinatarios = ['alexis.araujo@triara.com',
                               'jose.hernandez@triara.com',
                               'gerardo.trevino@triara.com'
                               ]

# se cargan o mandan los jobs al worker
data = ClientGearmanUtils.set_job_data_dict()
job = gm_client.submit_job(task='test_claro_video_play_button', data=data,
                           background=False, wait_until_complete=True, poll_timeout=300.0)

json_error = {}
json_error['error'] = []

# bandera para debug
modo_debug = True

try:
    json_job_result = json.loads(job.result)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)

json_result_text = json.dumps(json_job_result, indent=4)

if 'error' in json_result_text:
    print(json_result_text['error'])
    sys.exit(1)

# list_errors = JsonUtils.exist_errors_in_play_button_data(json_job_result, modo_debug)
#
# # verifica que al menos no haya algun error localizado en la lista de errores/validaciones de las vigencias y push
# # buttons, en caso contrario, se envia la notificacion por email
# if len(list_errors) > 0:
#     HTML = HtmlUtils.generate_html_table_errors_push_buttons(list_errors)
#     subject = const.SUBJECT_MAIL_INCONSISTENCIA_PLAY_BUTTON
#     resp = MailUtils.send_email(lista_correos_destinatarios, 'notificacion.itoc@triara.com', subject, HTML)
#     print(resp.text)
