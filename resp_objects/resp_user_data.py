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

        if json:
            self.user_id = json['response']['user_id']
            self.parent_id = json['response']['parent_id']
            self.session_stringvalue = json['response']['session_stringvalue']
            self.authpt = json['entry']['authpt']
            self.hks = json['entry']['HKS']
            self.session_userhash = json['response']['session_userhash']
            self.user_token = json['response']['user_token']
            self.user_sesion = json['response']['user_session']