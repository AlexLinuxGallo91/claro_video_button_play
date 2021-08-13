import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List
from pathlib import Path

import requests

import constants.constants as const


class MailUtils:

    @staticmethod
    def send_email_with_google_account_and_file_attach(gmail, password, path_file, subject, email_addreses):
        path_file_to_send = Path(path_file)
        mail_body = const.HTML_BODY_EMAIL_GMAIL_MESSAGE
        sender_address = gmail
        sender_pass = password

        message = MIMEMultipart('alternative')
        message['From'] = sender_address
        message['To'] = ','.join(email_addreses)
        message['Subject'] = subject
        message.preamble = """
        Your mail reader does not support the report format.
        Please visit us online!
        """

        message.attach(MIMEText(mail_body, 'html'))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(path_file, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(path_file_to_send.name))
        message.attach(part)

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        session.sendmail(sender_address, ','.join(email_addreses), message.as_string())
        session.quit()

    @staticmethod
    def send_email(lista_destinatarios: List, p_from, subject, body):
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
