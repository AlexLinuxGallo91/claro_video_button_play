
"""
Clase el cual permite almacenar datos importantes como tokens y request parameters para reutilizarlos en cada peticion
web que realicemos a la API de Claro Video.
"""
class ResponseDataObj:

    def __init__(self, json=None):

        self.user_id = ""
        self.parent_id = ""
        self.session_stringvalue = ""
        self.authpt = ""
        self.hks = ""
        self.parent_id = ""
        self.session_userhash = ""
        self.user_token = ""
        self.user_sesion = ""

        if json and 'response' in json:
            if 'user_id' in json['response']:
                self.user_id = json['response']['user_id']

            if 'parent_id' in json['response']:
                self.parent_id = json['response']['parent_id']

            if 'session_stringvalue' in json['response']:
                self.session_stringvalue = json['response']['session_stringvalue']

            if 'session_userhash' in json['response']:
                self.session_userhash = json['response']['session_userhash']

            if 'user_token' in json['response']:
                self.user_token = json['response']['user_token']

            if 'user_session' in json['response']:
                self.user_sesion = json['response']['user_session']

        if json and 'entry' in json:
            if 'authpt' in json['entry']:
                self.authpt = json['entry']['authpt']

            if 'HKS' in json['entry']:
                self.hks = json['entry']['HKS']

