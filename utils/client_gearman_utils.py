import copy
import json


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

        id_dict = {
            'node_id': ['102741',
                        '102738',
                        '102737',
                        #'102687', '102686'
                        ],
            'filter_id': [
                # '9482', '31049', '31069', '36125', '36217', '38146', '38466', '38485', '38488', '38489',
                #           '38503', '38504', '38539', '38540', '39522', '39581', '39597'
            ]
        }

        for key, value in id_dict.items():
            for id in value:
                new_args = copy.deepcopy(param_dict)

                if key == 'node_id':
                    new_args['node_id'] = id
                elif key == 'filter_id':
                    new_args['filter_id'] = id

                job_list.append(dict(task="test_claro_video_play_button", data=json.dumps(new_args)))

        return job_list
