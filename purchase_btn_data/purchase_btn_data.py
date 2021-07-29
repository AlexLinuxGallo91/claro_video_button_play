import datetime
import json

import requests
from requests import Session

from constants import constants as const
from resp_objects.resp_user_data import ResponseDataObj


class PurchaseBtnData:

    @staticmethod
    def get_purchased_button_info(group_id: int, acquired_resp_data: ResponseDataObj, session: Session):
        """
        Metodo que se encarga de hacer una peticion a la api para obtener la informacion del boton de paga

        :param group_id:
        :param acquired_resp_data:
        :param session:
        :return:
        """
        url_req = const.BTN_REQ_CLARO_VIDEO.format(
            acquired_resp_data.authpt, acquired_resp_data.session_stringvalue, acquired_resp_data.user_id, group_id)
        json_resp = json.loads(session.get(url_req).content)

        return json_resp

    @staticmethod
    def get_expired_date_info(group_id: int, session: Session):
        """
        Metodo el cual permite obtener las fechas de vigencia con respecto a un group id prorpocionado

        :param group_id:
        :param session:
        :return:
        """
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

                date_until = datetime.datetime(int(anio), int(mes), int(dia))
                json_expired_date_obtained['FECHA_HASTA'] = '{}-{}-{}'.format(dia, mes, anio)

                is_in_force = 1 if date_until >= datetime.datetime.now() else 0
                json_expired_date_obtained['VIGENCIA'] = is_in_force
                json_expired_date_obtained['group_id'] = group_id

        return json_expired_date_obtained

    @staticmethod
    def get_purchased_button_info_with_threading(group_id: int, acquired_resp_data: ResponseDataObj, session: Session,
                                                 result: dict, key: str, region: str, nodo_obtained: str):
        """
        Metodo el cual permite obtener la informacion del boton de compra de una serie con respecto a su group id
        y la informacion de las fechas de vigencia. Este metodo se llama por medio de multithreading y dentro del
        mismo se mandan a llamar las dos funciones que obtienen la informacion de las fechas y boton de pago.

        :param group_id: group id de la serie a buscar
        :param acquired_resp_data:
        :param session:
        :param result:
        :param key:
        :param region:
        :param nodo_obtained:
        :return:
        """
        url_req = const.BTN_REQ_CLARO_VIDEO.format(
            acquired_resp_data.authpt, region, acquired_resp_data.session_stringvalue, acquired_resp_data.user_id,
            group_id)

        try:
            resp = session.get(url_req).content
            json_resp = json.loads(resp)

            date_info_expiration = PurchaseBtnData.get_expired_date_info(group_id, session)
            btn_purchase_info = json_resp['response']['playButton']

            complete_json = {}
            complete_json['date_info_expiration'] = date_info_expiration
            complete_json['playButton'] = btn_purchase_info
            complete_json['nodo'] = nodo_obtained

            result[key] = complete_json
        except json.decoder.JSONDecodeError:
            pass
        except requests.exceptions.ConnectionError:
            pass
        except TypeError:
            pass
