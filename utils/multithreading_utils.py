from threading import Thread
from purchase_btn_data.purchase_btn_data import PurchaseBtnData
from requests.sessions import Session
from resp_objects.resp_user_data import ResponseDataObj


class MultithreadingUtils:

    @staticmethod
    def process_data_id_group_requests(list_group_id: list, session: Session, acquired_resp_data: ResponseDataObj,
                                       region: str, nodo_obtained: str):
        """
        Metodo el cual se encarga de la paralelizacion de las peticiones a la API de Claro Video para la obtencion
        de los datos del play button y las fechas de vigencia. Para ello se requiere la lista de group_id
        que se iterara y se usara para consultar informacion en cada peticion a la API.

        :param list_group_id:
        :param session:
        :param acquired_resp_data:
        :param region:
        :param nodo_obtained:
        :return:
        """
        threads = {}
        results = {}
        list_result = []

        for i, id in enumerate(list_group_id):
            key_name = 'thread_{}'.format(i)
            threads[key_name] = Thread(
                target=PurchaseBtnData.get_purchased_button_info_with_threading,
                args=(id, acquired_resp_data, session, results, key_name, region, nodo_obtained))

        for key, value in threads.items():
            value.start()

        for key, value in threads.items():
            value.join()

        for key, value in results.items():
            list_result.append(value)

        return list_result
