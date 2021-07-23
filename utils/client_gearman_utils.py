import json


class ClientGearmanUtils:

    @staticmethod
    def set_list_jobs():
        job_list = []
        list_filter_id = [
            9482,
            # 31069
        ]
        region = 'mexico'

        for filter_id in list_filter_id:
            data_args = {}
            data_args['user'] = 'clarovideomty01@gmail.com'
            data_args['password'] = 'C14r0.V1de0.12'
            data_args['region'] = region
            data_args['filter_id'] = filter_id
            data_args['node_id'] = ''
            data_args = json.dumps(data_args)
            job_list.append(dict(task="test_claro_video_play_button", data=data_args))

        return job_list
