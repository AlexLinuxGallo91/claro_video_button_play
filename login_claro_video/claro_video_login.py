from requests.sessions import Session
from resp_objects.resp_user_data import ResponseDataObj
import constants.constants as const
import json


class LoginClaroVideo:

    @staticmethod
    def login_portal(username, password, session: Session):
        data = dict(username=username, password=password)
        resp = session.post(const.LOGIN_REQ_CLARO_VIDEO, data)
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
    def get_purchased_button_info(group_id: int, acquired_resp_data: ResponseDataObj, session: Session):
        url_req = const.BTN_REQ_CLARO_VIDEO.format(
            acquired_resp_data.authpt, acquired_resp_data.session_stringvalue, acquired_resp_data.user_id, group_id)
        json_resp = json.loads(session.get(url_req).content)

        return json_resp
