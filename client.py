import json
import sys

from python3_gearman import GearmanClient
from utils.client_gearman_utils import ClientGearmanUtils

gm_client = GearmanClient(['localhost:4770'])

lista_constantes_imagenes = ['SUCCESS', 'FAILED']
pais_por_verificar = ''
job_list = []
contador_errores = 0
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
modo_debug = False

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

# print('{}\n'.format(json_result_texto))

# valida si existen imagenes corruptas, en caso de ser asi se forma una tabla HTML para su notificacion por correo
if JsonUtils.se_presentan_urls_imagenes_corruptas(json_result):
    HTML = HtmlUtils.generar_html_table_errores_imagenes(json_result)
    subject = MailUtils.subject_imagenes_dinamico(json_result)
    resp = MailUtils.send_email(lista_correos_destinatarios, 'notificacion.itoc@triara.com', subject, HTML)
    print(resp.text)

if JsonUtils.se_presentan_secuencias_corruptas(json_result):
    subject = MailUtils.subject_sequences_dinamico(json_result)
    HTML = HtmlUtils.generar_html_table_errores_secuencias(json_result)
    resp = MailUtils.send_email(lista_correos_destinatarios, 'notificacion.itoc@triara.com', subject, HTML)
    print(resp.text)
