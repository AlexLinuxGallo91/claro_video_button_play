import json
from resp_objects.resp_user_data import ResponseDataObj
from requests import Session
from login_claro_video.claro_video_login import LoginClaroVideo
from constants import constants as const

class PurchaseBtnData:

    @staticmethod
    def get_purchased_button_info(group_id: int, acquired_resp_data: ResponseDataObj, session: Session):
        url_req = const.BTN_REQ_CLARO_VIDEO.format(
            acquired_resp_data.authpt, acquired_resp_data.session_stringvalue, acquired_resp_data.user_id, group_id)
        json_resp = json.loads(session.get(url_req).content)

        return json_resp

    @staticmethod
    def get_expired_date_info(group_id: int, session: Session):
        url_req = const.REQUEST_URL_COMMON.format(group_id)
        json_text = session.get(url_req).content
        json_resp = json.loads(json_text)

        json_expired_date_obtained = {}
        json_expired_date_obtained['NOMBRE_INTERNO'] = json_resp['_source']['NOMBRE_INTERNO']

        for region in json_resp['_source']['INFO_REGION_DERECHOS']:
            if region['REGION'] == 'MX':
                fecha = region['FECHA_DESDE']
                mes = fecha[4:6]
                dia = fecha[6:8]
                anio = fecha[:4]

                json_expired_date_obtained['FECHA_DESDE'] = '{}-{}-{}'.format(dia, mes, anio)

                fecha = region['FECHA_HASTA']
                mes = fecha[4:6]
                dia = fecha[6:8]
                anio = fecha[:4]

                json_expired_date_obtained['FECHA_HASTA'] = '{}-{}-{}'.format(dia, mes, anio)

        return json_expired_date_obtained

    @staticmethod
    def get_purchased_button_info_with_threading(group_id: int, acquired_resp_data: ResponseDataObj, session: Session,
                                                 result: dict, key: str):
        url_req = const.BTN_REQ_CLARO_VIDEO.format(
            acquired_resp_data.authpt, acquired_resp_data.session_stringvalue, acquired_resp_data.user_id, group_id)
        json_resp = json.loads(session.get(url_req).content)

        date_info_expiration = PurchaseBtnData.get_expired_date_info(group_id, session)
        btn_purchase_info = json_resp['response']['playButton']

        complete_json = {}
        complete_json['date_info_expiration'] = date_info_expiration
        complete_json['btn_purchase_info'] = btn_purchase_info

        result[key] = complete_json