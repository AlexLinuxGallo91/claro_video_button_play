import requests

from id_group_data.id_group_api_data import IdGroupApi
from login_claro_video.claro_video_login import LoginClaroVideo
from utils.iterable_utils import IterableUtils
from utils.multithreading_utils import MultithreadingUtils

session = requests.Session()
group_id_list = []
result_purchase_button_list = []

acquired_resp_data = LoginClaroVideo.login_portal('dummy@gmail.com', 'dummy', session)
acquired_resp_data = LoginClaroVideo.push_session(acquired_resp_data, session)

# obtencion de la lista de id groups de la region mexico
id_group_json = IdGroupApi().main()
group_id_list = id_group_json['idgrups']

for chunk_id in IterableUtils.chunker(group_id_list, 100):
    result_purchase_button_list.extend(
        MultithreadingUtils.process_data_id_group_requests(chunk_id, session, acquired_resp_data))

