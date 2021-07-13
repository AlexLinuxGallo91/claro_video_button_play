import json

import requests

from id_group_data.id_group_api_data import IdGroupApi
from login_claro_video.claro_video_login import LoginClaroVideo
from utils.iterable_utils import IterableUtils
from utils.multithreading_utils import MultithreadingUtils
from utils.arguments_utils import ArgumentsUtils

session = requests.Session()
group_id_list = []
result_purchase_button_list = []

ArgumentsUtils.verify_argument()
arguments_json = ArgumentsUtils.convert_arg_to_dict()

# obtencion de la lista de id groups de la region mexico
id_group_json = IdGroupApi().main(arguments_json['node_id'], arguments_json['filter_id'], arguments_json['region'])
group_id_list = id_group_json['idgrups']

hks = LoginClaroVideo.generate_hks()
authpt = LoginClaroVideo.get_authpt(session)

# acquired_resp_data = LoginClaroVideo.get_starter_header_info(authpt, hks, session)
acquired_resp_data = LoginClaroVideo.login_portal(
    arguments_json['user'], arguments_json['password'], session, authpt, hks, arguments_json['region'])

acquired_resp_data = LoginClaroVideo.push_session(acquired_resp_data, session, arguments_json['region'])

for chunk_id in IterableUtils.chunker(group_id_list, 49):
    result_purchase_button_list.extend(
        MultithreadingUtils.process_data_id_group_requests(
            chunk_id, session, acquired_resp_data, arguments_json['region']))

result_purchase_button_list = {'result': result_purchase_button_list}
json_string = json.dumps(result_purchase_button_list)
session.close()

print(json_string)
