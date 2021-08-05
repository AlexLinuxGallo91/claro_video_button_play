import copy
import json
from constants import constants as const

class ClientGearmanUtils:

    @staticmethod
    def generate_gearman_job_list():
        job_list = []

        param_dict = {
            "user": "clarovideomty01@gmail.com",
            "password": "C14r0.V1de0.12",
            "region": "mexico",
            "filter_id": "",
            "node_id": ""
        }

        for item in const.DICT_NODOS:
            new_args = copy.deepcopy(param_dict)
            new_args['node_name'] = item['node_name']
            new_args['node_id'] = item['node_id']
            new_args['filter_id'] = item['filter_id']

            job_list.append(dict(task="test_claro_video_play_button", data=json.dumps(new_args)))

        return job_list
