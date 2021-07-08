from threading import Thread
from purchase_btn_data.purchase_btn_data import PurchaseBtnData
from requests.sessions import Session
from resp_objects.resp_user_data import ResponseDataObj


class MultithreadingUtils:

    @staticmethod
    def process_data_id_group_requests(list_group_id: list, session: Session, acquired_resp_data: ResponseDataObj):
        threads = {}
        results = {}
        list_result = []

        for i, id in enumerate(list_group_id):
            key_name = 'thread_{}'.format(i)
            threads[key_name] = Thread(
                target=PurchaseBtnData.get_purchased_button_info_with_threading,
                args=(id, acquired_resp_data, session, results, key_name))

        for key, value in threads.items():
            value.start()

        for key, value in threads.items():
            value.join()

        for key, value in results.items():
            list_result.append(value)

        return list_result
