from requests.sessions import Session
from resp_objects.resp_user_data import ResponseDataObj
import constants.constants as const
import json
import string
import random
from bs4 import BeautifulSoup


class LoginClaroVideo:

    @staticmethod
    def get_authpt(session: Session):
        resp = session.get(const.LOGIN_MAIN_PAGE)
        soup = BeautifulSoup(resp.content, 'html5lib')
        list_script_tags = soup.find_all('script')
        dict_params = {}

        for script_tag in list_script_tags:

            text = script_tag.text.strip()

            if 'window.claro = ' in text:
                text = text.replace('window.claro = ','')
                text = text.replace(';', '')

                for l in text.splitlines():

                    if 'apiParams:' in l.strip():
                        l = l.replace('apiParams:','')
                        l = l.strip()
                        l = l.rstrip(l[-1])
                        dict_params = json.loads(l)

        if 'authpt' in dict_params.keys():
            return dict_params['authpt']
        else:
            return ''

    @staticmethod
    def get_starter_header_info(authpt, hks, session: Session):
        resp = session.post(const.POST_STARTER_HEADER_INFO.format(authpt, hks))
        json_resp = json.loads(resp.content)

        return json_resp

    @staticmethod
    def login_portal(username, password, session: Session, authpt, hks):
        data = dict(username=username, password=password)
        resp = session.post(const.LOGIN_REQ_CLARO_VIDEO.format(authpt, hks), data)
        json_resp = json.loads(resp.content)
        acquired_resp_data = ResponseDataObj(json_resp)

        return acquired_resp_data

    @staticmethod
    def push_session(acquired_resp_data: ResponseDataObj, session: Session):
        data = dict(user_session=acquired_resp_data.user_sesion)
        url_req = const.PUSH_SESION_REQ_CLARO_VIDEO.format(
            acquired_resp_data.user_id, acquired_resp_data.authpt, acquired_resp_data.session_stringvalue)
        resp = session.post(url_req, data)
        acquired_resp_data.session_stringvalue = session.cookies.get_dict()[const.COOKIE_PHPSESSION_ID]

        return acquired_resp_data

    @staticmethod
    def generate_hks():
        return ''.join((random.choice(string.ascii_letters) for x in range(26)))