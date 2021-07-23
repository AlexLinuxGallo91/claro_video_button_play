import json
from utils.json_utils import JsonUtils
from utils.html_utils import HtmlUtils
from python3_gearman import GearmanClient
from utils.client_gearman_utils import ClientGearmanUtils
from constants import constants as const
from utils.mail_utils import MailUtils

gm_client = GearmanClient(['localhost:4770'])

job_list = []
lista_correos_destinatarios = ['alexis.araujo@triara.com',
                               'jose.hernandez@triara.com',
                               'gerardo.trevino@triara.com'
                               ]

# se establece una lista con los jobs a ejecutar, donde cada job contiene la region establecida y cada uno de los
# filte id para la obtencion de los datos de fechas de vigencia y estado del play button
job_list = ClientGearmanUtils.set_list_jobs()

# se cargan o mandan los jobs al worker
submitted_requests = gm_client.submit_multiple_jobs(job_list, background=False, wait_until_complete=False)

# si sobrepasa mas de 300 segundos, no regresa nada, se detiene la ejecucion del job y de resultado se obtiene un None
completed_requests = gm_client.wait_until_jobs_completed(submitted_requests, poll_timeout=300.0)

lista_result_response = []
json_error = {}
json_error['error'] = []

# DEBUG
modo_debug = True

for job_finished in completed_requests:
    result = job_finished.result
    try:
        json_job_result = json.loads(result)
        lista_result_response.append(json_job_result)
    except ValueError:
        pass
    except TypeError:
        pass

json_result = {}
json_result['response'] = lista_result_response
json_result_texto = json.dumps(json_result, indent=4)

list_errors = JsonUtils.exist_errors_in_play_button_data(json_result, modo_debug)

# verifica que al menos no haya algun error localizado en la lista de errores/validaciones de las vigencias y push
# buttons, en caso contrario, se envia la notificacion por email
if len(list_errors) > 0:
    HTML = HtmlUtils.generar_html_table_errores_imagenes(json_result)
    subject = const.SUBJECT_MAIL_INCONSISTENCIA_PLAY_BUTTON
    resp = MailUtils.send_email(lista_correos_destinatarios, 'notificacion.itoc@triara.com', subject, HTML)
    print(resp.text)

