from typing import List

import requests


class MailUtils:

    @staticmethod
    def send_email(lista_destinatarios:List, p_from, subject, body):
        url_api_mail = 'http://itoc-tools.triara.mexico:8083/notifications/email/html'

        data = {}
        data['from'] = p_from
        data['to'] = ','.join(lista_destinatarios)
        data['subject'] = subject
        data['body'] = body
        print('enviando correo de notificacion')
        response = requests.post(url_api_mail, data=data)
        print(response)
        return response
