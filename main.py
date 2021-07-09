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
id_group_json = IdGroupApi().main(arguments_json['node_id'], arguments_json['filter_id'])
group_id_list = id_group_json['idgrups']

hks = LoginClaroVideo.generate_hks()
authpt = LoginClaroVideo.get_authpt(session)

# acquired_resp_data = LoginClaroVideo.get_starter_header_info(authpt, hks, session)
acquired_resp_data = LoginClaroVideo.login_portal(
    arguments_json['correo'], arguments_json['password'], session, authpt, hks)

acquired_resp_data = LoginClaroVideo.push_session(acquired_resp_data, session)

for chunk_id in IterableUtils.chunker(group_id_list, 100):
    result_purchase_button_list.extend(
        MultithreadingUtils.process_data_id_group_requests(chunk_id, session, acquired_resp_data))

session.close()